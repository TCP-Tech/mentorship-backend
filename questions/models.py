from django.db import models

class Topic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
class Question(models.Model):
    id=models.IntegerField(primary_key=True)
    topic=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    codechefLink=models.CharField(max_length=200)
    codeforcesLink=models.CharField(max_length=200)
    gfgLink=models.CharField(max_length=200)
    leetcodeLink=models.CharField(max_length=200)
    hackerrankLink=models.CharField(max_length=200)
    global_check=models.BooleanField(default=False)
    level=models.CharField(max_length=20)
    mentor_id=models.IntegerField()
    alloted_at=models.DateTimeField()


    