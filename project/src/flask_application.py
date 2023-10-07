from flask import Flask, render_template

# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired


# Create flask instance
app = Flask(__name__)

# app.config["SECRET_KEY"] = "123"


# Create a Form Class
# class NamerForm(FlaskForm):
#    name = StringField("Write your query", validators=[DataRequired()])
#    submit = SubmitField("Submit")


# Create a URL route in our application for "/"
@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/make_query")
# def query():
#    return render_template("query.html")
