from flask import Flask

app = Flask(__name__)

app.route("/")
def home():
  return "IT works"


if __name__ == '__main__":
	app.run()
