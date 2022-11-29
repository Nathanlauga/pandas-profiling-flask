from pandas_profiling import ProfileReport
from os.path import dirname, abspath

from .utils import set_session_var

import matplotlib

matplotlib.use("agg")


def get_save_path():
    """ """
    return dirname(dirname(abspath(__file__))) + "/views/reports/"


def generate_pandas_prof_report(df, title):
    """ """
    profile = ProfileReport(df, title=title, explorative=False)

    output_path = get_save_path()
    output_path = output_path + title + ".html"

    profile.to_file(output_path)
