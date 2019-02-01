#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


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


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        a = self.request.get('number-1')
        b = self.request.get('number-2')

        number_a = int(a)
        number_b = int(b)

        result = number_a + number_b

        context = {
            "operation_result": result,
            "number_a": number_a,
            "number_b": number_b,
        }

        return self.render_template("hello.html", params=context)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
