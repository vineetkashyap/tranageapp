from django.db import models

# Create your models here.
################################START REGISTRATION MODEL########################################################
class TruckOwnerModel(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    alternate_mobile_number = models.CharField(max_length=50)
    email_id  = models.EmailField(max_length=254,unique=True)
    address  = models.CharField(max_length=50)
    aadhar_number =models.CharField( max_length=50,unique=True)
    pan_number = models.CharField(max_length=50,unique=True)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    aadhar_front = models.FileField(upload_to='media', max_length=100)
    aadhar_back = models.FileField(upload_to='media', max_length=100)
    pan_card_front= models.FileField(upload_to='media', max_length=100)
    cancelled_cheque= models.FileField(upload_to='media', max_length=100)
    photo = models.FileField(upload_to='media', max_length=100)
    sign = models.FileField(upload_to='media', max_length=100)
    register_on = models.DateField(auto_now_add=True)
    register_by = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)



class TransporterModel(models.Model):
    business_name = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    alternarte_number = models.CharField(max_length=500)
    email = models.EmailField(max_length=254,unique=True)
    address = models.CharField(max_length=500)
    gstin = models.CharField(max_length=50,unique=True)
    pan_number = models.CharField(max_length=50,unique=True)
    bank_account_name = models.CharField(max_length=100)
    bank_account_number = models.IntegerField()
    ifsc_code = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=100)
    branch_name = models.CharField(max_length=100)
    gstin_certificate = models.FileField(upload_to='media', max_length=100)
    pan_card_front= models.FileField(upload_to='media', max_length=100)
    cancelled_cheque = models.FileField(upload_to='media', max_length=100)
    registered_on=models.DateTimeField(auto_now_add=True)
    registered_by =models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)

class Tranage_Agent(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number =models.CharField(max_length=50)
    alternate_mobile_number = models.CharField(max_length=50)
    email_id  = models.EmailField(max_length=254,unique=True)
    address  = models.CharField(max_length=50)
    aadhar_number =models.CharField(max_length=50,unique=True)
    pan_number = models.CharField(max_length=50,unique=True)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    aadhar_front = models.FileField(upload_to='media', max_length=100)
    aadhar_back = models.FileField(upload_to='media', max_length=100)
    pan_card_front = models.FileField(upload_to='media', max_length=100)
    cancelled_cheque = models.FileField(upload_to='media', max_length=100)
    photo = models.FileField(upload_to='media', max_length=100)
    sign = models.FileField(upload_to='media', max_length=100)
    registered_on=models.DateTimeField(auto_now_add=True)
    registered_by =models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)


class VehicleRegistraionModel(models.Model):
    vehicle_registration_number = models.CharField(max_length=50)
    vehicle_chassis_no= models.CharField(max_length=50,blank=True)
    owner_name  =models.CharField(max_length=50)
    owner_contact_number = models.CharField(max_length=500)
    vehicle_model_number = models.CharField(max_length=50)
    vehicle_type = models.CharField( max_length=50)
    wheel_type  =models.CharField(max_length=50)
    maximum_load_capacity = models.CharField(max_length=50)
    insurance_name = models.CharField(max_length=100)
    insurance_policy_no = models.CharField(max_length=100)
    insurance_expiry_date = models.CharField(max_length=100)
    preference_product = models.CharField(max_length=50)
    preferred_location = models.CharField(max_length=50)
    vehicle_front_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_back_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_left_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_right_photo= models.FileField( upload_to='media', max_length=100)
    registration_certificate= models.FileField( upload_to='media', max_length=100)
    fitness_certificate = models.FileField( upload_to='media', max_length=100)
    fitness_no = models.FileField(blank=True, upload_to='media', max_length=100)
    pollution_certificate= models.FileField( upload_to='media', max_length=100)
    permit_certificate= models.FileField( upload_to='media', max_length=100)
    insurance_certificate= models.FileField( upload_to='media', max_length=100)
    registered_on=models.DateTimeField(auto_now_add=True)
    registered_by =models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    def __str__(self):
        return self.vehicle_registration_number



class DriverRegistrationModel(models.Model):
    driver_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=50)
    alternate_number = models.CharField(max_length=50)
    home_mobile_number = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    email = models.EmailField( max_length=254,unique=True)
    address = models.CharField(max_length=200)
    aadhar_number = models.CharField(max_length=50,unique=True)
    pan_number = models.CharField( max_length=50,unique=True)
    dl_number = models.CharField(max_length=50,unique=True)
    dl_type = models.CharField( max_length=50)
    dl_expiry_date = models.CharField(max_length=200)
    experience =models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.CharField(max_length=200)
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='media', max_length=100)
    aadhar_front = models.FileField(upload_to='media', max_length=100)
    aadhar_back = models.FileField(upload_to='media', max_length=100)
    pan_front= models.FileField(upload_to='media', max_length=100)
    dl_front = models.FileField(upload_to='media', max_length=100)
    dl_back = models.FileField(upload_to='media', max_length=100)
    passbook_or_cheque = models.FileField(upload_to='media', max_length=100)
    registered_on=models.DateTimeField(auto_now_add=True)
    registered_by =models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)

################################END REGISTRATION MODEL########################################################



###########################################################################################################################



############################################START LODING MODELS########################################

class Trip_model(models.Model):
    vehicle_no = models.CharField(max_length=500)
    driver_name = models.CharField(max_length=500)
    driver_contact_no = models.CharField(max_length=500)
    material_type = models.CharField(max_length=500)
    weight_at_loading = models.CharField(max_length=500)
    weight_at_unloading = models.CharField(max_length=500)
    distance_between_loading_and_unloading = models.CharField(max_length=50)
    trip_material_cost = models.CharField(max_length=50)
    loading_from = models.CharField(max_length=500)
    unloading_at = models.CharField(max_length=500,blank=True)
    advance_fuel = models.CharField(max_length=500)
    advance_amount = models.CharField(max_length=500)
    loading_employee =models.CharField(max_length=500)
    unloading_employee =models.CharField(max_length=500)
    transaction_id = models.CharField(max_length=500)
    transaction_status = models.CharField(max_length=500)
    job_status = models.CharField(max_length=500)
    project_id = models.CharField(max_length=500)
    loading_date = models.CharField(max_length=50)
    unloading_date = models.CharField(max_length=50)
    loading_unit=models.CharField( max_length=50)
    royality =models.FileField( upload_to='media', max_length=100,blank=True)
    challan =models.FileField( upload_to='media', max_length=100,blank=True)
    load_reciept = models.FileField( upload_to='media', max_length=100)
    fuel_reciept = models.FileField( upload_to='media', max_length=100)
    bill=models.FileField( upload_to='media', max_length=100)
    amount_reciept = models.FileField(upload_to='media', max_length=100)
    weight_at_loading_reciept = models.FileField(upload_to='media', max_length=100)
    weight_at_unloading_reciept = models.FileField(upload_to='media', max_length=100)
    
############################################END LODING MODELS##########################################


