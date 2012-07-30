from django.db import models

# Create your models here.
class ms_primary_schools(models.Model):
    name_of_school = models.CharField(max_length=200)
    level_of_education = models.CharField(max_length=200)
    sponsor_of_school = models.CharField(max_length=200)
    genderbase_of_school = models.CharField(max_length=200)
    boardnature_of_school = models.CharField(max_length=200)
    capacityneeds_of_school = models.CharField(max_length=200) #whether boarding or day
    pupil_teacher_ratio = models.CharField(max_length=200)
    pupil_classroom_ration = models.CharField(max_length=200)
    pupil_toilet_ration = models.CharField(max_length=200)
    total_no_classrooms = models.CharField(max_length=200)
    boys_toilet = models.CharField(max_length=200)
    girls_toilets = models.CharField(max_length=200)
    teachers_toilets = models.CharField(max_length=200)
    total_toilets = models.CharField(max_length=200)
    total_boys = models.CharField(max_length=200)
    total_girls = models.CharField(max_length=200)
    total_enrolment = models.CharField(max_length=200)
    gok_tsc_male = models.CharField(max_length=200)
    gok_tsc_female = models.CharField(max_length=200)
    local_authority_male = models.CharField(max_length=200)
    local_authority_female = models.CharField(max_length=200)
    pta_bog_male = models.CharField(max_length=200)
    pta_bog_female = models.CharField(max_length=200)
    others_male = models.CharField(max_length=200)
    others_female = models.CharField(max_length=200)
    none_teachingstuff_male = models.CharField(max_length=200)
    none_teachingstuff_female = models.CharField(max_length=200)
    pr_province = models.CharField(max_length=200)
    pr_district = models.CharField(max_length=200)
    pr_division = models.CharField(max_length=200)
    pr_location = models.CharField(max_length=200)
    pr_constituency = models.CharField(max_length=200)
    pr_geolocation = models.CharField(max_length=200)
    pr_location = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class ms_secondary_schools(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    
    
class ms_university_schools(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')