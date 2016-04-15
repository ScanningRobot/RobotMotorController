var express = require('express'), http = require('http');
var app = express();
var server = http.createServer(app);
var bodyParser = require('body-parser')

// Parse json get request
app.use(bodyParser.json());

// START ROBOT PROCESS
const spawn = require('child_process').spawn;
const robot = spawn('python', ['-u', 'serverTest.py']);

robot.stdin.setEncoding('utf-8');
robot.stdout.setEncoding('utf-8');

robot.stdout.on('data', (data) => {
  console.log(data);
});

robot.stderr.on('data', (data) => {
  console.log(`stderr: ${data}`);
});

robot.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});

robot.on('message', function(message) {
  console.log('Received message...');
  console.log(message);
});

// Listen for commands to forward to robot from the Android App
app.post('/moveRobot', function(req, res) {
  console.log(req.body.direction);
  robot.stdin.write(req.body.direction + '\n');
  res.send("200")
});

server.listen(8080, function () {
  var port = server.address().port
  console.log("Robot is listening at http://localhost:%s", port)
})
