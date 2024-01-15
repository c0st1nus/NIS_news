from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    link = models.URLField(blank=True)
    introduction = models.TextField(blank=True)
    text = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def get_tags(self):
        return [tag.strip() for tag in self.tags.split(',') if tag]

    def set_tags(self, tags):
        self.tags = ','.join(tags)

    def str(self):
        return self.title