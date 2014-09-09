import redis

from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from polls.models import Question, Choice
from django.db.models import F
from django.core.urlresolvers import reverse

@csrf_exempt
def home(request):
    questions = Question.objects.all()

    if request.method == 'POST':
        question_id = request.POST['question_id']

        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return redirect(reverse('home'))

        else:
            Choice.objects.create(question=question, 
                                  user_agent=request.META.get('HTTP_USER_AGENT', ''))

            Question.objects.filter(id=question.id).update(counter=F('counter')+1)
            messages = Question.objects.values_list('counter', flat=True)
            message = ",".join([str(i) for i in messages])

            r = redis.StrictRedis()
            r.publish('my_channel', message)
            print message

        return redirect(reverse('polls:thankyou'))

    return render(request, "polls/home.html", {'questions': questions})


def dashboard(request):
    questions = Question.objects.all().order_by('id')

    return render(request, "polls/dashboard.html", {'questions': questions})


def thankyou(request):
    questions = Question.objects.all().order_by('id')
    total = Choice.objects.count()
    return render(request, "polls/thankyou.html", {'questions': questions,
                                                   'total': total})


def reset(request):
    Question.objects.all().update(counter=0)
    Choice.objects.all().delete()
    return HttpResponse("OK")
