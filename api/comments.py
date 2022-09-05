from flask import Flask, request, jsonify, Blueprint
from blog.models import Comments

apiComments = Blueprint('apiComments', __name__, url_prefix='/api/comments')


@apiComments. route('/', methods=["GET", "POST"])
def Comments_list():
    try:
        allComments = Comments.get_all_comments()
        comment = []
        for comments in allComments:
            comment.append({"id": comments.id, "users_id": comments.users_id, "articles_id": comments.articles_id, "comment": comments.comments})
        return jsonify({"success": True, "data": comment})
    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})



@apiComments.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def comments_delete_update_list(id):

    try:
        comments = Comments.get_comments_by_id(id)
        if comments == None:
            return jsonify({"succes": False, "message": "comments not found"})

        if request.method == "GET":
            commentsObj = {"id": comments.id, "users_id": comments.users_id, "articles_id": comments.articles_id, "comment": comments.comments,
                         "created_at": comments.created_at}
            return jsonify({"success": True, "data": commentsObj})

        elif request.method == "DELETE":
            comments.delete_comments(id)
            return jsonify({"succes": True, "message": "comments deleted"})

    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})

@apiComments.route("/addcomments", methods=["GET", "POST"])
def addUsers():
    try:
        users_id = request.form.get("users_id")
        articles_id = request.form.get("articles_id")
        comment = request.form.get("comment")
        Comments.add_comments(users_id, articles_id, comment)
        return jsonify({"success": True, "message": "comment add a succesfully..."})
    except Exception as e:
        print("Eror:",e)
        return jsonify({"success": False, "message": "There is an error"})