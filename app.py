from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app= Flask(__name__)

#hardcode vaules
valid_username= "Radha"
valid_pwd= "Radha123"

#initializing the database and create table



@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    # dynamically rendering user name from website- 1st
    # if request.method == 'POST':
    #     username=request.form['username']
    #     # password=request.form['password']
    #     return redirect(url_for('success',name=username))
    # else:
    #     user=request.args.get('username')
    #     return redirect(url_for('success',name=username))

    #login -2nd
    username=request.form.get("username")
    password=request.form.get("password")
    
    if username==valid_username and password==valid_pwd:
        return render_template("success.html",username=username)
    else:
        return "Invalid credentials.Please try again."
    

#1st -dynamic username
# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' %name  #string

# @app.route('/success/<int: age>')
# def success(age):
#     return 'welcome %d' %age  #int,%.2f -float



#login-2nd(optional-no use)
@app.route("/success")
def success():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug= True)


