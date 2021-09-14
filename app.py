from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/index')
def index():
    obj = {
        "title" : "這是一個標題",
        "body" : "這是一個內容",
        "show" : False
    }
    return render_template("index.html", obj=obj)

if __name__ == '__main__':
    app.run(debug=True)