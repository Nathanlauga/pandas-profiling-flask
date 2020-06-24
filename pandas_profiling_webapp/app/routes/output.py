from flask import render_template, session, request, redirect, url_for
import pandas as pd
from pandas_profiling import ProfileReport

from ..utils import check_session_var, set_session_var
from ..utils import retrieve_dataset_from_file


def generate_pandas_prof_report(df, title):
    """
    """
    profile = ProfileReport(df, title=title, explorative=False)
    return profile


def check_output_path(output_path, title=None):
    """
    """
    if len(output_path) > 5:
        if output_path[-5:] == '.html':
            return output_path
    return output_path + title + '.html'


def get_output():
    """
    """
    check_session_var('error')
    return render_template("output.html", session=session)


def post_output():
    """
    """
    data = request.form
    input_type = session['input-type']

    if 'output-path' not in data:
        return redirect(url_for("index"))
    output_path = data['output-path']

    if input_type == 'file':
        fpath = session['fpath']

        try:
            data = retrieve_dataset_from_file(fpath)
        except Exception as exception:
            set_session_var('error', "Le fichier n'est pas valide.")
            return redirect(url_for("get_output"))

        title = fpath.split('/')[-1]

    elif input_type == 'oracle':
        con = session['con']
        query = session['query']
        title = "Oracle"
        data = pd.read_sql(query, con=con)

        return redirect(url_for("get_output"))
    else:
        return redirect(url_for("get_output"))

    profile = generate_pandas_prof_report(data, title)

    title = title.split('.')[-2]
    output_path = check_output_path(output_path, title)

    profile.to_file(output_path)

    output_path = 'http://file:///' + output_path
    set_session_var('output_path', output_path)

    return redirect(url_for("index"))
