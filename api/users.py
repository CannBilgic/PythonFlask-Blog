
from datetime import datetime
from flask import Flask, request, jsonify, Blueprint
from flask_cors import cross_origin

from blog import Config
from blog.models import Users
import jwt,datetime
apiUsers = Blueprint('apiUsers', __name__, url_prefix='/api/users')


@apiUsers. route('/', methods=["GET", "POST"])
def users_list():
    try:
        allUsers = Users.get_all_users()
        user = []
        for users in allUsers:
            user.append({"id": users.id, "name": users.name, "surname": users.surname, "username": users.username,
                         "email": users.email, "phonNumber": users.phonNumber, "password": users.password})
        return jsonify({"success": True, "data": user})
    except Exception as e:
        # print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})



@apiUsers.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def users_delete_update_list(id):

    try:
        users = Users.get_users_by_id(id)
        if users == None:
            return jsonify({"succes": False, "message": "user not found"})

        if request.method == "GET":
            userObj = {"id": users.id, "name": users.name, "surname": users.surname, "username": users.username,
                       "email": users.email, "phonNumber": users.phonNumber, "password": users.password}
            return jsonify({"success": True, "data": userObj})

        elif request.method == "DELETE":
            users.delete_users(id)
            return jsonify({"succes": True, "message": "user deleted"})

        elif request.method == "PUT":
            name = request.form.get("name")
            surname = request.form.get("surname")
            username = request.form.get("username")
            email = request.form.get("email")
            phonNumber = request.form.get("phonNumber")
            password = request.form.get("password")

            if name == None:
                name = users.name
            if surname == None:
                surname = users.surname
            if username == None:
                username = users.username
            if email == None:
                email = users.email
            if phonNumber == None:
                phonNumber = users.phonNumber
            if password == None:
                password = users.password
            Users.update_users(id, name, surname, username,
                               email, phonNumber, password)

            return jsonify({"succes": True, "message": "user updated"})

    except Exception as e:
        #print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})

@apiUsers.route("/addusers", methods=["GET", "POST"])
def addUsers():
    try:
        name = request.form.get("name")
        surname = request.form.get("surname")
        username = request.form.get("username")
        email = request.form.get("email")
        phonNumber = request.form.get("phonNumber")
        password = request.form.get("password")
        Users.add_users(name, surname, username, email, phonNumber, password)
        return jsonify({"success": True, "message": "users add a succesfully..."})
    except Exception as e:
        print("Eror:",e)
        return jsonify({"success": False, "message": "There is an error"})


@apiUsers.route("/login",methods=["POST"])
@cross_origin()
def login():
    try:
        username=request.form.get("username")
        password=request.form.get("password")
        users = Users.get_users_by_username(username)
        response =''
        status = 200
        if users != None and users.username == username and users.password== password:
            token=jwt.encode({
                'username': users.username,
                'id':users.id,

                'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
            },Config.SECRET_KEY)
            response = {"success": True, "token": token, "message": "Succes Login"}
        else:
            status = 404
            response = {"success": False,"message": 'invaild username or password'}

        return jsonify(response), status
    except Exception as e:
        print("Eror:",e)
        return jsonify({"success": False, "message": "There is an error"}),500

    