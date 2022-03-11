from flask import Flask, render_template
from utils import get_posts_all

app = Flask(__name__)

@app.route('/')
def page_main():
    posts = get_posts_all()
    count_posts = len(posts)
    return render_template('index.html', posts=posts, count_posts=count_posts)


if __name__ == '__main__':
    app.run()