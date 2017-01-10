from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import desc


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://sql9152809:D1ZBAljk9n@sql9.freemysqlhosting.net:3306/sql9152809'
app.config['SECRET_KEY'] = "mysecret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Courses(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50))
   description = db.Column(db.String(1000))
   sub = db.Column(db.String(100))
   link = db.Column(db.String(100))
   price = db.Column(db.String(10))
   image = db.Column(db.String(100))
   featured = db.Column(db.String(3))
   category = db.Column(db.String(20))


class Category(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name= db.Column(db.String(20))
   description = db.Column(db.String(400))
   image= db.Column(db.String(400))




def __init__(self, name, description, link,image,featured,category):
   self.name = name
   self.descritopn = description
   self.link = link
   self.image = image
   self.featured = featured
   self.category = category




# FLASK ADMIN
admin = Admin(app, name='coursestash', template_mode='bootstrap3')
admin.add_view(ModelView(Courses, db.session))
admin.add_view(ModelView(Category,db.session))



# Routing


@app.route('/')
def show_all():
    return render_template('index.html', categories = Category.query.all())

@app.route('/listing/<cat>')
def show_list(cat):
    return render_template('listings.html' , courses = Courses.query.filter_by(category = cat).order_by("featured desc"), Heading = cat)

@app.route('/home')
def home():
   return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)
