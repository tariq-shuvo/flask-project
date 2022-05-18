from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/html")
def hello_html():
    return "<html><body><h1>Hello World</h1></body></html>"

@app.route("/html/<name>")
def hello_html_param(name):
    return render_template("hello.html", name=name)

@app.route("/html/marks/<int:mark>")
def marks_html_param(mark):
    return render_template("mark.html", mark=mark)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s!" %name

@app.route("/blog/<int:postID>")
def blog(postID):
    return "Blog number is %d!" %postID

@app.route("/rev/<float:revNo>")
def revision(revNo):
    return "Revision number is %f!" %revNo

@app.route("/redirect/<name>")
def redirect_admin(name):
    if name == "admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_name', name=name))

if __name__ == '__main__':
    app.run(debug=True)