from django.db import models

# Create your models here.


class regmodel(models.Model):
    companyname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)


# class vaccancyuploadmodel(models.Model):
#     companyname = models.CharField(max_length=30)
#     email = models.EmailField()
#     jobtitle = models.CharField(max_length=30)
#     jobtype = models.CharField(max_length=30)
#     worktype = models.CharField(max_length=30)
#     experiencerequired = models.CharField(max_length=30)
#     qualificationrequired =  models.CharField(max_length=30)



class vaccancyuploadmodel(models.Model):
    catchoice = [
        ('Part time','Part time'),
        ('Full time','Full time'),

    ]
    cho=[
        ('Hybrid','Hybrid'),
        ('Remote','Remote'),
    ]
    choice=[
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10'),
    ]

    companyname = models.CharField(max_length=50)
    email = models.EmailField()
    jobtitle = models.CharField(max_length=35)
    jobtype = models.CharField(max_length=50,choices=catchoice)
    worktype = models.CharField(max_length=30,choices=cho)
    experiencerequired = models.CharField(max_length=20,choices=choice)
    qualificationrequired = models.CharField(max_length=100)





class userdetailsmodel(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    resume = models.FileField(upload_to="samapp/static")
    image = models.FileField(upload_to="samapp/static")
    educationalqualification = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    mobile = models.IntegerField()

    def __str__(self):
        return self.fullname


class jobapplymodel(models.Model):
    companyname = models.CharField(max_length=30)
    jobtitle = models.CharField(max_length=30)
    fullname = models.CharField(max_length=30)
    email =models.EmailField()
    resume = models.FileField(upload_to="samapp/static")


class wishlistmodel(models.Model):
    cid=models.IntegerField()
    companyname = models.CharField(max_length=50)
    email = models.EmailField()
    jobtitle = models.CharField(max_length=35)
    jobtype = models.CharField(max_length=50)
    worktype = models.CharField(max_length=30)
    experiencerequired = models.CharField(max_length=20)
    qualificationrequired = models.CharField(max_length=100)

# <select name="state">
# <option></option>
# <option value="kerala">kerala</option>
# <option value="tamil nadu">tamil nadu</option>
# <option value="karnataka">karnataka</option>
# </select>

class regmodel1(models.Model):
    choice=[
        ('kerala' ,'kerala'), #(database,label(template))
        ('tamil nadu','tamil nadu'),
        ('karnataka','karnataka')

        ]

    name=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=30)
    state=models.CharField(max_length=30,choices=choice) #select
    english=models.BooleanField(default=False)
    malayalam=models.BooleanField(default=False)








