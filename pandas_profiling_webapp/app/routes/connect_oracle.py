from flask import render_template, session, request, redirect, url_for
import cx_Oracle

from ..utils import set_session_var, check_session_var
from ... import app


def get_connect_oracle():
    check_session_var("error")
    con_exists = app.con is not None

    return render_template(
        "data-sources/connect-oracle.html", session=session, con_exists=con_exists
    )


def post_connect_oracle():
    data = request.form

    valid_keys = ["server", "port", "service", "user", "pwd"]
    conn_dict = dict()

    for key in valid_keys:
        if key not in data:
            return redirect(url_for("index"))
        conn_dict[key] = data[key]

    dsn_str = cx_Oracle.makedsn(
        conn_dict["server"], conn_dict["port"], service_name=conn_dict["service"]
    )

    try:
        con = cx_Oracle.connect(
            user=conn_dict["user"], password=conn_dict["pwd"], dsn=dsn_str
        )
    except Exception as exception:
        set_session_var("error", str(exception))
        return redirect(url_for("get_connect_oracle"))

    print("Connected to Oracle database.")
    app.con = con

    return redirect(url_for("get_sql"))
