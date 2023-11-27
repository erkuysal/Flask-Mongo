# Package imports
from flask import render_template, request, redirect, url_for, flash, session, jsonify
# ...

# Model imports
# ...

# Inner imports
from . import main
from .forms import *


@main.route('/')
def home():
    return render_template('home.html')