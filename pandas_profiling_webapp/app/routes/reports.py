from flask import render_template, session, request

from ..utils import check_session_var, get_save_path

from os import listdir
from os.path import isfile, join


def reports():
    check_session_var('error')
    path = get_save_path()
    data = request.args

    files = [f for f in listdir(path) if isfile(join(path, f))]

    if 'name' in data:
        if data['name'] in files:
            return render_template("show-report.html", session=session, name=data['name'])

    return render_template("reports.html", session=session, files=files)


def show_report():
    path = get_save_path()
    data = request.args
    files = [f for f in listdir(path) if isfile(join(path, f))]

    if 'name' in data:
        if data['name'] in files:
            return render_template("reports/%s" % data['name'])

    return ""
