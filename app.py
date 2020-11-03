from flask import Flask, request, render_template
from forex import get_current_rate, get_date, create_plot



app = Flask(__name__)
app.config["SECRET_KEY"] = "i<3mydadoqwieh2912497"

@app.route('/')
def render_homepage(): 
    return render_template('base.html')

@app.route('/get-rate')
def get_rate(): 
    result = get_current_rate()
    resultstring = f"{result} kr"
    date = get_date()
    datestring = f"Today's date is: {date}"
    bar = create_plot()
    return render_template('base.html', result = resultstring, today = datestring, plot = bar)