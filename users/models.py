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
    codechefID = models.CharField(max_length=100)
    codeforcesID = models.CharField(max_length=100)
    leetcodeID = models.CharField(max_length=100)
    gfgID = models.CharField(max_length=100)
    hackerrankID = models.CharField(max_length=100)
    linkedinID = models.CharField(max_length=100)
    score = models.BigIntegerField()
    total_q = models.BigIntegerField()
    
