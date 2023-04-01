from flask import *
import utils
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/', methods=["GET", "POST"]) #decorator drfines the   
def home():  
    if request.method == 'POST':
        print(request.form['text'])

    return render_template('home.html')

@app.route('/history', methods=["GET", "POST"])
def history():
    if request.method == 'POST':
        try:
            date = request.form['date'].split("-")
            y, m, d = date[0], date[1], date[2]
            print(y, m, d, "HIHIHI")
            x = utils.msgread(y, m, d)
        except:
            x = ""
    else:
        x = ""
    try:
        if not x:
            if date:
                x = f"No Entry for {'/'.join(date)}"
            else:
                x = "No Entry"
    except:
        x = "No Entry"
    return render_template('history.html', output=x)

@app.route('/friends')
def friends():
    return render_template('friends.html')
  
if __name__ =='__main__':  
    app.run(port=8000, debug = True)
