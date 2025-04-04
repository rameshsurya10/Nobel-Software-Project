from flask import request,jsonify
import mysql.connector as mc
from mysql.connector import Error
import jwt 
import datetime


def db_cn():
    return mc.connect(
            host = "localhost",
            user = "root",
            password = "Rameshsurya@08",
            database = "website"
        )
    

def Log(data):
    

    db = db_cn()

    connection = None
    cursor = None

    try:

        if db.is_connected():

            cursor = db.cursor()

            data = request.get_json()

            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return jsonify({"Error":"All Fields are Required..."})
             
            
            else:
        
                query = """select * from members where username = %s and password = %s"""


                cursor.execute(query,(username,password))

                result = cursor.fetchall()
                print(result)
                db.commit()

            if result:
                 SECRET_KEY = 'Honey123'
                 payload = {
                    'username': username,
                    'password': password,
                    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)  # Token expiration time
                }

                 # Generate the JWT token
                 encoded_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

                 decode_token = jwt.decode(encoded_token, SECRET_KEY, algorithms=['HS256'])

                 return jsonify({
                     'message': 'Login successful',
                     'token': encoded_token,
                     'decode': decode_token 
                 })
            
    
            else:
                return jsonify({"Error": "Username and password is mismatched..."})
                         
    except Error as er:
        return jsonify({"Error":f"Unable to connect the server {str(er)}"})
    

#Forgot password

def passwd(data):

    db = db_cn()

    connection = None
    cursor = None

    try:

        if db.is_connected():

            cursor = db.cursor()

            data = request.get_json()

            user_name = data.get("username")
            password = data.get("password")
            con_password = data.get("con_password")

            if not user_name or not password or not con_password :
                return jsonify({"Error":"Username Required..."})
            
            if password != con_password:
                return jsonify({"Error":"Password is Mismatched..."})
            
            check_un = "SELECT * FROM members WHERE username = %s"
            cursor.execute(check_un, (user_name,))
            result = cursor.fetchone()
            
            if result:
                data = "UPDATE members set password = %s WHERE username = %s"
                cursor.execute(data, (password,user_name))
                db.commit()
                    
            if cursor.rowcount>0:
                return jsonify({"Result":"Password Updated successfull..."})
            else:
                return jsonify({"Error": "Password is not Updated..."})
                         
    except Error as er:
        return jsonify({"Error":f"Unable to connect the server {str(er)}"})
    

#Forgot username


def ur_name(data):

    db = db_cn()

    connection = None
    cursor = None

    try:

        if db.is_connected():

            cursor = db.cursor()

            data = request.get_json()

            email = data.get("email")
            ur_name = data.get("ur_name")
            con_ur_name = data.get("con_ur_name")

            if not email or not ur_name or not con_ur_name :
                return jsonify({"Error":"mail_id Required..."})
            
            if ur_name != con_ur_name:
                return jsonify({"Error":"User_name is Mismatched..."})
            
            check_un = "SELECT * FROM members WHERE email = %s"
            cursor.execute(check_un, (email,))
            result = cursor.fetchone()
            
            if result:
                data = "UPDATE members set username = %s WHERE email = %s"
                cursor.execute(data, (ur_name,email))
                db.commit()
                    
            if cursor.rowcount>0:
                return jsonify({"Result":"Username Updated successfull..."})
            else:
                return jsonify({"Error": "Username is not Updated..."})
                         
    except Error as er:
        return jsonify({"Error":f"Unable to connect the server {str(er)}"})
    

