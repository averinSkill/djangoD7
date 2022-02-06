from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        p_rat = self.publication_set.aggregate(post_rating=Sum('rating'))
        post_rat = 0
        post_rat += p_rat.get('post_rating')

        c_rat = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        comment_rat = 0
        comment_rat += c_rat.get('comment_rating')
        self.rating = post_rat * 3 + comment_rat
        self.save()

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    subscribers = models.ManyToManyField(User, related_name='subscriber', blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):

    d_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания новости")
    type_post = models.CharField(
        max_length=3,
        choices=[('NWS', 'новость'), ('ART', 'статья')],
        default='NWS',
        verbose_name="Вид публикации"
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ManyToManyField(
        Category,
        through='PostCategory',
        through_fields=('publication', 'category'),
    )
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    # slug = models.SlugField(max_length=128, unique=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]} ...'

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


class PostCategory(models.Model):
    publication = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.publication} {self.category}'


class Comment(models.Model):
    publication = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True)
    d_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.text}'


