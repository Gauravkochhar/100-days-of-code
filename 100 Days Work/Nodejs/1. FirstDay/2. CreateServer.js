var http= require('http');
var server=http.createServer(function(req,res)
{
	res.writeHead(200,{"Content-Type":"text/plain"});
	res.end("Welcome To my First Server Program.");
});
server.listen(1234,function()
{
	console.log("Server is Started go to browser to run the program at 1234 port of localhost");
});




//Run This Program At ("http://localhost:1234//")
