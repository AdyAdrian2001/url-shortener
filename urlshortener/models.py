from django.db import models
from django.conf import settings
from django.core.validators import URLValidator
from django.utils.encoding import smart_text
from django.utils import timezone
from .utils import shortcode_generator

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class ShortUrl(models.Model):
    url = models.URLField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.shortcode = shortcode_generator()
        super(ShortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.url)

    def __unicode__(self):
        return smart_text(self.url)
