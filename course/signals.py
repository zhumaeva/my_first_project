from typing import Counter
from django.db.models.signals import post_save
from course.models import Student, Group
from django.dispatch import receiver
from datetime import date

@receiver([post_save], sender=Student)
def my_signal(sender, instance, created, **kwargs):
    if created:
        current_date = date.today()
        current_year = current_date.year
        age = current_year - instance.date_of_birth.year 
        print(age)
        instance.age = age
        instance.save()


@receiver([post_save], sender=Group )
def my_signal(sender, instance, created, **kwargs):
    counter = Group.objects.filter(group = instance)
    res_student = counter.count
    print(res_student)
