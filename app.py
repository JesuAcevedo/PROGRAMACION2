from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/main.html')
def main():
    return render_template('main.html')

@app.route('/charts-chartjs.html')
def charts():
    return render_template('charts-chartjs.html')

@app.route('/components-alerts.html')
def componentes():
    return render_template('components-alerts.html')

@app.route('/forms-elements.html')
def  elements_forms():
    return render_template('forms-elements.html')


@app.route('/tables-general.html')
def  tables_general():
    return render_template('tables-general.html')

@app.route('/users-profile.html')
def  usuarios():
    return render_template('users-profile.html')




