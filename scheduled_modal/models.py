from django.db import models
from ckeditor.fields import RichTextField

class Announcement(models.Model):
    
    begin_date = models.DateField()
    end_date = models.DateField()
    text = RichTextField()

    class Meta:
        ordering = ('begin_date', 'end_date')

