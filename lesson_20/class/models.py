# coding=utf-8
from google.appengine.ext import ndb


class Message(ndb.Model):
    content = ndb.StringProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted = ndb.BooleanProperty(default=False)  # flag para saber si está borrado o no
