from django.db import models
from django.urls import reverse

class PersonContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.PositiveBigIntegerField()
    email = models.EmailField()
    date_of_birth = models.DateField()

    class Meta:
        ordering = ['first_name']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse("contatcs:contact", kwargs={"pk": self.pk})
    
