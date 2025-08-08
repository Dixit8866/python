from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/variables')
def variables():
    return render_template('variables/index.html')

@app.route('/variables/example1')
def variables_example1():
    return render_template('variables/example1.html')

@app.route('/variables/example2')
def variables_example2():
    return render_template('variables/example2.html')

@app.route('/datatypes')
def datatypes():
    return render_template('datatypes/index.html')

@app.route('/datatypes/example1')
def datatypes_example1():
    return render_template('datatypes/example1.html')

@app.route('/datatypes/example2')
def datatypes_example2():
    return render_template('datatypes/example2.html')

@app.route('/python-intro')
def python_intro():
    return render_template('python_intro.html')

@app.route('/variables/easy')
def variables_easy():
    return render_template('variables/easy.html')

@app.route('/variables/medium')
def variables_medium():
    return render_template('variables/medium.html')

@app.route('/variables/hard')
def variables_hard():
    return render_template('variables/hard.html')

@app.route('/variables/interview')
def variables_interview():
    return render_template('variables/interview.html')

@app.route('/datatypes/easy')
def datatypes_easy():
    return render_template('datatypes/easy.html')

@app.route('/datatypes/medium')
def datatypes_medium():
    return render_template('datatypes/medium.html')

@app.route('/datatypes/hard')
def datatypes_hard():
    return render_template('datatypes/hard.html')

@app.route('/datatypes/interview')
def datatypes_interview():
    return render_template('datatypes/interview.html')

if __name__ == '__main__':
    app.run(debug=True)
