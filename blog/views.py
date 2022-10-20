from flask import Blueprint, render_template
from app import db
from blog.forms import PostForm
from models import Post
from sqlalchemy import desc

blog_blueprint = Blueprint('blog', __name__, template_folder='template')


@blog_blueprint.route('/blog')
def blog():
    posts = Post.query.order_by(desc('id')).all()
    return render_template('blog/blog.html', posts=posts)


@blog_blueprint.route('/create', methods=('GET', 'POST'))
def create():
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(username=None, title=form.title.data, body=form.body.data)

        db.session.add(new_post)
        db.session.commit()

        return blog()
    return render_template('blog/create.html', form=form)


@blog_blueprint.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        return render_template('500.html')

    form = PostForm()

    if form.validate_on_submit():
        post.update_post(form.title.data, form.body.data)

    form.title.data = post.title
    form.body.data = post.body

    return render_template('blog/blog.html', form=form)


@blog_blueprint.route('/<int:id>/delete')
def delete(id):
    Post.query.filter_by(id=id).delete()
    db.session.commit()

    return blog()
