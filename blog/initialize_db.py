from blog.models import db
from blog import createApp
def CreateDB():
    db.create_all(app=createApp())