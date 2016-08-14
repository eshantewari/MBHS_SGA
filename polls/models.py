import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


#The Class which keeps a record of student records
class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    grade = models.IntegerField() #this will be deleted after PAM
    password = models.CharField(max_length=30, blank=True, null=True) #this will be deleted after PAM
    #This will be a huge-ass string used solely for authentication/record purposes: it will just be a concatenated list of all of the student's votes
    votes = models.TextField(blank = True, null = True)
    class Meta:
        verbose_name_plural = "Students"

class Category(models.Model):
    category_text = models.CharField(max_length = 200)
    category_num = models.IntegerField(default = 0)
    pub_date = models.DateTimeField('date published')
    grade_level = models.IntegerField(default = 0)

    #I used slugs as an alternative for primary keys because:
    #1) primary keys can get nasty and become anachronistic when data is edited
    #2) it's easier to keep track of slugs
    slug = models.CharField(max_length=200)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_num)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

class Candidate(models.Model):
    category = models.ForeignKey(Category)
    candidate_name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='candidate_pics', blank=True, null=True)
    motto = models.CharField(max_length=500, blank = True, null = True)
    votes = models.IntegerField(default = 0)
