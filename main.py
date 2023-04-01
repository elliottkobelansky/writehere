from flask import Flask, render_template, redirect, url_for
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return render_template('home.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/history')
def history():
    return render_template('history.html')
  
if __name__ =='__main__':  
    app.run(port=8000, debug = True)
