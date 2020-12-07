from flask import Flask, render_template, url_for, request, session, redirect

import json

app = Flask(__name__)
# signup or home page
@app.route("/", methods=["GET","POST"])
def home():
  if request.method=="POST":
    name = request.form.get("name")
    password = request.form.get("password")
    email = request.form.get("email")
    data = {
      "name":name,
      "email":email,
      "password":password,
    }
    f = open("data.txt","a")
    f.write(json.dumps(data))
    f.write("\n")
    f.close()
    return render_template("tologin.html")
  
  return render_template("signup.html")


#login page
@app.route("/login", methods=["GET","POST"])
def login():
  if request.method=="POST":
    email = request.form.get("email")
    password = request.form.get("password")
    f = open("data.txt","r")
    for i in f:
      j = json.loads(i)
      if j["email"]==email and j["password"]==password:
        return render_template("index.html")
    else:
      return render_template("signup.html")
  else:
    return render_template("login.html")




if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=5000  # Randomly select the port the machine hosts on.
	)
