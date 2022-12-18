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

class CustomUser(AbstractUser):
    UserTypes=(
        ("1","Mentor"),
        ("2","Mentee")
    )
    user_type=models.CharField(max_length=10,choices=UserTypes)
    class Meta:
        verbose_name="User"

class Mentor(CustomUser):
    name = models.CharField(max_length=200, null=False)
    branch = models.CharField(max_length=10,choices=Branches)
    semester = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(8)])
    phone_number = models.CharField(max_length=10,unique=True)
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

# mentee model

class Mentee(CustomUser):
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
    alloted_mentor_id=models.ForeignKey(Mentor,on_delete=models.CASCADE)
    mentee_rank=models.IntegerField()

    def __str__(self):
        return self.username