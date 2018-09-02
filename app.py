from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
	<link rel="stylesheet" type="text/css" href="/styles.css">
	<title>NOMINA18</title>
    <center>
		<h1>NOMINA18</h1>
		<p><b>Welcome to the Qchat</b></p>
		<br>
		<br>

	
		<form>
			<div class="receive chat"></div>	
			<div class="send chat">
			<input type="text" class="form-control" name="message" id="msj" placeholder="especta o participa">
			</div>
			<br>
			<img src="http://loremflickr.com/200/300" />
		</form>
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
		height: 50px;
		background-color: white;
	}
    
	.chat{
		border: 5px solid;
		border-radius: 5px;		
		border-color: #01A9DB;
	}
	
	input{
		border:none;
		height:50;
		width:300px;	
	}
	

	input:focus{
		border-color:#424242;
	}
    """


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

