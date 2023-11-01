from flask import Blueprint

xss_bp = Blueprint('xss', __name__)

from app.xss import routes