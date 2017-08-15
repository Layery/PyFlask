#coding='utf-8'
from flask import (
	Flask,
	render_template,
	request
)

def p(data, status=None):
	if (status == 'see'):
		return dir(data)
	else:
		return data
	exit()



app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



'''
user login action
'''
@app.route('/login', methods = ['get', 'post'])
def login():
	print('asdfa')
	if (request.method == 'post'):
		return 'asfa'
		loginAct()
	else:
		return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


''' login method'''
def loginAct():
	pass

if __name__ == '__main__':
    app.run(debug = True)