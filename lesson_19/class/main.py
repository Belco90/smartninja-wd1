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
        return self.render_template("hello.html")


class ResultHandler(BaseHandler):
    # 2) Añadimos lógica necesaria al POST de este controlador para guardar el mensaje en db
    def post(self):
        result = self.request.get("some_text")

        # aquí creamos un objeto nuevo de la clase Message, con el contenido que ha escrito el usuario
        new_message = Message(content=result)

        # aquí guardamos el mensaje en db
        new_message.put()

        return self.write(result)


# 4) Añadimos la lógica necesaria a nuestro controlador para obtener todos los mensajes desde db y pasarlos a
# la vista
class MessageListHandler(BaseHandler):
    def get(self):

        # aquí obtenemos todos los mensajes de db
        all_messages = Message.query().fetch()

        context = {
            "messages": all_messages,
        }

        return self.render_template("message_list.html", params=context)


# 8) Añadimos la lógica necesaria a nuestro controlador para obtener el mensaje concreto y pasarlo a la vista
class MessageDetailsHandler(BaseHandler):
    def get(self, message_id):

        # tenemos que pasar el message_id a int
        message = Message.get_by_id(int(message_id))

        context = {
            "message_item": message,
        }

        return self.render_template("message_details.html", params=context)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/result', ResultHandler),

    # 3) Añadimos ruta, controlador y template necesarios para la página de listar mensajes
    webapp2.Route('/message-list', MessageListHandler),

    # 7) Añadimos ruta, controlador y template necesarios para la página de detalles de un mensaje,
    # con una url dinámica que coge un número cualquiera (id) y lo pasa a través de message_id
    webapp2.Route('/message-details/<message_id:\d+>', MessageDetailsHandler),
], debug=True)