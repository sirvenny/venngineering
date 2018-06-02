from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from markdownx.models import MarkdownxField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(verbose_name='text', blank=True, null=True)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
