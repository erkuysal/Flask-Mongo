from flask import Blueprint

act = Blueprint('action', __name__)

from . import routes