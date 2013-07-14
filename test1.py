'''
Created on Jul 8, 2013

@author: lsh
'''

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello/<name>',method=['GET','POST'])
def home():
    if request.method == 'POST':
        return 'hello post %s' % name
    return return render_template('index.html', name=name)

app.run(debug = True,host='0.0.0.0',port=7777)
