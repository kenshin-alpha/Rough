from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '192.168.29.40'
app.config['MYSQL_USER'] = 'monty'
app.config['MYSQL_PASSWORD'] = 'AdpT.w20'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)


@app.route("/")
def index():
    
    return render_template("yourwish.html")


@app.route("/viewmessages", methods=["GET"])
def messages():
    cur = mysql.connection.cursor()

    
    result = cur.execute("SELECT * FROM messages")

    articles = cur.fetchall()

    return render_template("viewmessages.html",msgs=articles)


@app.route("/save", methods=["POST"])
def save():

 # Create cursor
        name = request.form['usertxt']
        cur = mysql.connection.cursor()
        print(name)
        # Execute query
        cur.execute("INSERT INTO messages(messages) VALUES(%s)",[name])

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()
        return render_template('yourwish.html')

app.run(debug=True)