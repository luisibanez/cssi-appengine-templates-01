import jinja2
import os
import webapp2


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('templates/input_order.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('templates/output_order.html')
        pizza_order = {
          'crust_answer': self.request.get('crust'),
          'size_answer': self.request.get('size'),
          'sauce_answer': self.request.get('sauce'),
          'cheese_answer': self.request.get('cheese'),
          'topings_answer': self.request.get('topings')}
        self.response.write(template.render(pizza_order))


app = webapp2.WSGIApplication([
  ('/', MainHandler),
], debug=True)
