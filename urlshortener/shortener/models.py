import string
import random
from django.db import models


def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"
