from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Admin
@app.route('/superadmin')
def admin():
    return render_template('admin/admin.html')

@app.route('/updating')
def update():
    return render_template('src/update.html')

@app.route('/exotic/')
def exotic():
    return render_template('src/project/exotic.html')

@app.route('/linear/')
def linear():
    return render_template('src/project/linear.html')

@app.route('/nest/')
def nest():
    return render_template('src/project/nest.html')

@app.route('/steps/')
def steps():
    return render_template('src/project/steps.html')

@app.route('/otto/')
def otto():
    return render_template('src/project/otto.html')

@app.route('/buddaya/')
def buddaya():
    return render_template('src/project/buddaya.html')

if __name__ == "__main__":
    app.run(debug=True)

