from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CV(models.Model):
    identifier = models.CharField("Identifier", max_length=100)
    full_name = models.CharField("Full name", max_length=100)
    address = RichTextField("Address", config_name='default')
    contact = RichTextField("Contact", config_name='default')
    information = RichTextField("Information", config_name='default')
    knowledge = RichTextField("Knowledge", config_name='default')
    hobby = RichTextField("Hobby", config_name='default', blank=True, null=True, default=None)
    color = ColorField(default='#3e3e3e')

    def get_preference_column_nbr(self):
        total_length = self.preference_set.count()

        if total_length == 2 or total_length == 4:
            return 2

        return total_length


class Grade(models.Model):
    year = models.IntegerField("Year")
    title = models.CharField("Title", max_length=100)
    sub_title = models.CharField("Sub Title", max_length=100)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-year",)


class Experience(models.Model):
    title = models.CharField("Title", max_length=100)
    tasks = RichTextField("Tasks", config_name='default')
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)

    class Meta:
        ordering = ("position",)


class Technology(models.Model):
    title = models.CharField("Title", max_length=100)
    force = models.IntegerField("force", default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)

    class Meta:
        ordering = ("position",)


class Preference(models.Model):
    title = models.CharField("Title", max_length=100)
    force = models.IntegerField("force", default=1, validators=[MaxValueValidator(4), MinValueValidator(1)])
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)

    class Meta:
        ordering = ("position",)
