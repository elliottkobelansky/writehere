from flask import *
import utils
import time
  
app = Flask(__name__) #creating the Flask class object   
PROMPT = utils.choose_prompt()
 
@app.route('/', methods=["GET", "POST"]) 
def home():  
    if request.method == 'POST':
        x = request.form['text']
        x = x.replace('\n', ' ')
        utils.msgappend(time.time(), x, PROMPT)

    return render_template('home.html', output=PROMPT)

@app.route('/history', methods=["GET", "POST"])
def history():
    if request.method == 'POST':
        try:
            date = request.form['date'].split("-")
            y, m, d = int(date[0]), int(date[1]), int(date[2])
            x = utils.msgread(y, m, d)
            x = list(x)
            x = x[::-1]
            x = "\n\n".join(x)

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
