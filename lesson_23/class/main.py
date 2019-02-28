#!/usr/bin/env python
# coding=utf-8
import os
import json
import jinja2
import webapp2
from google.appengine.api import urlfetch


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
        data_json = open("people.json", "r").read()

        # aquí parseamos json a python
        people_list = json.loads(data_json)

        context = {
            "people": people_list,
        }

        return self.render_template("hello.html", params=context)


class WeatherHandler(BaseHandler):
    def get(self):
        unit_choice = self.request.get("temperature-unit")

        url = 'http://api.openweathermap.org/data/2.5/weather?q=Malaga&units={}&appid=db8b1ce1eaccb7d82980f5c1144e2eec'.format(unit_choice)

        response = urlfetch.fetch(url)

        weather_info = json.loads(response.content)

        context = {
            "weather_info": weather_info,
            "unit_choice": unit_choice,
        }

        return self.render_template("weather.html", params=context)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/weather', WeatherHandler),
], debug=True)
