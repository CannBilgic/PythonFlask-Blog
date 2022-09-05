from flask import Flask, request, jsonify, Blueprint
from blog.models import Tags

apiTags = Blueprint('apiTags', __name__, url_prefix='/api/tags')



@apiTags. route('/', methods=["GET", "POST"])
def tags_list():
    try:
        allTags = Tags.get_all_tags()
        tags = []
        for tag in allTags:
            tags.append({"id": tag.id, "name": tag.title,"articles_id":tag.articles_id})
        return jsonify({"success": True, "data": tags})
    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiTags.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def tags_delete_update_list(id):

    try:
        tags = Tags.get_tags_by_id(id)
        if tags == None:
            return jsonify({"succes": False, "message": "tags not found"})

        if request.method == "GET":
            tagsObj = {"id": tags.id, "name": tags.title,"articles_id":tags.articles_id}
            return jsonify({"success": True, "data": tagsObj})

        elif request.method == "DELETE":
            tags.delete_tags(id)
            return jsonify({"succes": True, "message": "tags deleted"})

        elif request.method == "PUT":
            title = request.form.get("title")


            if title == None:
                title = tags.title
            if articles_id == None:
                articles_id = tags.articles_id
           
            Tags.update_tags(id, title,articles_id)

            return jsonify({"succes": True, "message": "Tags updated"})

    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiTags.route("/addtags", methods=["GET", "POST"])
def addTags():
    try:
        title = request.form.get("title")
        articles_id = request.form.get("articles_id")
        
        Tags.add_tags(title,articles_id)
        return jsonify({"success": True, "message": "Tags add a succesfully..."})
    except Exception as e:
        print("Eror:",e)
        return jsonify({"success": False, "message": "There is an error"})