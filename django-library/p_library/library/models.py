from django.db import models


class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
    	return self.full_name


class Redaction(models.Model):
    name = models.TextField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    redaction = models.ForeignKey(Redaction, default=None, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/', null=True)

    def __str__(self):
    	return self.title


class Friend(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    borrowed_books = models.ManyToManyField(Book, related_name='book', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

