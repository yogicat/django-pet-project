from django.conf import settings
from django.db import models
from django.urls import reverse


class Pet(models.Model):
    ANIMAL_TYPE_CHOICES = (
        ('강아지', '강아지'),
        ('고양이', '고양이'),
        ('기타', '기타')
    )

    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    birthday = models.DateField(auto_now_add=False, null=True, blank=True)
    animal = models.CharField(
        max_length=50, blank=True, choices=ANIMAL_TYPE_CHOICES)
    registration_number = models.CharField(max_length=50, blank=True)
    diseases_info = models.CharField(max_length=200, blank=True)
    allergies_info = models.CharField(max_length=200, blank=True)
    preferences = models.CharField(max_length=200, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # new
        return reverse('pet_detail', args=[str(self.id)])
