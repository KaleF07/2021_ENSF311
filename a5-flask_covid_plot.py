# Author: Kale Fordham

import sqlite3
from flask import Flask, render_template, request
from flask import g # Keeping state: contains database connection
import pandas as pd
from datetime import datetime
from matplotlib.ticker import FormatStrFormatter
import cgi

# Used for plotting to memory and converting to ascii stream
import base64
from io import BytesIO

from matplotlib.figure import Figure
import seaborn as sns

app = Flask(__name__)


DATABASE='data/measurements.db'

# From: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
    
def get_df_from_db(start_date, end_date):
    # without a date range, we select all data
    if start_date is None and end_date is None:
        query = "select * from alberta"
    else: # checking if date range is valid, construct sql query with between
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d' )
        except:
            # default start date is prior to pandemic
            start_date = '2020-01-01'
        try:
            end_date = datetime.strptime(end_date, '%Y-%m-%d' )
        except:
            # default end date is today
            end_date = datetime.today().strftime('%Y-%m-%d' )
        query = f"select * from alberta where date between '{start_date}' and '{end_date}'"
        
    df = pd.read_sql_query(query, con=get_db(), parse_dates=['date'])
    df['total_cases'] = df['daily_cases'].cumsum()
    # min_periods=1 avoids NaN at the start
    df['smooth_daily_cases'] = df['daily_cases'].rolling(7, min_periods=1).mean()

    return df

#From: https://matplotlib.org/devdocs/gallery/user_interfaces/web_application_server_sgskip.html
def get_image_from_fig(fig):
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

# From: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('index.html',
                            title='Home')

@app.route('/daily', methods=['GET', 'POST'])
def daily():
    # if start and end date were entered
    if request.method == 'POST':
        sdate = request.values.get('sdate')
        edate = request.values.get('edate')
    else: # if not, set to None
        sdate = None
        edate = None

    df = get_df_from_db(sdate, edate)

    fig = Figure()
    ax = fig.subplots()

    sns.lineplot(x='date', y='smooth_daily_cases', data=df, ax=ax)
    ax.tick_params(axis="x", which="both", rotation=45)
    ax.grid(b=True)

    fig.tight_layout()

    return render_template('plot.html', 
                            title="Daily", 
                            image_tag=get_image_from_fig(fig))
    
@app.route('/total', methods=['GET', 'POST'])
def total():
    # if start and end date were entered
    if request.method == 'POST':
        sdate = request.values.get('sdate')
        edate = request.values.get('edate')
    else: # if not, set to None
        sdate = None
        edate = None

    df = get_df_from_db(sdate, edate)

    fig = Figure()
    ax = fig.subplots()

    sns.lineplot(x='date', y='total_cases', data=df, ax=ax)
    ax.tick_params(axis="x", which="both", rotation=45)
    ax.grid(b=True)

    fig.tight_layout()

    return render_template('plot.html', 
                            title="Total",
                            image_tag=get_image_from_fig(fig))

@app.route('/loglog', methods=['GET', 'POST'])
def loglog():
    # if start and end date were entered
    if request.method == 'POST':
        sdate = request.values.get('sdate')
        edate = request.values.get('edate')
    else: # if not, set to None
        sdate = None
        edate = None

    df = get_df_from_db(sdate, edate)

    fig = Figure()
    ax = fig.subplots()
    x_str='total_cases'
    y_str='smooth_daily_cases'
    # using log-log and two minor ticks per decade
    ax.loglog(df[x_str], df[y_str], subs=[2, 5])
    # Add a 'dot' to indicate last measurement
    ax.plot(df[x_str].iloc[-1], df[y_str].iloc[-1], 'ko')

    ax.set_xlabel(x_str)
    ax.set_ylabel(y_str)

    ax.xaxis.set_major_formatter(FormatStrFormatter("%.0f"))
    ax.xaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
    ax.yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
    ax.yaxis.set_minor_formatter(FormatStrFormatter("%.0f"))
    ax.tick_params(axis="x", which="both", rotation=45)
    ax.grid(which='both')

    fig.tight_layout()

    return render_template('plot.html',
                            title="Log-Log",
                            image_tag=get_image_from_fig(fig))

if __name__ == '__main__':
    app.debug = True
    app.run()