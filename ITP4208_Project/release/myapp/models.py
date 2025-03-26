from django.db import models

# Create your models here.
class ModelAuthor(models.Model):
    username = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.username

class ModelPost(models.Model):
    title   = models.CharField(max_length=120)
    author  = models.ForeignKey(ModelAuthor, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Post from {} created at {}".format(self.author, self.created)

    class Meta:
        pass
    
    def get_absolute_url(self):
        return '/list/'
        