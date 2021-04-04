#-*- coding: utf-8 -*-

from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.file import FilerFileField


class Announcement(models.Model):
    
    begin_date = models.DateField(verbose_name="date de début")
    end_date = models.DateField(verbose_name="date de fin")
    show_period = models.BooleanField(default=False, verbose_name="période affichée")
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name="titre")
    text = RichTextField(verbose_name="contenu")

    class Meta:
        ordering = ('-begin_date', '-end_date')
        verbose_name = "Annonce (popup)"
        verbose_name_plural = "Annonces (popup)"


class AnnouncementAttachment(models.Model):
    label = models.CharField(max_length=255, verbose_name="intitulé")
    file = FilerFileField(verbose_name="fichier")
    announcement = models.ForeignKey(Announcement, related_name="attachments", on_delete=models.CASCADE)
