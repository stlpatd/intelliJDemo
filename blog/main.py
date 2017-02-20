#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2

import re
from string import letters
import os
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
#class MainPage(BlogHandler):
#    def get(self):
#        self.write('Hello, me!')
        
### blog stuff

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    
    #def render(self):
    #    self.render_text = self.content.replace('\n', '<br>')
    #    return render_str("post.html", p = self)
    
class BlogFront(BlogHandler):
    def get(self):
        posts = db.GqlQuery("select * from Post order by created desc limit 5")
        self.render('front.html', posts = posts)
        
class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        
        if not post:
            self.error(404)
            return
        self.render("permalink.html", post = post)
        
class NewPost(BlogHandler):
    def get(self):
        self.render("newpost.html")
        
    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        
        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)
            
class ViewPostHandler(BlogHandler):
    def get(self, id):
        a= Post.get_by_id(int(id))
        self.render("permalink.html", post = a)
    
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_env.get_template('base.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog/?', BlogFront),
    ('/blog/<id:\d+>', ViewPostHandler),
    ('/blog/([0-9]+)', PostPage),
    ('/blog/newpost', NewPost),
], debug=True)

