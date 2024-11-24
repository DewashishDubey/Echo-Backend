from flask import request, Blueprint
from api.modules.blog.blog import Blog

blog_views = Blueprint('blog_views', __name__)
blog_obj = Blog()

@blog_views.route('/api/v1/fetch-all-blogs', methods=['GET'])
def fetch_all_blogs():
    return blog_obj.fetch_all_blogs()

@blog_views.route('/api/v1/create-blog', methods=['POST'])
def add_blog():
    blog_title = request.args.get('blog_title')
    blog_author = request.args.get('blog_author')
    blog_content = request.args.get('blog_content')
    return blog_obj.create_blog(blog_author = blog_author, blog_title = blog_title, blog_content = blog_content)

@blog_views.route('/api/v1/remove-blog', methods=['DELETE'])
def remove_blog():
    blog_title = request.args.get('blog_title')
    return blog_obj.remove_blog(blog_title = blog_title)

@blog_views.route('/api/v1/fetch-author-blogs', methods=['GET'])
def fetch_author_blogs():
    blog_author = request.args.get('blog_author')
    return blog_obj.fetch_author_blogs(blog_author = blog_author)
