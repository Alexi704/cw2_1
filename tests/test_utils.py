import pytest

from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk


def test_get_posts_all():
    assert get_posts_all()[0]['pk'] == 1, 'Неверный вывод поста'


def test_get_posts_by_user():
    assert get_posts_by_user('leo')[0]['poster_name'] == 'leo', 'Неверное имя'


def test_get_comments_by_post_id():
    assert get_comments_by_post_id(3)[0]['post_id'] == 3, 'Неверный id поста'


def test_search_for_posts():
    assert search_for_posts('Ржавые Елки')[0]['pk'] == 3, 'Неверный поиск'


def test_get_post_by_pk():
    assert get_post_by_pk(3)['pk'] == 3, 'Неверный идентификатор поста'
