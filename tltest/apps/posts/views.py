from django.shortcuts import render
import requests
from .models import Post, User


def index(request):
    posts_list = Post.objects.all().order_by('-id')

    return render(request, 'posts/index.html', {'posts_list': posts_list})


def upload(request):
    # статусы пользователей и постов
    status = {
        'posts': '',
        'users': ''
    }

    # загрузка пользователей
    request_users = requests.get('http://jsonplaceholder.typicode.com/users')
    # добавленные пользователи
    add_users = []
    if (request_users.status_code == 200):
        request_users = request_users.json()
        users_list = User.objects.all()

        i = 0
        for user in request_users:
            # проверка на наличие пользователя в базе
            if user['id'] not in (ul.id for ul in users_list):
                new_user = User(
                    id=user['id'],
                    name=user['name'],
                    username=user['username'],
                    email=user['email'],
                    address=user['address'],
                    phone=user['phone'],
                    website=user['website'],
                    company=user['company']
                )
                new_user.save()
                add_users.append(user)
            i += 1

        status['users'] = 'Загружены новые пользователи: '
    else:
        status['users'] = 'Пользователи не загружены, код: ' + str(request_users.status_code)

    # загрузка постов
    request_posts = requests.get('http://jsonplaceholder.typicode.com/posts')
    # добавленные посты
    add_posts = []
    if (request_posts.status_code == 200):
        request_posts = request_posts.json()
        posts_list = Post.objects.all()

        i = 0
        for post in request_posts:
            # проверка на наличие поста в базе
            if (post['id'] not in (ul.id for ul in posts_list)):
                new_post = Post(
                    id=post['id'],
                    title=post['title'],
                    body=post['body'],
                    user_id=post['userId']
                )
                new_post.save()
                add_posts.append(post)
            i += 1

        status['posts'] = 'Загружены новые посты: '
    else:
        status['posts'] = 'Посты не загружены, код: ' + str(request_posts.status_code)

    return render(request, 'posts/upload.html', {'add_posts': add_posts, 'add_users': add_users, 'status': status})
