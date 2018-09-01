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

	<center>
		<div class="receive chat"></div>	
		<div class="send chat"></div>
		<img src="http://loremflickr.com/200/300" />
	</center>

	<bottom>
		<p>It is currently {time}.</p>
	</bottom>

    """.format(time=the_time)

@app.route('/styles.css')
def styles():

    return """
    body{
		background-color:black;
		color:white;
		
	}

    title{
		color: #FEFEFE;
	}
   
	.receive{
		width: 300px;
		height: 400px;
		background-color: white;
		border-raid
	}
	
	.send{
		margin-top: 10px;
		width: 300px;
		height: 100px;
		background-color: white;
	}
    
	.chat{
		border-top: 7px;
		border-left: 7px;
		border-right: 7px;
		border-bottom:7px;
		border-color: green;
	}
    """


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

