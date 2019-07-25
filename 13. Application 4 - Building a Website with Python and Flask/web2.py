## web2.py

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home1.html")

@app.route('/about/')
def about():
    return render_template("about1.html")

if __name__=="__main__":
    app.run(debug=True)
