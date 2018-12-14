from django.db import models as db

# Create your models here.
class Address(db.Model):
    name = db.CharField(max_length = 100)
    email = db.EmailField(max_length = 100)
    phone = db.CharField(max_length = 100)

    def __str__(self):
        return self.name
