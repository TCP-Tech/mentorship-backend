from django.db import models

class Topic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Question(models.Model):
    LEVELS=[
        ('easy','easy'),
        ('medium','medium'),
        ('hard','hard'),
        ]
    topic=models.ForeignKey(Topic,models.CASCADE)
    name=models.CharField(max_length=200)
    codechefLink=models.URLField(max_length=200)
    codeforcesLink=models.URLField(max_length=200)
    gfgLink=models.URLField(max_length=200)
    leetcodeLink=models.URLField(max_length=200)
    hackerrankLink=models.URLField(max_length=200)
    level=models.CharField(choices=LEVELS,max_length=6)
    # mentor_id=models.IntegerField()
    alloted_at=models.DateTimeField()


    