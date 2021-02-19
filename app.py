from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def hello():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)