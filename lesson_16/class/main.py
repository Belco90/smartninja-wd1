#!/usr/bin/env python
import os
from random import randint
from datetime import datetime

import jinja2
import webapp2

# SETTING JINJA
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


# BASE CONTROLLERS FOR MY CONTROLLERS
class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


# CONTROLLERS
class MainHandler(BaseHandler):
    def get(self):
        my_number = randint(1, 100)
        now = datetime.now()

        context = {
            "favourite_number": my_number,
            "current_time": now.strftime("%H:%M")
        }

        return self.render_template("hello.html", params=context)


class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")


# ROUTING
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/blog', BlogHandler),
], debug=True)
