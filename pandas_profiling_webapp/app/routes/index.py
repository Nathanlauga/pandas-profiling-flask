from flask import render_template, session, request

from ..utils import check_session_var, get_save_path


def index():
    check_session_var("error")

    return render_template("index.html", session=session)
