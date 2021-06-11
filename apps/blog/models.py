from django.db import models
from django.utils.text import slugify 

# Create your models here.
class Article(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=100, unique=True) #6 words
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)


    content = models.TextField() #1,400 - 1,600 words
    meta_description = models.CharField(max_length=120, blank=True) # 120, 158, 168

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.CharField(max_length=255, blank=True, null=True)
    #author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    #tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, self.subtitle)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'blogs/{self.slug}/'