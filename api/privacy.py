from flask import Flask, request, jsonify, Blueprint
from blog.models import PrivacyStatus

apiPrivacyStatus = Blueprint('apiPrivacyStatus', __name__, url_prefix='/api/privacyStatus')



@apiPrivacyStatus. route('/', methods=["GET", "POST"])
def privacyStatus_list():
    try:
        allPrivacyStatus = PrivacyStatus.get_all_privacyStatus()
        privacyStatus = []
        for Status in allPrivacyStatus:
            privacyStatus.append({"id": Status.id, "status": Status.status})
        return jsonify({"success": True, "data": privacyStatus})
    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiPrivacyStatus.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def privacyStatus_delete_update_list(id):

    try:
        privacyStatus = PrivacyStatus.get_privacyStatus_by_id(id)
        if privacyStatus == None:
            return jsonify({"succes": False, "message": "PrivacyStatus not found"})

        if request.method == "GET":
            privacyStatusObj = {"id": privacyStatus.id, "name": privacyStatus.status}
            return jsonify({"success": True, "data": privacyStatusObj})

        elif request.method == "DELETE":
            privacyStatus.delete_privacyStatus(id)
            return jsonify({"succes": True, "message": "PrivacyStatus deleted"})

        elif request.method == "PUT":
            status = request.form.get("status")
           
            PrivacyStatus.update_privacyStatus(id, status)

            return jsonify({"succes": True, "message": "PrivacyStatus updated"})

    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiPrivacyStatus.route("/addprivacyStatus", methods=["GET", "POST"])
def addprivacyStatus():
    try:
        status = request.form.get("status")
        
        PrivacyStatus.add_privacyStatus(status)
        return jsonify({"success": True, "message": "PrivacyStatus add a succesfully..."})
    except Exception as e:
        #print("Eror:",e)
        return jsonify({"success": False, "message": "There is an error"})