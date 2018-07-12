const { spawn } = require('child_process');

const charsIn = l => r => l.map(w => r.includes(w)).every(identity)

const identity = _ => _

const inputs = [
  // square
  '1\n10\n',
  // rectangle
  '2\n5\n5\n',
  // triangle
  '3\n7\n12\n',
  // rectangle
  '4\n10\n',
  // invalid input
  '42\n',
].reverse()

const tests = [
  [identity,
  identity,
  charsIn(['100', 'square'])],
  [identity,
  identity,
  identity,
  charsIn(['25', 'rectangle'])],
  [identity,
  identity,
  identity,
  charsIn(['42', 'triangle'])],
  [identity,
  identity,
  charsIn(['314', 'circle'])],
  [identity,
  identity]
].reverse()

const tester = (times) => {
  if (times == 0) process.exit()
  const py3 = spawn('python3', ['solution.py']);

  py3.stdin.setEncoding('utf-8');
  py3.stdin.write(inputs.pop())

  py3.stdout.on('data', (data) => {
    t = tests[times - 1].shift()
    o = t(String(data))
    if (o) {
      console.log(`stdout: ${data}`);
    } else {
      console.error(`Test failed: ${data}`)
      py3.kill('SIGINT')
      process.exit()
    }
  });

  py3.stderr.on('data', (data) => {
    console.error(`Test failed: ${data}`)
    py3.kill('SIGINT')
    process.exit()
  });

  py3.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    tester(times - 1)
  });
}

tester(5)
