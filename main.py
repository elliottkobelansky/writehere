from flask import *
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/', methods=["GET", "POST"]) #decorator drfines the   
def home():  
    if request.method == 'POST':
        print(request.form['text'])

    return render_template('home.html')

@app.route('/history', methods=["GET", "POST"])
def history():
    if request.method == 'POST':
        print(request.form['date'])
    return render_template('history.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')
  
if __name__ =='__main__':  
    app.run(port=8000, debug = True)
