from flask import request, Blueprint
from api.modules.blog.blog import Blog

blog_views = Blueprint('blog_views', __name__)
blog_obj = Blog()

@blog_views.route('/api/v1/fetch-all-blogs', methods=['GET'])
def fetch_all_blogs():
    return blog_obj.fetch_all_blogs()

@blog_views.route('/api/v1/create-blog', methods=['POST'])
def add_blog():
    blog_data = request.get_json()
    return blog_obj.create_blog(blog_data = blog_data)

@blog_views.route('/api/v1/remove-blog', methods=['DELETE'])
def remove_blog():
    blog_data = request.get_json()
    return blog_obj.remove_blog(blog_data = blog_data)

@blog_views.route('/api/v1/fetch-author-blogs', methods=['GET'])
def fetch_author_blogs():
    blog_data = request.get_json()
    return blog_obj.fetch_author_blogs(blog_data = blog_data)
