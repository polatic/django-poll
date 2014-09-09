var express = require('express');
var sockjs  = require('sockjs');
var http    = require('http');
var redis   = require('redis');

var sockjs_example = sockjs.createServer(
    {sockjs_url: "http://cdn.sockjs.org/sockjs-0.3.min.js"}
);

sockjs_example.on('connection', function(connection) {
    var client = redis.createClient();
    client.subscribe('my_channel');

    client.on("message", function(channel, message){
        connection.write(message);
    });

});

var my_app = express();
var server = http.createServer(my_app);

sockjs_example.installHandlers(server,
    {prefix:'/example'}
);

server.listen(8080, '0.0.0.0');