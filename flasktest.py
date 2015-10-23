from flask import Flask
import RPi.GPIO as GPIO
import time

GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/blink')
def blink():
    print('blinked')
    GPIO.output(11, True)
    time.sleep(1)
    GPIO.output(11, False)
    return 'LED Blinked'

if __name__ == '__main__':
    app.run()