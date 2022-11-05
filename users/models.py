from django.db import models

# Mentor model

class Mentor(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    alloted_team_ids = models.BigIntegerField()
    branch = models.CharField(max_length=200)
    semester = models.BigIntegerField()
    phone_number = models.BigIntegerField()
    codechefID = models.TextField()
    codeforcesID = models.TextField()
    leetcodeID = models.TextField()
    gfgID = models.TextField()
    hackerrankID = models.TextField()
    linkedinID = models.TextField()
    score = models.BigIntegerField()
    total_q = models.BigIntegerField()
    
