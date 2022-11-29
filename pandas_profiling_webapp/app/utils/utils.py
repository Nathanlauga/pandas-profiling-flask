from flask import session


def set_session_var(vname, value):
    """ """
    session[vname] = value
    session[vname + "_old"] = True


def check_session_var(vname):
    """ """
    if vname in session:
        if vname + "_old" in session:
            del session[vname + "_old"]
        else:
            del session[vname]
