from flask import Flask
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)

app = Flask(__name__)

GPIO.output(4, 0)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/blink')
def blink():
    print('blinked')
    GPIO.output(4, 1)
    time.sleep(5)
    GPIO.output(4, 0)
    return 'LED Blinked'

if __name__ == '__main__':
    app.run()