from flask import Flask, render_template, session, redirect

app = Flask (__name__)
app.secret_key = 'secret2021'

@app.route('/', methods=['GET'])
def index():
    if 'loadnum' in session:
        session['loadnum'] = int(session['loadnum']) + 1
    else:
        session['loadnum'] = 1
    return render_template('index.html')

@app.route('/destroy', methods=['GET'])
def destroy():
    print ("this is being called")
    # session.clear()	
    session.pop('loadnum')
    return redirect('/')

if __name__ == ('__main__'):
    app.run(debug=True)     