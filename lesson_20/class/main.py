#!/usr/bin/env python
# coding=utf-8
import os
import jinja2
import webapp2

from models import Message

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("message_create.html")


class ResultHandler(BaseHandler):
    def post(self):
        result = self.request.get("some_text")

        new_message = Message(content=result)
        new_message.put()

        return self.redirect_to("message-list")


class MessageListHandler(BaseHandler):
    def get(self):

        # Ahora tenemos que filtrar los mensajes para obtener solo aquellos que NO están borrados
        all_messages = Message.query(Message.deleted == False).fetch()

        context = {
            "messages": all_messages,
        }

        return self.render_template("message_list.html", params=context)


class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):

        message = Message.get_by_id(int(message_id))

        context = {
            "message_item": message,
        }

        return self.render_template("message_details.html", params=context)


class MessageEditHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))

        context = {
            "message": message
        }

        return self.render_template("message_edit.html", params=context)

    def post(self, message_id):
        new_content = self.request.get("some_text")

        message = Message.get_by_id(int(message_id))
        message.content = new_content
        message.put()

        context = {
            "message": message,
            "success": True,
        }

        # renderizamos el mismo template pero pasándole success: True para poder pintar el mensaje
        return self.render_template("message_edit.html", params=context)


class MessageDeleteHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))

        context = {
            "message": message
        }

        return self.render_template("message_delete.html", params=context)

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))

        # Esta es la forma en la que borramos un objeto de la db
        # message.key.delete()

        # Esta es la forma en la que marcamos un objeto como borrado de la db sin llegar a borrarlo
        message.deleted = True
        message.put()

        # Hacemos redirect a la lista de mensajes
        return self.redirect_to("message-list")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/message-create', ResultHandler),
    webapp2.Route('/message-list', MessageListHandler, name="message-list"),
    webapp2.Route('/message-details/<message_id:\d+>', MessageDetailsHandler),
    webapp2.Route('/message/<message_id:\d+>/edit', MessageEditHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', MessageDeleteHandler)
], debug=True)