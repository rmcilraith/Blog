from app import blog_app, db

from app.models import User, Post

@blog_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}