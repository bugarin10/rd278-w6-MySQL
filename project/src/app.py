import mysql.connector
import credentials


from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


def doing_query(query_by_user):
    try:
        cnx = mysql.connector.connect(
            user="myadmin",
            password=credentials.password,
            host="mysqlserverrd278.mysql.database.azure.com",
            port=3306,
            database="vet_schema",
        )

        cursor = cnx.cursor()

        cursor.execute(query_by_user)

        results = cursor.fetchall()

        columns = cursor.column_names

        n_columns = len(columns)

        # for row in results:
        #    print(row)
        # print(columns)
        cursor.close()
        cnx.close()
        return results, columns, n_columns
    except:
        raise Exception("Something went wrong with the query")


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

    if query_by_user is None:
        results = None
        columns = None
        n_columns = None
    else:
        results, columns, n_columns = doing_query(query_by_user)

    return render_template(
        "query.html",
        form=form,
        query_by_user=query_by_user,
        results=results,
        columns=columns,
        n_columns=n_columns,
    )
