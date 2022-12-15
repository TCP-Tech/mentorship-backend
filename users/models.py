from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Mentor model

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
    ("10" , "BIOMED"),
    ("11" , "BIOTECH"),
    ("12" , "MCA"),
)

class Mentor(AbstractUser):
    name = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=200,null=False,unique=True)
    password = models.CharField(max_length=200)
    branch = models.CharField(max_length=8,choices=Branches)
    semester = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(8)])
    phone_number = models.BigIntegerField(unique=True)
    codechefID = models.URLField(max_length=100)
    codeforcesID = models.URLField(max_length=100)
    leetcodeID = models.URLField(max_length=100)
    gfgID = models.URLField(max_length=100)
    hackerrankID = models.URLField(max_length=100)
    linkedinID = models.URLField(max_length=100)
    score = models.BigIntegerField(default=0)
    total_q = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.username