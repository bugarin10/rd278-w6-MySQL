from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create flask instance
app = Flask(__name__)

app.config["SECRET_KEY"] = "123"


# Create a Form Class
class QueryForm(FlaskForm):
    query_by_user = StringField("Write your query", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a URL route in our application for "/"
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/make_query", methods=["GET", "POST"])
def query():
    query_by_user = None
    form = QueryForm()

    if form.validate_on_submit():
        query_by_user = form.query_by_user.data
        form.query_by_user.data = ""

    return render_template("query.html", form=form, query_by_user=query_by_user)
