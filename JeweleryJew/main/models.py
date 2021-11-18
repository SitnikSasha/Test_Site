from django.db import models

# Create your models here.


class CategoryItem(models.Model):

    name = models.CharField('Категория', max_length=40)
    slug = models.SlugField('URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория изделия'
        verbose_name_plural = 'Категории изделий'


class Item(models.Model):
    article = models.IntegerField('Артикул')
    title = models.CharField('Изделие', max_length=40)
    slug = models.SlugField('URL')
    cat = models.ForeignKey('CategoryItem', on_delete=models.CASCADE)
    price = models.IntegerField('Цена')
    img = models.ImageField('Фото товара 600x400', upload_to='static/image')

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'
