from django.db import models

# Mentee model


class Mentee(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    team_id = models.BigIntegerField()
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
    solved_q = models.BigIntegerField()
    alloted_mentor_id = models.BigIntegerField()
    rank = models.BigIntegerField()

