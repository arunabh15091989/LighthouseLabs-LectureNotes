from flask import Flask,redirect, url_for,render_template,request


app = Flask(__name__)



@app.route('/')
def home():
    return 'Hello Flask!'


@app.route('/about')
def about():
    return ' this is a url shorterner!'


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
