from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s!" %name

@app.route("/blog/<int:postID>")
def blog(postID):
    return "Blog number is %d!" %postID

@app.route("/rev/<float:revNo>")
def revision(revNo):
    return "Revision number is %f!" %revNo

if __name__ == '__main__':
    app.run(debug=True)