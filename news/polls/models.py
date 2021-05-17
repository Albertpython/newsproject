from django.db import models

class News(models.Model):
    name = models.CharField('News', max_length=50,unique=True)
    slug = models.SlugField('Url', unique=True)
    photo = models.ImageField('Photo', upload_to='News')
    about = models.TextField('About')
    description = models.TextField('Description')
    date = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

class World(models.Model):
    name = models.CharField('World', max_length=50, unique=True)
    slug = models.SlugField('Url', unique=True)
    photo = models.ImageField('Photo', upload_to='News')
    about = models.TextField('About')
    description = models.TextField('Description')
    date = models.DateTimeField('Date', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'World'
        verbose_name_plural = 'Worlds'

