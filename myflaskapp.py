from flask import Flask, render_template, flash, request, url_for, redirect
from time import sleep
from PIL import Image
from smbus import SMBus

addr =0x69
bus = SMBus(1)


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
	bus.write_byte(addr,len(data))
	for key in data.keys():
            for val in data.getlist('in'+str(i)):
                i+=1
                value = val[1:-1]
                x_raw, y_raw = value.split(",")
                X_int = int(x_raw)
                Y_int = int(y_raw)
		pnts = []
		pnts.append(X_int)
		pnts.append(Y_int)
		bus.write_i2c_block_data(addr,0,pnts)
                alsoSend.append((X_int,Y_int))
		sleep(0.05)
        sendToKurt.append(alsoSend)
	print (alsoSend) 
    return redirect(url_for('render'))


if __name__=='__main__':
    app.run(debug=True)
