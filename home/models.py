# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    experience:  = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Subject(models.Model):

    #__Subject_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Subject_FIELDS__END

    class Meta:
        verbose_name        = _("Subject")
        verbose_name_plural = _("Subject")


class Publication(models.Model):

    #__Publication_FIELDS__
    content = models.TextField(max_length=255, null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    executives = models.ForeignKey(Editor, on_delete=models.CASCADE)

    #__Publication_FIELDS__END

    class Meta:
        verbose_name        = _("Publication")
        verbose_name_plural = _("Publication")


class Editor(models.Model):

    #__Editor_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)

    #__Editor_FIELDS__END

    class Meta:
        verbose_name        = _("Editor")
        verbose_name_plural = _("Editor")



#__MODELS__END
