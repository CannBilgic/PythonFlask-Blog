
from blog import createApp
from blog.initialize_db import CreateDB
from api.users import apiUsers
from api.tags import apiTags
from api.privacy import apiPrivacyStatus
from api.articles import apiArticles
from api.comments import apiComments


app = createApp()
CreateDB()

app.register_blueprint(apiUsers)
app.register_blueprint(apiTags)
app.register_blueprint(apiPrivacyStatus)
app.register_blueprint(apiArticles)
app.register_blueprint(apiComments)





if __name__ == "__main__":
    app.run(debug=True)
