cd pandas_profiling_webapp

export FLASK_APP=run.py
export FLASK_DEBUG=true  # DO NOT use true in production!!
export FLASK_PORT=${1:-5000}  # defaults to 5000
flask run -p $FLASK_PORT