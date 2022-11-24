import pandas as pd


def get_file_extension(fpath):
    """Returns the extension of a given file
    Parameters
    ----------
    fpath: str
        Path of a file
    Returns
    -------
    str:
        extension of the given file
        the text after the last dot
    """
    return str(fpath).split(".")[-1]


def retrieve_dataset_from_file(fpath, nrows=None):
    """ """
    ext = get_file_extension(fpath)

    if ext == "csv":
        return pd.read_csv(fpath, sep=None, engine="python", nrows=nrows)
    elif ext in ["xls", "xlsx"]:
        return pd.read_excel(fpath, nrows=nrows)
    else:
        raise ValueError("L'extension n'est pas valide")


def retrieve_dataset_from_upload(storage):
    """ """
    fpath = storage.filename
    ext = get_file_extension(fpath)

    if ext == "csv":
        return pd.read_csv(storage.stream)
    else:
        raise ValueError("L'extension n'est pas valide")


def check_file_is_readable(fpath):
    """ """
    return retrieve_dataset_from_file(fpath, nrows=5)
