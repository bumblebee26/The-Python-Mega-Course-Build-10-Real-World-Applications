from flask import Flask

app=Flask(__name__)

@app.route('/about/')
def about():
    return "About content goes here."

@app.route('/')
def home():
    return "Homepage."

if __name__=="__main__":
    app.run(debug=True)
