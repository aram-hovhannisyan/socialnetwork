from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='posts', null = True, blank = True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.author}{self.id, self.title}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def get_post_likers(self):
        return self.likes.all()
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return f"{self.user}'s comment on {self.post}"
    

# media content-section