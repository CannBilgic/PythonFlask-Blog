from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from blog import db


class Base(db.Model):

    __abstract__ = True

    @declared_attr
    def created_at(cls):
        return db.Column(db.DateTime, default=datetime.now())

    @declared_attr
    def updated_at(cls):
        return db.Column(db.DateTime, onupdate=datetime.now())


@dataclass
class Users(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30))
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    phonNumber = db.Column(db.String(13), unique=True)
    password = db.Column(db.String(16), nullable=False)

    def __init__(self, id, name, surname, username, email, phonNumber, password, ):
        self.id = id
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.phonNumber = phonNumber
        self.password = password

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def get_users_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    @classmethod
    def get_users_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def add_users(cls,name, surname, username, email, phonNumber, password, ):
        user = cls(None,name, surname, username, email,
                   phonNumber, password)
        db.session.add(user)
        db.session.commit()
    @classmethod
    def update_users(cls,id,name, surname, username, email, phonNumber, password):
        user=cls.query.filter_by(id=id).first()
        user.name = name
        user.surname = surname
        user.username = username
        user.email = email
        user.phonNumber = phonNumber
        user.password = password
        db.session.commit()
    @classmethod
    def delete_users(cls,id):
        user= cls.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()


@dataclass
class PrivacyStatus(db.Model):

    __tablename__ = 'privacyStatus'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(30))

    def __init__(self, id, status):
        self.id = id
        self.status = status

    @classmethod
    def get_all_privacyStatus(cls):
        return cls.query.all()

    @classmethod
    def get_privacyStatus_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_privacyStatus(cls, status):
        privacyStatus = cls(None,status)
        db.session.add(privacyStatus)
        db.session.commit()
    @classmethod
    def update_privacyStatus(cls,id, status):
        privacyStatus=cls.query.filter_by(id=id).first()
        privacyStatus.status=status
        db.session.commit()

    @classmethod
    def delete_privacyStatus(cls,id):
        privacyStatus=cls.query.filter_by(id=id).first()
        db.session.delete(privacyStatus)
        db.session.commit()


@dataclass
class Articles(Base):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    tags = db.relationship("Tags")
    privacyStatus_id = db.Column(db.Integer, db.ForeignKey(
        'privacyStatus.id'), nullable=False)
    comment_status = db.Column(db.Integer)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comments')

    def __init__(self, id, title, text, privacyStatus_id, comment_status, users_id):
        self.id = id
        self.title = title
        self.text = text
        self.privacyStatus_id = privacyStatus_id
        self.comment_status = comment_status
        self.users_id = users_id
   

    @classmethod
    def get_all_articles(cls):
        return cls.query.all()

    @classmethod
    def get_articles_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_articles(cls, title, text, privacyStatus_id, comment_status, users_id):
        articles = cls(None,title, text, privacyStatus_id,
                       comment_status, users_id)
        db.session.add(articles)
        db.session.commit()
    @classmethod
    def update_articles(cls, id, title, text, privacyStatus_id, comment_status, users_id):
        articles=cls.query.filter_by(id=id).first()
        articles.title = title
        articles.text = text
        articles.privacyStatus_id = privacyStatus_id
        articles.comment_status = comment_status
        articles.users_id = users_id
        db.session.commit()
    
    @classmethod
    def delete_articles (cls,id):
        articles=cls.query.filter_by(id=id).first()
        db.session.delete(articles)
        db.session.commit()

@dataclass
class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    articles_id = db.Column(db.Integer, db.ForeignKey('articles.id'),nullable=False)

    def __init__(self, id, title, articles_id):
        self.id = id
        self.title = title
        self.articles_id = articles_id

    @classmethod
    def get_all_tags(cls):
        return cls.query.all()

    @classmethod
    def get_tags_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_tags(cls, title, articles_id):
        tags = cls(None,title, articles_id)
        db.session.add(tags)
        db.session.commit()
    @classmethod
    def update_tags(cls,id,title,articles_id):
        tags=cls.query.filter_by(id=id).first()
        tags.title=title
        tags.articles_id=articles_id
        db.session.commit()

    @classmethod
    def delete_tags(cls,id):
        tags=cls.query.filter_by(id=id).first()
        db.session.delete(tags)
        db.session.commit()


@dataclass
class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    articles_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    comments = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, id, users_id, articles_id, comments):
        self.id = id
        self.users_id = users_id
        self.articles_id = articles_id
        self.comments = comments

    @classmethod
    def get_all_comments(cls):
        return cls.query.all()

    @classmethod
    def get_comments_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_comments(cls, user_id, articles_id, comments):
        comments = cls(None,user_id, articles_id, comments)
        db.session.add(comments)
        db.session.commit()
        
    @classmethod
    def delete_comments(cls,id):
        comments=cls.query.filter_by(id=id).first()
        db.session.delete(comments)
        db.session.commit()
