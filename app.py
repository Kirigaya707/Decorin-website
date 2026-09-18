from flask import Flask

from controllers.main_controller import main_bp


app = Flask(__name__, template_folder="views/templates", static_folder="views/static")
app.register_blueprint(main_bp)


if __name__ == "__main__":
	app.run(debug=True)
