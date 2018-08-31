from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
	<link rel="stylesheet" type="text/css" href="/styles.css">
	<title>NOMINA18</title>
    <center><h1 id="tit">NOMINA18</h1></center>

    <p>Welcome to the Qchat</p>
	<br>
	<br>
    <p>It is currently {time}. hola Isabel</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/styles.css')
def styles():

    return """
    body{
		background-color:black;
		
	}

    title{
		color: grey;
	}	
    """


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

