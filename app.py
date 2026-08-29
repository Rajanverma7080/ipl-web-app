from flask import Flask

app=Flask(__name__)


@app.route('/')
def home():
    return 'create and connect to the server'


app.run(debug=True)