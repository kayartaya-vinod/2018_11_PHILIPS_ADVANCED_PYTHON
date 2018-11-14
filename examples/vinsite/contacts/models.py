from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=50, default='Bangalore')
    picture = models.CharField(max_length=250)

    def __str__(self):
        return 'Contact [Id={}, Name={}, Email={}, Phone={}, City={}, Picture={}]'.format(
            self.id, self.name, self.email, self.phone, self.city, self.picture)