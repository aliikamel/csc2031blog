from flask import Flask, render_template
from main.views import main_blueprint
from blog.views import blog_blueprint
from users.views import users_blueprint
import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

app.register_blueprint(main_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(users_blueprint)


@app.errorhandler(403)
def function_name(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def function_name(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def function_name(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()

