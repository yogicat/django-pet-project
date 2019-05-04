from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Pet(models.Model):
    ANIMAL_TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Other', 'Other')
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

    def clean(self):
        if self.is_main:
            active = Pet.objects.filter(is_main=True, owner=self.owner)
            if self.pk:
                active = active.exclude(pk=self.pk)
            if active.exists():
                raise ValidationError(
                    "You already have a main pet.")
