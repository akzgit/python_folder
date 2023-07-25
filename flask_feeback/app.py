from flask import Flask,request,redirect,url_for,render_template #flask - package, Flask -module/class
from flask_mysqldb import MySQL #pip install flask_mysqldb
app =Flask(__name__)    #app is the object , __name__ variable/argument

#configuration of databse
app.config['MYSQL_HOST']='localhost'
# app.config['MYSQLPORT']=3307 #for diffeent port
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='flaskDB'#after creating the database

mysql=MySQL(app)

@app.route('/')
def feedbackform():
    return render_template('feedback.html')

@app.route("/feedback", methods=['POST'])
def home():
    if request.method =='POST':
         uname =request.form['name']
         uemail =request.form['email']
         ufeedback =request.form['feedback']
         #creating a connetion
         cur=mysql.connection.cursor()
         cur.execute('''create dtabase flaskDB''')
        #  cur.execute('''create table feedbackdetailas(name varchar(50),email varchar(50),feedback varchar(1000))''')
        #  cur.execute('''insert into feedbackdetails(name,email,feedback) values(%s,%s)''',(uname,uemail,ufeedback))
         #saving the actions performed
         mysql.connection.commit()
         cur.close()
         return 'Successfully inserted data'
        #  return redirect(url_for('showtime', name=uname, email=uemail,feedback=ufeedback))
    # else:
    #      return render_template('feedback.html')

    
    
# @app.route('/python/<name>/<email>/<feedback>')
# def showtime(name,email,feedback):
#     return 'Hello  %s,\nThank you for your feedback\nYour feedback is: %s\n Your email is:%s\n We will in touch ' %(name,feedback,email)



if __name__ =='__main__':
    app.run(debug = True)