from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Sex(models.TextChoices):
        MALE = 'М', 'Мужской'
        FEMALE = 'Ж', 'Женский'
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True) 
    bio = models.TextField(blank=True)
    sex = models.CharField(max_length=2, choices=Sex.choices, blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.username}'


