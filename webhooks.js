
var http = require('http');
var callfile = require('child_process');

const PORT = 8011;

function handleRequest(request, response) {
	console.log("webhooked.");
	response.end('gotcha');
	callfile.execFile('autoblog.sh', [], null, function (err, stdout ,stderr) {
		console.log(stdout);
	});
}

var server = http.createServer(handleRequest);

server.listen(PORT, function() {
	console.log("Webhooks Server started listening port %s", PORT);
});
