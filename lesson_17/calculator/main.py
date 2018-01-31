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
        return self.render_template("calculator.html")

    def post(self):
        # get numbers and operation
        first_number = int(self.request.get("first_number"))
        second_number = int(self.request.get("second_number"))
        operation = self.request.get("operation")

        # check operation
        result = None
        if operation == "+":
            result = first_number + second_number

        elif operation == "-":
            result = first_number - second_number

        elif operation == "*":
            result = first_number * second_number

        elif operation == "/":
            result = first_number / second_number

        context = {
            "result": result,
        }
        return self.render_template("calculator.html", params=context)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
