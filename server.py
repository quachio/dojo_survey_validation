from flask import Flask, render_template, redirect, session, request, flash, get_flashed_messages
import re


app = Flask(__name__)
app.secret_key = "r4bgFu%[jA6)oc[%a)4Ekm6LZtbk]gLtdov{TXsthX?J,3TFJ6rR7mR2yeX3Y7uj"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reset')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/submit', methods=['POST'])
def submit_survey():
    print(request.form)

    if len(request.form['name']) < 1:
        flash('Name is required', 'name')
    else:
        session['name'] = request.form['name']

    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank", 'comment')
    elif len(request.form['comment']) > 120:
        flash("Comment cannot be longer than 120 characters", 'comment')
    else:
        session['comment'] = request.form['comment']

    session['location'] = request.form['location']
    session['language'] = request.form['language']
    

    # Checked if there are any flash mession in session keys _flashes
    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return redirect('/result')

if __name__ == '__main__':
    app.run(debug=True)

