#!/usr/bin/env python
import os
from random import randint

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
        return self.render_template("index.html")


class LotteryHandler(BaseHandler):
    def generate_unique_random_numbers(self, count):
        numbers = []
        while len(numbers) < count:

            new_number = randint(1, 99)

            if new_number not in numbers:
                numbers.append(new_number)

        return numbers

    def get(self):
        random_numbers = self.generate_unique_random_numbers(8)

        context = {
            "lottery_numbers": random_numbers,
        }

        return self.render_template("lottery.html", params=context)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/lottery', LotteryHandler),
], debug=True)
