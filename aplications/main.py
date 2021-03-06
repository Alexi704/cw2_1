from flask import Flask, render_template, request

from aplications.utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user


app = Flask(__name__)


@app.route('/')
def page_main():
    """ главная страничка """
    posts = get_posts_all()
    count_posts = len(posts)
    return render_template('index.html', posts=posts, count_posts=count_posts)

@app.route('/post/<int:post_id>')
def page_post(post_id):
    """ выводим пост по id поста"""
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    count_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@app.route('/search')
def page_search():
    """ страничка поиска """
    s = request.args.get('s', '')
    search_posts = search_for_posts(s)
    count_search_post = len(search_posts)
    max_out_posts = 10  # задаем максимальное количество выводимых постов на странице поиска
    output_post = search_posts[:max_out_posts]
    return render_template('search.html', output_post=output_post, s=s, count_search_post=count_search_post)


@app.route('/users/<user_name>')
def page_user(user_name):
    """ страничка конкретного пользователя"""
    user_posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', user_posts=user_posts)


if __name__ == '__main__':
    app.run()
