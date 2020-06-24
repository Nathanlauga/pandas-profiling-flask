from flask import render_template, session, request, redirect, url_for
import cx_Oracle

from ..utils import set_session_var, check_session_var



def get_connect_oracle():
    check_session_var('error')
    return render_template("data-sources/connect-oracle.html", session=session)


def post_connect_oracle():
    data = request.form

    valid_keys = ['server', 'port', 'service', 'user', 'pwd']
    conn_dict = dict()

    for key in valid_keys:
        if key not in data:
            return redirect(url_for("index"))
        conn_dict[key] = data[key]

    dsn_str = cx_Oracle.makedsn(
        conn_dict['server'], conn_dict['port'], service_name=conn_dict['service'])

    try:
        con = cx_Oracle.connect(
            user=conn_dict['user'], password=conn_dict['pwd'], dsn=dsn_str)
    except Exception as exception:
        set_session_var('error', str(exception))
        return redirect(url_for("get_connect_oracle"))

    set_session_var('con', con)
    set_session_var('input-type', 'oracle')

    return redirect(url_for("sql"))