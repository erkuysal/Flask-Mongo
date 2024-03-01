# Package imports
from flask import render_template, request, redirect, url_for, flash, send_file, abort
from flask_login import login_required, current_user
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename
import uuid
import sys
import os

# Relative imports
from . import act
from .forms import *

from ...models import Post, File


# ------------------------------ Posts Section --------------------------------------
@act.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data, author=current_user)
        new_post.save()
        flash('Post created successfully!', 'SUCCESS')
        return redirect(url_for('main.feed'))
    return render_template('actions/action.html', form=form)


# @auth.route('/delete_post/<post_id>', methods=['GET', 'POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.objects(id=post_id).first()
#
#     # Ensure the user deleting the post is the author
#     if post and post.author == current_user:
#         post.delete()
#         return redirect(url_for('feed'))
#
#     # Handle cases where the post does not exist or the user is not the author
#     flash('Unable to delete the post.', 'danger')
#     return redirect(url_for('feed'))


# ------------------------------ End Posts Section / Begin Upload Section --------------------------------------

@act.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        user = current_user

        file = form.file.data

        filename = secure_filename(file.filename)

        new_file = File(filename=filename, data=file, author=user)
        new_file.save()

        flash('File uploaded successfully', 'SUCCESS')
        return redirect(url_for('main.feed'))

    return render_template('actions/upload.html', form=form)


# ------------------------------ End Upload Section --------------------------------------

# form = UploadForm()
# if request.method == 'POST':
#     uploaded_file = form.file.data
#     if uploaded_file.filename != '':
#         uploaded_file.save(uploaded_file.filename)
#         flash('File uploaded successfully!', 'SUCCESS')
#     return redirect(url_for('main.feed'))
# return render_template('actions/upload.html', form=form)