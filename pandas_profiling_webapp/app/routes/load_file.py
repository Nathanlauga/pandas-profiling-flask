from flask import render_template, session, request, redirect, url_for
import pandas as pd

from ..utils import set_session_var, check_session_var
from ..utils import get_file_extension, retrieve_dataset_from_upload
from ..utils import generate_pandas_prof_report


def get_load_file():
    check_session_var("error")
    return render_template("data-sources/load-file.html", session=session)


def post_load_file():
    data = request.files

    if "file-upload" not in data:
        return redirect(url_for("get_load_file"))

    storage = data["file-upload"]

    # 1. check extension
    fpath = storage.filename
    ext = get_file_extension(fpath)
    valid_ext = ["csv", "xlsx", "xls"]

    if ext not in valid_ext:
        set_session_var("error", "Le fichier n'est pas valide.")
        return redirect(url_for("get_load_file"))

    # 2. load the file into a pd.DataFrame
    try:
        data = retrieve_dataset_from_upload(storage)
    except Exception as _:  # most likely will be a TypeError
        set_session_var("error", "Impossible de lire le fichier.")
        return redirect(url_for("get_load_file"))

    # 3. Generate pandas-profiling report
    fpath = fpath.replace("\\", "/")
    title = fpath.split("/")[-1].split(".")[-2]
    generate_pandas_prof_report(data, title)

    return redirect(url_for("reports", name=title + ".html"))
