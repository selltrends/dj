from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    slug = models.SlugField(default="", null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        slug = self.firstname + ' ' + self.lastname
        self.slug = slugify(slug)
        super(Member, self).save(*args, **kwargs)