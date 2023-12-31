import RPi.GPIO as GPIO
from flask import Flask, render_template
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 26
senPIR = 27
buttonSts = 0
senPIRSts = 0
   
# Set button and PIR sensor pins as an input
GPIO.setup(button, GPIO.IN)   
GPIO.setup(senPIR, GPIO.IN)
    
@app.route("/")
def index():
    # Read Sensors Status
    buttonSts = GPIO.input(button)
    senPIRSts = GPIO.input(senPIR)
    templateData = {
      'title' : 'GPIO input Status!',
      'button'  : buttonSts,
      'senPIR'  : senPIRSts
      }
    return render_template('InputRead_Web.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
