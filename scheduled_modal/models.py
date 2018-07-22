from django.db import models
from ckeditor.fields import RichTextField

class Announcement(models.Model):
    
    begin_date = models.DateField()
    end_date = models.DateField()
    show_period = models.BooleanField(default=False)
    title =  models.CharField(max_length=200, null=True, blank=True)
    text = RichTextField()

    class Meta:
        ordering = ('begin_date', 'end_date')

