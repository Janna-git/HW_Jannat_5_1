from django.db import models


class Tweet(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.author} - {self.title}"


class Comment(models.Model):
    text = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} - {self.tweet}'


class Mark(models.Model):
    mark_value = models.CharField(max_length=20, choices=[
        (1, 'like'),
        (2, 'dislike')
    ])
    tweet = models.OneToOneField(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mark_value} - {self.tweet}'
