from flask import Flask, render_template, request
import qrcode
import os

IMG_FOLDER=os.path.join('static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=IMG_FOLDER


@app.route('/', methods=['POST','GET'])
def hello_world():  # put application's code here
    return render_template('base.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    inp_string = request.form['inp']
    img = qrcode.make(inp_string)
    img.save("/home/fernblade/PycharmProjects/qrcode/static/1.png")
    img_filename=os.path.join(app.config["UPLOAD_FOLDER"], '1.png')
    return render_template('base.html', img_filename=img_filename)


if __name__ == '__main__':
    app.run()
