from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__, template_folder='template')


@blog_blueprint.route('/blog')
def blog():
    return render_template('blog/blog.html')

