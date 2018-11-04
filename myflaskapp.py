from flask import Flask, render_template, flash, request, url_for, redirect

from PIL import Image
from smbus import SMBus
import time


slave_address = 0x69
def __init__(self,address = 69, bus = default_bus):
    self.file_read = io.open("/dev/i2c-"+str(bus),"rb",buffering=0)
    self.file_write = io.open("/dev/i2c-"+str(bus),"wb",buffering = 0)

app= Flask(__name__)

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/handle_data',methods=['GET','POST'])
def handle_data():
    if request.method =="POST":

        data = request.form
        i=1
        sendToKurt= []
        sendToKurt.append(1)
        alsoSend = []
        alsoSend.append(len(data))
        for key in data.keys():
            for val in data.getlist('in'+str(i)):
                i+=1
                value = val[1:-1]
                x_raw, y_raw = value.split(",")
                X_int = int(x_raw)
                Y_int = int(y_raw)
                alsoSend.append((X_int,Y_int))
        sendToKurt.append(alsoSend)
        print (sendToKurt) 
        bus.write_block_data(slave_address,69,sendToKurt)
    return redirect(url_for('render'))


if __name__=='__main__':
    app.run(debug=True)
