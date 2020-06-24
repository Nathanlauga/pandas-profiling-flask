from flask import render_template, session, request

from ..utils import check_session_var, get_save_path


def index():
    check_session_var('output_path')
    check_session_var('error')
    check_session_var('fpath')
    check_session_var('input-type')
    return render_template("index.html", session=session)


def sql():
    return render_template("sql.html")