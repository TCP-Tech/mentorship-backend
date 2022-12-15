from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Mentee(AbstractUser):
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
    name=models.CharField(max_length=100,null=False)
    # team_id=
    branch=models.CharField(choices=Branches,max_length=10)
    semester = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(8)])
    phone_number = models.CharField(max_length=10,unique=True)
    codechefID = models.URLField(max_length=100)
    codeforcesID = models.URLField(max_length=100)
    leetcodeID = models.URLField(max_length=100)
    gfgID = models.URLField(max_length=100)
    hackerrankID = models.URLField(max_length=100)
    linkedinID = models.URLField(max_length=100)
    score = models.BigIntegerField(default=0)
    solved_q = models.BigIntegerField(default=0)
    # alloted_mentor_id=
    mentee_rank=models.IntegerField()

    def __str__(self):
        return self.username