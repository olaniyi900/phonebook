from django.db import models

class PersonContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.PositiveBigIntegerField()
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
