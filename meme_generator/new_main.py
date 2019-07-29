import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def getImageUrl(image_type):
    image_type_to_url_dict = {
    "alpaca" : "https://www.publicdomainpictures.net/pictures/90000/velka/alpaca-chewing.jpg",
    "pikachu" : "https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png",
    "gorilla" : "https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
    }
    return image_type_to_url_dict[image_type]

def getImageUrl2(image_type):
    image_type_to_url_dict = {
    "alpaca" : "https://www.publicdomainpictures.net/pictures/90000/velka/alpaca-chewing.jpg",
    "pikachu" : "https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png",
    "gorilla" : "https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
    }
    if image_type == "alpaca":
        return "https://www.publicdomainpictures.net/pictures/90000/velka/alpaca-chewing.jpg"
    elif image_type == "pikachu":
        return "https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png"
    elif image_type == "gorilla":
        return "https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('welcome.html')
        self.response.write(template.render())

    def post(self):
        self.response.write("You made a post request to the MainPage handler!")

class MemePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('results.html')
        my_variable_dict = {
        "title_color": "red",
        "line1": "",
        "line2": "Me: Gets a bad grade on a test",
        "line3": "Me:",
        "meme_img_url": "https://www.publicdomainpictures.net/pictures/90000/velka/alpaca-chewing.jpg"
        }
        self.response.write(template.render(my_variable_dict))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('results.html')
        title_color = self.request.get("title_line")
        first_line = self.request.get('first')
        second_line = self.request.get('second')
        third_line = self.request.get('third')
        meme_picture = self.request.get("meme_picture")

        my_variable_dict = {
        "title_color": title_color,
        "line1": first_line,
        "line2": second_line,
        "line3": third_line,
        "meme_img_url": getImageUrl(meme_picture)
        }
        self.response.write(template.render(my_variable_dict))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/meme', MemePage),
], debug=True)
