from django.db import models


# Create your models here.
class ClassCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class Class(models.Model):
    class_name = models.ForeignKey(
        ClassCategory, on_delete=models.CASCADE, related_name="classes"
    )
    instructor = models.CharField(max_length=30)
    date = models.DateTimeField()
    slots = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.class_name.name} - {self.instructor} on {self.date.strftime('%Y-%m-%d %H:%M')}"


class Client(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=30)
    c_email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.c_name} ({self.class_name})"
