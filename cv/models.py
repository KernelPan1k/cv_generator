from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Grade(models.Model):
    year = models.IntegerField("Year")
    title = models.CharField("Title", max_length=100)
    sub_title = models.CharField("Sub Title", max_length=100)

    class Meta:
        ordering = ("-year",)


class Experience(models.Model):
    title = models.CharField("Title", max_length=100)
    tasks = RichTextField("Tasks", config_name='full')
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ("position",)


class Technology(models.Model):
    title = models.CharField("Title", max_length=100)
    force = models.IntegerField("force", default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ("position",)


class Preference(models.Model):
    title = models.CharField("Title", max_length=100)
    force = models.IntegerField("force", default=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ("position",)


class CV(models.Model):
    full_name = models.CharField("Full name", max_length=100)
    address = RichTextField("Address", config_name='full')
    contact = RichTextField("Contact", config_name='full')
    information = RichTextField("Information", config_name='full')
    knowledge = RichTextField("Knowledge", config_name='full')
    grades = models.ForeignKey(Grade, on_delete=models.CASCADE)
    experiences = models.ForeignKey(Experience, on_delete=models.CASCADE)
    technologies = models.ForeignKey(Technology, on_delete=models.CASCADE)
    preferences = models.ForeignKey(Preference, on_delete=models.CASCADE)
