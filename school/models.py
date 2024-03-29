from django.db import models


class SchoolModel(models.Model):
    name = models.CharField(max_length=65, default='')
    address = models.TextField(default='')
    info = models.JSONField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'school'
# Create your models here.
