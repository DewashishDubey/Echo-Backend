from db.models.blog_model import Blogs
from db.base import db

class Blog:
    def __init__(self) -> None:
        pass

    def fetch_all_blogs(self):
    
        blogs = Blogs.query.all()

        blog_list = [
            {
                'id': blog.id,
                'title': blog.title,
                'created_by': blog.created_by,
                'author': blog.created_by,
                'content': blog.content,
                'created_at': blog.created_at  
            }
            for blog in blogs
        ]

        if (len(blog_list) == 0):
            return {'resp_code': 1001, 'resp_msg': 'No blogs found'}

        return {'resp_code': 2000, 'resp_msg': 'Blogs fetched successfully.', 'data': blog_list}

    def create_blog(self, blog_author, blog_title, blog_content):
        existing_blog = Blogs.query.filter_by(title=blog_title).first()
    
        if existing_blog:
            return {'resp_code': 1001, 'resp_msg': 'A blog with this title already exists. Please choose a different title.'}
        
        blog = Blogs(title = blog_title, created_by = blog_author, content = blog_content)
        db.session.add(blog)
        db.session.commit()
        return {'resp_code': 2000, 'resp_msg': 'Blog Created Successfully'}
    
    def remove_blog(self, blog_title):
        
        blog = Blogs.query.filter_by(title = blog_title).first()
    
        if not blog:
            return {'resp_code': 1001, 'resp_msg': 'Blog not found. Deletion failed.'}
    
        db.session.delete(blog)
        db.session.commit()
    
        return {'resp_code': 2000, 'resp_msg': 'Blog deleted successfully.'}
    
    def fetch_author_blogs(self, blog_author):
        blogs = Blogs.query.filter_by(created_by = blog_author).all()
        blog_list = [
            {
                'id': blog.id,
                'title': blog.title,
                'created_by': blog.created_by,
                'author': blog.created_by,
                'content': blog.content,
                'created_at': blog.created_at  
            }
            for blog in blogs
        ]

        if (len(blog_list) == 0):
            return {'resp_code': 1001, 'resp_msg': f'No blogs found by {blog_author}'}

        return {'resp_code': 2000, 'resp_msg': 'Blogs fetched successfully.', 'data': blog_list}

