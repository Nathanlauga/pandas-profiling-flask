from flask import render_template, session, request, redirect, url_for
import pandas as pd

from ..utils import set_session_var, check_session_var
from ..utils import generate_pandas_prof_report
from ... import app


def get_title_from_query(query):
    """ """
    query = query.upper().split("FROM")
    if len(query) < 2:
        return "Résultat Oracle"

    query = query[1].replace("\t", " ").replace("\n", " ").replace("\r", " ").split(" ")
    query = [e for e in query if e != ""]

    return query[0]


def get_sql():
    check_session_var("error")
    return render_template("data-sources/sql.html", session=session)


def post_sql():
    data = request.form

    if "code" not in data:
        return redirect(url_for("get_sql"))
    if app.con is None:
        set_session_var("error", "La connexion à la BDD n'est pas active")
        return redirect(url_for("get_connect_oracle"))

    query = data["code"]

    # 1. Get data from database
    try:
        data = pd.read_sql(query, con=app.con)
    except Exception as exception:
        set_session_var("error", str(exception))
        return redirect(url_for("get_sql"))

    print("Oracle : data retrieved")

    # 2. Generate pandas-profiling report
    title = get_title_from_query(query)
    generate_pandas_prof_report(data, title)

    return redirect(url_for("reports", name=title + ".html"))
