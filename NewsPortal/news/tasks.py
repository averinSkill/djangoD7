from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, Category
import datetime as DT
from datetime import timedelta, date, datetime

# pip install backports.zoneinfo
import zoneinfo


MSC = zoneinfo.ZoneInfo("Europe/Moscow")
datetime(2022, 5, 2, tzinfo=MSC)


def weekly_digest():
    categories = Category.objects.all()
    today = DT.datetime.today()

    week_ago = today - DT.timedelta(days=7)
    week = timedelta(days=7)
    # week_ago = today - DT.timedelta(days=7)
    # week = timedelta(days=7)
    print('today', today)
    print('week_ago', week_ago)
    print('week', week)

    for category in categories:
        subscribers_emails = category.subscribers.all().values('email')
        print('subscribers_emails', subscribers_emails)

        category_subscribers = category.subscribers.all()
        print('category_subscribers', category_subscribers)

        category_subscribers_emails = []
        for subscriber in category_subscribers:
            category_subscribers_emails.append(subscriber.email)

        weekly_posts_in_category = []
        posts_in_category = Post.objects.all().filter(category=f'{category.id}')

        for post in posts_in_category:
            print('today = ', today)
            print('post.d_time = ', post.d_time.utcnow())
            # time_delta = DT.datetime.today - post.d_time
            time_delta = DT.datetime.now() - post.d_time.utcnow()
            print('43 time_delta', time_delta)
            days_delta = today - post.d_time.utcnow()

            print('45 days_delta', days_delta)
            if time_delta < week:
                weekly_posts_in_category.append(post)
                print(f'Дата публикации: {post.d_time}')
                print(f'Дельта: {time_delta}')
                print('----------------   ---------------')

        print(f'ID: {category.id}')
        print(category)
        print(f'Кол-во публикаций: {len(weekly_posts_in_category)}')
        print(category_subscribers_emails)
        print(weekly_posts_in_category)
        print('----------------   ---------------')
        print('----------------   ---------------')
        print('----------------   ---------------')

        if category_subscribers_emails:
            msg = EmailMultiAlternatives(
                subject=f'Weekly digest for subscribed category "{category}" from News Portal.',
                body=f'Привет! Еженедельная подборка публикаций в выбранной категории "{category}"',
                from_email='apractikant@yandex.ru',
                to=category_subscribers_emails,
            )

            # получаем наш html
            html_content = render_to_string(
                'weekly_notify.html',
                {
                    'digest': weekly_posts_in_category,
                    'category': category,
                }
            )

            msg.attach_alternative(html_content, "text/html")  # добавляем html

            msg.send()  # отсылаем
        else:
            continue