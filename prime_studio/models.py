from django.db import models


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()
    minie_picture = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title


class Navigation(models.Model):
    navigation_title = models.CharField(max_length=250)
    navigation_headline = models.TextField()
    navigation_content = models.TextField()
    navigation_image = models.ImageField(upload_to='navigation/')

    def __str__(self):
        return self.navigation_title


class Painting(models.Model):
    painting_level = models.CharField(max_length=150)
    painting_description = models.TextField()
    painting_example = models.ImageField(upload_to='level/')
    painting_splash = models.ImageField(upload_to='level/')
    categories = models.ForeignKey(Navigation, on_delete=models.CASCADE)

    def __str__(self):
        return self.painting_level


class Terms(models.Model):
    terms_title = models.CharField(max_length=150)
    terms_content = models.TextField()

    def __str__(self):
        return self.terms_title
