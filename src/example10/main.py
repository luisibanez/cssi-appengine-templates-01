import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'names': ['John', 'Paul', 'George', 'Ringo'],
            'showimg': self.request.get('showimg')}
        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
