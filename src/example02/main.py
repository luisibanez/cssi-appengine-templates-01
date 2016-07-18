import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World!')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1, 21):
          self.response.write('Hello %d <br>' % i)

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/count', CountHandler)
], debug=True)

