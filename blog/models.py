from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title