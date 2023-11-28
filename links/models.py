from django.db import models
from django.utils.text import slugify
# Create your models here.
# save a shortened link - name, url, slug, number of clicks

class Link(models.Model):
    name = models.CharField(max_length=50, unique=True) # unique används så det inte ska finna dubletter
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) # unique används så det inte ska finna dubletter
    clicks = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} | {self.clicks}"
    
    def click(self):
        # increment by 1
        self.clicks += 1
        # kommer spara ovan increment för den unika linken så det uppdateras i the table
        self.save()
    
    # Om admin inte skrivit in slug så kommer en slug att sparas
    def save(self, *args, **kwargs):
        if not self.slug:
            #förvandlar name till slug
            self.slug = slugify(self.name)
            
        return super().save(*args, **kwargs)
    