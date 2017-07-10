from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def pokemon():
    got_name = request.form['name']
    got_email = request.form['email']
    return render_template('index.html', name = got_name, email = got_email)
    # return  redirect('/')
app.run(debug=True)