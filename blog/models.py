from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import strftime
from slugify import slugify

# Create your models here.

class State(models.Model):
    """модель областей"""
    name = models.CharField(verbose_name='имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

class District(models.Model):
    """модель Постов"""
    name = models.CharField(verbose_name='имя', max_length=100)
    slug = models.SlugField('url', max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='district')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

class SelfMgr(models.Model):
    """модель самоуправлений"""
    name = models.CharField(verbose_name='имя', max_length=100)
    slug = models.SlugField('url', max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='selfManager')
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Самоуправление'
        verbose_name_plural = 'Самоуправления'


class Tag(models.Model):
    """модель ТЭГОВ"""
    name = models.CharField(verbose_name= 'имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    """модель Постов"""
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True,related_name='author')
    title = models.CharField(verbose_name='заголовок', max_length=200, unique=True)
    mini_text = models.TextField(verbose_name='краткий текст')
    text = models.TextField(verbose_name='полный текст')
    image = models.ImageField('Главная фотография', upload_to='media/post/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=False)
    slug = models.SlugField(verbose_name='url', max_length=200)
    tags = models.ManyToManyField(Tag, verbose_name='Тег', blank=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.title, self.mini_text, self.text, self.created_date)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



# from blog.models import Post
# p = Post(title='dfdf',mini_text='fdfdfd',text='fdddddddsfsdsdfsf')


# from blog.models import Post
# from datetime import datetime
# p = Post(title='fdfdfdf', mini_text='fdfdfdfdf', text='fddfgjfgkfjgkfjgkfgjfjgkfg', created_date=datetime.today())
