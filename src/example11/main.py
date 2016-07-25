import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        beatles_dict = {
            'John': { 'name': 'John Lennon', 'dob': '10/09/40', 'pob': 'Liverpool'},
            'Paul': { 'name': 'Paul McCartney', 'dob': '06/18/42', 'pob': 'Liverpool'},
            'George': { 'name': 'George Harrison', 'dob': '02/25/43', 'pob': 'Liverpool'},
            'Ringo': { 'name': 'Ringo Starr', 'dob': '07/07/40', 'pob': 'Dingle'}}
        template_vars = {
            'beatles': beatles_dict,
            'showimg': self.request.get('showimg')}
        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
