from django.db import models

class BookCategory(models.Model):
    category = models.CharField(max_length=20)
    p_category = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.category

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    book_category = models.ForeignKey(BookCategory)

    def __unicode__(self):
        return self.name

