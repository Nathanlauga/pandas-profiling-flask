from flask import render_template, session, request, redirect, url_for
import pandas as pd

from ..utils import set_session_var, check_session_var
from ..utils import get_file_extension, retrieve_dataset_from_file
from ..utils import generate_pandas_prof_report


def get_load_file():
    check_session_var('error')
    return render_template("data-sources/load-file.html", session=session)


def post_load_file():
    data = request.form

    if 'input-type' not in data:
        return redirect(url_for("get_load_file"))
    if 'file-path' not in data:
        return redirect(url_for("get_load_file"))

    input_type = data['input-type']
    if input_type != 'file':
        return redirect(url_for("get_load_file"))

    fpath = data['file-path']

    # 1. check extension
    ext = get_file_extension(fpath)
    valid_ext = ['csv', 'xlsx', 'xls']

    if ext not in valid_ext:
        set_session_var('error', "Le fichier n'est pas valide.")
        return redirect(url_for("get_load_file"))

    # 2. load data
    try:
        data = retrieve_dataset_from_file(fpath)
    except Exception as exception:
        set_session_var('error', "Impossible de lire le fichier.")
        return redirect(url_for("get_load_file"))

    # 3. Generate pandas-profiling report
    title = fpath.split('/')[-1].split('.')[-2]
    generate_pandas_prof_report(data, title)

    return redirect(url_for("reports", name=title+'.html'))
