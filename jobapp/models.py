from django.db import models

# Create your models here.


class Jobdesc(models.Model):
    title = models.CharField(max_length=50)
    skills = models.CharField(max_length=100, null=True, blank=True)
    roles_rensponsibilities = models.TextField(
        max_length=255, null=True, blank=True)
    recriter_details = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title
