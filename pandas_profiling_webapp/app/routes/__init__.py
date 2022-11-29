from flask import current_app as app

__all__ = ["index"]


from .index import index
from .connect_oracle import get_connect_oracle, post_connect_oracle
from .sql import get_sql, post_sql
from .load_file import get_load_file, post_load_file
from .reports import reports, show_report

app.add_url_rule("/", view_func=index, methods=["GET", "POST"])
app.add_url_rule("/sql", view_func=get_sql, methods=["GET"])
app.add_url_rule("/sql", view_func=post_sql, methods=["POST"])
app.add_url_rule("/reports", view_func=reports, methods=["GET"])
app.add_url_rule("/show-report", view_func=show_report, methods=["GET"])
app.add_url_rule("/connect-oracle", view_func=get_connect_oracle, methods=["GET"])
app.add_url_rule("/connect-oracle", view_func=post_connect_oracle, methods=["POST"])
app.add_url_rule("/load-file", view_func=get_load_file, methods=["GET"])
app.add_url_rule("/load-file", view_func=post_load_file, methods=["POST"])
