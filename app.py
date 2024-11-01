from flask import Flask, render_template, request, redirect, url_for, flash
#from flask import Blueprint
import main

app = Flask(__name__)

print(app.app_context())
response = "None"
@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        plot = request.form.get('plot')
        subplots = request.form.get('subplot')
        genre = request.form.get('genre')
        type = request.form.get('length')
        response = main.input(plot=plot, subplots=subplots, genre="is "+genre, type=type)
        return render_template("output.html", output=response)
    else:
        return render_template('index.html')

@app.route('/output', methods = ['GET','POST'])
def output():
    if request.method == 'POST':
        write = request.form.get('print')
        response = request.form.get('output')
        output = main.output(response,write)
        return(render_template("output.html", printed=output))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Error in %s or it doesn\'t exist' % path

if __name__ == "__main__":
    app.run(debug=True)
