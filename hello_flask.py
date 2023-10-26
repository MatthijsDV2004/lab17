# hello_flask.py
from flask import Flask, render_template
from genderize import Genderize
genderize = Genderize(
    user_agent='GenderizeDocs/0.0',
    api_key='example_api_key',
    timeout=5.0)
lst = Genderize().get(['Matthijs', 'Daniel', 'Angel'])

# create an instance of Flask
app = Flask(__name__)

# route decorator binds a function to a URL
@app.route('/')
def hello():
   return 'Hello world from Flask!'
@app.route('/welcome')
def wc():
   s1 = lst[0]['name'] + str(100*(lst[0]['probability'])) +  "% " + (lst[0]['gender'] + "\n") 
   s2 = lst[1]['name'] + str(100*(lst[1]['probability'])) +  "% "+ (lst[1]['gender'] + "\n") 
   s3 = lst[2]['name'] + str(100*(lst[2]['probability'])) + "% "+ (lst[2]['gender'] + "\n") 
   return s1 + s2 + s3
@app.route('/devries')
def t_test():
    return render_template('my_template_1.html')