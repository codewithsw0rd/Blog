from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
## 1-1 relationship
#1 user can have only 1 profile =>1
#1 profile is associated to only one user => 1
#OneToOneField() => anymodel

## 1 - M realationship
# 1 user can add M Post => 1
# 1 post is associated to only one user =>1
# in django use ForeignKey() =>use in many side models

# M - M relationship
# 1 student can learn from M teachers => M
# 1 teacher can teach M students => M
# ManyToManyField() =>Any PLace