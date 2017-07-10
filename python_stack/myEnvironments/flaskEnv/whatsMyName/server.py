from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("name.html")

@app.route('/process', methods=['POST'])
def create_user():
   print "Got Post Info"
   name = request.form['name']
#    email = request.form['email']
   return redirect('/')

app.run(debug=True)