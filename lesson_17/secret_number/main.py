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
        return self.render_template("secret_number.html")

    def post(self):
        secret = 17
        correct = False
        guess = int(self.request.get("user_guess"))

        if secret > guess:
            result = "Sorry, but your guess is to low. Try a bit higher."
        elif secret < guess:
            result = "Sorry, but your guess is to high. Try a bit lower."
        else:
            correct = True
            result = "Your answer is correct! The secret number is 22."

        context = {
            "result": result,
            "guess": guess,
            "correct": correct
        }
        return self.render_template("secret_number.html", params=context)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
