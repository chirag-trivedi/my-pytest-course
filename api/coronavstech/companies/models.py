import datetime
from django.db import models
from django.db.models.fields import URLField

# Create your models here.


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        max_length=30, choices=CompanyStatus.choices, default=CompanyStatus.HIRING
    )
    last_update = models.DateTimeField(default=datetime.datetime.now(), editable=True)
    application_link = URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name
