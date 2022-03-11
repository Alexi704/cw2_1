from flask import Flask, render_template, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts

app = Flask(__name__)

@app.route('/')
def page_main():
    posts = get_posts_all()
    count_posts = len(posts)
    return render_template('index.html', posts=posts, count_posts=count_posts)

@app.route('/post/<int:post_id>')
def page_post(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    count_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)

@app.route('/search')
def page_search():
    s = request.args.get('s', '')
    search_posts = search_for_posts(s)
    count_search_post = len(search_posts)
    return render_template('search.html', search_posts=search_posts, s=s, count_search_post=count_search_post)

if __name__ == '__main__':
    app.run()