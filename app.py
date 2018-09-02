from flask import Flask, request
from datetime import datetime
app = Flask(__name__)
messages = []

@app.route('/')
def homepage():
	nick = request.args.get('nick')
	message = request.args.get('message')
	time = datetime.now().strftime("%l:%M %p")
	messages.append({'nick':nick, 'message':message, 'time':time})
	print (messages)
	

	the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
	with open('./static/app.html','r') as f:
		return f.read().format(time=the_time, chat=getPrettyChat(), nick=nick)

@app.route('/styles.css')
def styles():

	with open('./static/app.css','r') as f:
		return f.read()

@app.route('/api/chat/message')
def addMessage():
	nick = request.args.get('nick')
	message = request.args.get('message')
	time = datetime.now().strftime("%l:%M %p")
	messages.append({'nick':nick, 'message':message, 'time':time})
	print (messages)
	
	return "ok" 

def getPrettyChat():
	chat=''
	for message in messages:
		chat += '[%s]  %s dice: %s\n' %(message["time"], message["nick"], message["message"])
	return chat


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

