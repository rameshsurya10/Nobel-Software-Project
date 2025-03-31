from flask import Flask,request,jsonify
from Register import Reg
from Login import Log,ur_name,passwd
 

app = Flask(__name__)



# For Registration

@app.route("/Register",methods = ["Post"])

def Regi():

    data = request.get_json()
 
    return Reg(data)

# For Login

@app.route("/Login",methods = ["Post"])

def Login():

    data = request.get_json()

    return Log(data)

# For Update password

@app.route("/Login/password",methods = ["Post"])

def password():

    data = request.get_json()

    return passwd(data)

# For Update User name

@app.route("/Login/username",methods = ["Post"])

def user_name():

    data = request.get_json()

    return ur_name(data)


if __name__ == "__main__":
    app.run(debug=True)