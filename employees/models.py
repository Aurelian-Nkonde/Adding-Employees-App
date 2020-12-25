from django.db import models
from django.urls import reverse

class Employee(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    empl_gender = models.CharField(max_length=1, choices=GENDER, default='N')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=400)  

    class Meta:
        ordering = ['first_name']
    
    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    
