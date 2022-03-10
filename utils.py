import json
from config import PATH_POSTS, PATH_COMMENTS
from pprint import pprint as pp


def get_posts_all():
    """ возвращает все посты """
    with open(PATH_POSTS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):
    """ возвращает посты определенного пользователя """
    posts = get_posts_all()
    list_posts_by_name = []
    for post in posts:
        poster_name = post['poster_name'].lower()
        if poster_name == user_name.lower():
            list_posts_by_name.append(post)
    return list_posts_by_name


def get_comments_by_post_id(post_id):
    """ возвращает комментарии определенного поста """
    with open(PATH_COMMENTS, 'r', encoding='utf-8') as file:
        comments = json.load(file)
    list_comments_by_id_post = []
    for comment in comments:
        if comment['post_id'] == post_id:
            list_comments_by_id_post.append(comment)
    return list_comments_by_id_post


def search_for_posts(query):
    """возвращает список словарей по вхождению query"""
    posts = get_posts_all()
    list_posts_by_search = []
    for post in posts:
        post_content = post['content'].lower()
        if query.lower() in post_content:
            list_posts_by_search.append(post)
    return list_posts_by_search


def get_post_by_pk(pk):
    """ возвращает один пост по его идентификатору """
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post

if __name__ == '__main__':
    # pp(get_posts_all()[1]['poster_name']) # тестируем
    # pp(get_posts_all()) # тестируем
    # pp(get_posts_by_user('Johnny')) # тестируем
    # pp(get_comments_by_post_id(3)) # тестируем
    # pp(search_for_posts('Ржавые Елки')) # тестируем
    pp(get_post_by_pk(3)) # тестируем
    pp(PATH_POSTS)
    pp(PATH_COMMENTS)
