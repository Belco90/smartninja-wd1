# coding=utf-8
from google.appengine.ext import ndb


# Así es cómo definíamos un modelo en python
# class Message(object):
#     def __init__(self, content_arg):
#         self.content = content_arg


# 1) Definimos el modelo Message para guardar mensajes
class Message(ndb.Model):
    content = ndb.StringProperty()

    # este campo se añadió más tarde, al principio no estaba y quedó vacío
    created_at = ndb.DateTimeProperty(auto_now_add=True)
