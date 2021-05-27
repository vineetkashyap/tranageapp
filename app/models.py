from django.db import models


class Distributor_Model(models.Model):
    full_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    aadhar_no = models.CharField(max_length=50)
    pan_no = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=500)
    house_no = models.CharField(max_length=500)
    street = models.CharField(max_length=500)
    block = models.CharField(max_length=500)
    distric = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    mobile_no = models.CharField(max_length=500)
    alternate_mobile_no = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    message = models.TextField(max_length=1500)



class Investor_Model(models.Model):
    full_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=50)
    residential_address = models.CharField(max_length=500)
    corresponding_address = models.CharField(max_length=500)
    mobile_no = models.CharField(max_length=500)
    alternate_mobile_no = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    invest_capacity = models.CharField(max_length=500)




