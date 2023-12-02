# Package imports
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_required
# ...

# Model imports
# ...
from ...models import Post

# Inner imports
from . import main
from .forms import *


@main.route('/')
def home():
    return render_template('main/home.html')


@main.route('/feed')
@login_required
def feed():
    all_posts = Post.objects()
    return render_template('main/feed.html', feed_posts=all_posts)