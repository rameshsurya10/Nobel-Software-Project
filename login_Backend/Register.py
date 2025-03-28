from flask import request,jsonify
import mysql.connector as mc
from mysql.connector import Error

def Reg(data):

    connection = None
    cursor = None

    try:
        db = mc.connect(
            host = "localhost",
            user = "root",
            password = "Rameshsurya@08",
            database = "website"
            )

        if db.is_connected():

            cursor = db.cursor()

            cursor.execute(
                """create table if not exists members
                (id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                mobile_number VARCHAR(255) NOT NULL,
                password varchar(255) NOT NUll)"""
            )

            data = request.get_json()

            username = data.get("username")
            email = data.get("email")
            mobile_number = data.get("mobileno")
            password = data.get("password")
            confirm_password = data.get("con_password")

            if not username or not email or not mobile_number or not password:
                return jsonify({"Error":"All Fields are Required..."})    

            
            else:
                if password == confirm_password:

                    query = """insert into members (username,email,mobile_number,password)
                    values(%s,%s,%s,%s)"""
                    
                    dt = (username,email,mobile_number,password)
                    cursor.execute(query,dt)
                    cursor.fetchall()
                    db.commit()
                    return jsonify({"Result":"Data has been successfully added..."})
                
                
                else:
                    return jsonify({"Match Error": "Password is mismatched..."})
                
    except Error as er:
        return jsonify({"Error":f"Unable to connect the server {str(er)}"})

