from flask import Flask, redirect, render_template, request, session, url_for, make_response
app = Flask(__name__)
app.secret_key = "session_secrect_key"

@app.route("/")
def hello_world():
    name = request.cookies.get("userID")
    if name and session:
        return "Hello "+name+" "+session["username"]
    else:
        return "Hello world!"

@app.route("/html")
def hello_html():
    session.pop("username", None)
    return "<html><body><h1>Hello World</h1></body></html>"

@app.route("/html/<name>")
def hello_html_param(name):
    session["username"] = "Test user"
    resp = make_response(render_template("hello.html", name=name))
    resp.set_cookie('userID', name)
    return resp

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

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return user

@app.route("/redirect/<name>")
def redirect_admin(name):
    if name == "admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_name', name=name))

if __name__ == '__main__':
    app.run(debug=True)