from db.models.blog_model import Blogs
from db.base import db
from schema.blog_schema import BlogSchema
from api.utils.validation import validate_and_extract_data

class Blog:
    def __init__(self) -> None:
        self.blog_schema = BlogSchema()
        self.schema_for_blog_deletion = BlogSchema(only = ['title'])
        self.schema_for_author_blog_fetch = BlogSchema(only = ['created_by'])
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

    def create_blog(self, blog_data):
        data,error = validate_and_extract_data(schema = self.blog_schema, data = blog_data)
        if not data or error:
            return{'resp_code' : 998,'resp_msg' : error}

        existing_blog = Blogs.query.filter_by(title=data.title).first()
    
        if existing_blog:
            return {'resp_code': 1001, 'resp_msg': 'A blog with this title already exists. Please choose a different title.'}
        
        blog = Blogs(title = data.title, created_by = data.created_by, content = data.content)
        db.session.add(blog)
        db.session.commit()
        return {'resp_code': 2000, 'resp_msg': 'Blog Created Successfully'}
    
    def remove_blog(self, blog_data):
        data,error = validate_and_extract_data(schema = self.schema_for_blog_deletion, data = blog_data)
        if not data or error:
            return{'resp_code' : 998,'resp_msg' : error}

        blog = Blogs.query.filter_by(title = data.title).first()
    
        if not blog:
            return {'resp_code': 1001, 'resp_msg': 'Blog not found. Deletion failed.'}
    
        db.session.delete(blog)
        db.session.commit()
    
        return {'resp_code': 2000, 'resp_msg': 'Blog deleted successfully.'}
    
    def fetch_author_blogs(self, blog_data):
        data,error = validate_and_extract_data(schema = self.schema_for_author_blog_fetch, data = blog_data)
        if not data or error:
            return{'resp_code' : 998,'resp_msg' : error}

        blogs = Blogs.query.filter_by(created_by = data.created_by).all()
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
            return {'resp_code': 1001, 'resp_msg': f'No blogs found by {data.created_by}'}

        return {'resp_code': 2000, 'resp_msg': 'Blogs fetched successfully.', 'data': blog_list}

