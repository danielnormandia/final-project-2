# import django
# django.setup()
from django.db import models
from django.utils import timezone

class Fact(models.Model):
    text = models.TextField(db_tablespace='indexes')
    created_date = models.DateTimeField(
            default=timezone.now, db_tablespace='indexes')

    def __str__(self):
        return self.text
