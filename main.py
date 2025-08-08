from flask import Flask
from controller.routes import pages

app = Flask(__name__)
app.register_blueprint(pages)

if __name__ == "__main__":
    app.run(debug=True)

