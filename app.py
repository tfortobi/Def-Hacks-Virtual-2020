from flask import Flask,request, render_template
from flaskext.mysql import MySQL
mysql=MySQL()

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')
def get_data():
	if request.method=='POST':
		state=request.form['state']
		age=request.form['age']
		hoursOut=request.form['hoursOut']
		peopleExposed=request.form['peopleExposed']
		none=request.form['none']
		diabetes=request.form['val']
		asthma=request.form['val']
		chronicLungDisease=request.form['chronicLungDisease']
		hemoglobinDisorders=request.form['hemoglobinDisorders']
		liverDiseases=request.form['liverDisease']
		connection = mysql.get_db()
		cursor = connection.cursor()
		query= "INSERT INTO tbl(State, Age, Hours_Out, People_Exposed) VALUES(%s, %s, %s, %s)"
		cursor.execute(query,(state, age, hoursOut, peopleExposed))
		connection.commit()
		percentage=0
		health = [diabetes, asthma, chronicLungDisease, hemoglobinDisorders, liverDiseases]
def give_data():
	return render_template('response.html', Age = age, Amount_Of_Hours = hoursOut, Amount_Of_People 
	= peopleExposed, Health_Conditions = health.len())		
		
