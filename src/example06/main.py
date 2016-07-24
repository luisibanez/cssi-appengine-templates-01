import jinja2
import os
import webapp2
from datetime import datetime


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {}
        template_vars["name"] = self.request.get('name')
        template_vars["food"] = self.request.get('food')
        template_vars["music"] = self.request.get('music')
        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
