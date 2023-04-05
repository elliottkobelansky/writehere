from flask import *
import utils
import time
from datetime import date

COUNTER = None

app = Flask(__name__) #creating the Flask class object   
@app.route('/', methods=["GET", "POST"]) 
def home():  
    if request.method == "GET":
        dt = date.today()
        y = int(dt.year)
        m = int(dt.month)
        d = int(dt.day)
        try:
            msg, prompt = utils.msgread(y, m, d)
        except:
            msg, prompt = '', None
        if not prompt:
            PROMPT = utils.choose_prompt()
        else:
            PROMPT = prompt
    if request.method == "POST":
        dt = date.today()
        y = int(dt.year)
        m = int(dt.month)
        d = int(dt.day)
        try:
            msg, prompt = utils.msgread(y, m, d)
            print('try1')
        except:
            msg, prompt = '', None
            print('except2')
        if not msg:
            PROMPT = utils.choose_prompt()
            print('notprompt')
        else:
            PROMPT = prompt
        x = request.form['text'] if msg else ''
        msg = x
        x = x.replace('\n', ' ')
        utils.msgappend(time.time(), x, PROMPT)

        return render_template('home.html', output=[msg, PROMPT])
    return render_template('home.html', output=[msg, PROMPT])

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
