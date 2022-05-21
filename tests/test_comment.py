from app.models import Comment,User,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Clemo = User(username = 'Clemo',password = 'mango', email = 'lumumbaclement@gmail.com')
        self.new_blog = Blog(id=1,title_blog='Test',blog_content='This is a Blog test',category="interview",user = self.user_Clemo)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_Clemo,blog=self.new_blog)

    def tearDown(self):
        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Clemo)
        self.assertEquals(self.new_comment.blog,self.new_blog)