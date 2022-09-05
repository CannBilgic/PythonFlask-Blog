from flask import Flask, request, jsonify, Blueprint
from blog.models import Articles

apiArticles = Blueprint('apiArticles', __name__, url_prefix='/api/articles')


@apiArticles. route('/', methods=["GET", "POST"])
def articles_list():
    try:
        allArticles = Articles.get_all_articles()
        article = []
        for articles in allArticles:
            article.append({"id": articles.id, "title": articles.title, "text": articles.text, "privacyStatus_id": articles.privacyStatus_id,
                         "comment_status": articles.comment_status, "users_id": articles.users_id})
        return jsonify( article)
    except Exception as e:
        # print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})



@apiArticles.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def articles_delete_update_list(id):

    try:
        articles = Articles.get_articles_by_id(id)
        if articles == None:
            return jsonify({"succes": False, "message": "Articles not found"})

        if request.method == "GET":
            userObj = {"id": articles.id, "title": articles.title, "text": articles.text, "privacyStatus_id": articles.privacyStatus_id,
                         "comment_status": articles.comment_status, "users_id": articles.users_id}
            return jsonify( userObj)

        elif request.method == "DELETE":
            Articles.delete_articles(id)
            return jsonify({"succes": True, "message": "Articles deleted"})

        elif request.method == "PUT":
            title = request.form.get("title")
            text = request.form.get("text")
            privacyStatus_id = request.form.get("privacyStatus_id")
            comment_status = request.form.get("comment_status")
            users_id = request.form.get("users_id")

            if title == None:
                title = articles.title
            if text == None:
                text = articles.text
            if privacyStatus_id == None:
                privacyStatus_id = articles.privacyStatus_id
            if comment_status == None:
                comment_status = articles.comment_status
            if users_id == None:
                users_id = articles.users_id
            Articles.update_articles(id, title, text,
                               privacyStatus_id, comment_status,users_id)

            return jsonify({"succes": True, "message": "Articles updated"})

    except Exception as e:
        print("Eror:", e)
        return jsonify({"success": False, "message": "There is an error"})

@apiArticles.route("/addarticles", methods=["GET", "POST"])
def addArticles():
    try:
        title = request.form.get("title")
        text = request.form.get("text")
        privacyStatus_id = request.form.get("privacyStatus_id")
        comment_status = request.form.get("comment_status")
        users_id = request.form.get("users_id")
        Articles.add_articles(title, text, privacyStatus_id, comment_status, users_id)
        return jsonify({"success": True, "message": "Articles add a succesfully..."})
    except Exception as e:
        print("Eror:",e)
        return jsonify({"success": False, "message": "There is an error"})