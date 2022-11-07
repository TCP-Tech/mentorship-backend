from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Mentor model

Semesters = (
    ("1" , "1"),
    ("2" , "2"),
    ("3" , "3"),
    ("4" , "4"),
    ("5" , "5"),
    ("6" , "6"),
    ("7" , "7"),
    ("8" , "8"),
)
Branches = (
    ("1" , "CSE"),
    ("2" , "IT"),
    ("3" , "ECE"),
    ("4" , "ELEC"),
    ("5" , "MECH"),
    ("6" , "CHEM"),
    ("7" , "CIVIL"),
    ("8" , "META"),
    ("9" , "MIN"),
    ("10" , "MCA"),
    ("11" , "BIOMED"),
    ("12" , "BIOTECH"),
    ("13" , "MCA"),
)

class Mentor(AbstractUser):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=200,null=False,unique=True)
    password = models.CharField(max_length=200)
    alloted_team_ids = models.BigIntegerField()
    branch = models.CharField(max_length=100,choices=Branches)
    semester = models.CharField(max_length=100,choices=Semesters)
    phone_number = models.BigIntegerField(unique=True)
    codechefID = models.CharField(max_length=100)
    codeforcesID = models.CharField(max_length=100)
    leetcodeID = models.CharField(max_length=100)
    gfgID = models.CharField(max_length=100)
    hackerrankID = models.CharField(max_length=100)
    linkedinID = models.CharField(max_length=100)
    score = models.BigIntegerField(default=0)
    total_q = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.username