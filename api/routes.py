from flask import Blueprint, jsonify
from aplications.utils import get_posts_all

api_bp = Blueprint('api', __name__)

@api_bp.route('/posts')
def get_posts():
    posts = get_posts_all()
    return jsonify(posts)