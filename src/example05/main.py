import jinja2
import os
import webapp2
from datetime import datetime


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {"name": "CSSI NYC"}
        utc_time = datetime.now()
        nyc_hour = utc_time.hour - 4
        template_vars["time"] = nyc_hour
        if nyc_hour < 13:
            template_vars["food"] = "Pizza"
            template_vars["music"] = "Rap"
        else:
            template_vars["food"] = "Steak"
            template_vars["music"] = "Jazz"
        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
