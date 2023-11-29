from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    front_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    back_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)




Status = (
    ('Parcel Has Been Received And It Is Ready For Shipping!', 'Parcel Has Been Received And It Is Ready For Shipping!'),
    ('On Transit', 'On Transit'),
    ('On Hold', 'On Hold'),
    ('Shipped', 'Shipped'),
    ('Package Arrived (On Clearance)', 'Package Arrived (On Clearance)'),
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Quote(models.Model):
    sender_name = models.CharField(max_length=200,null=False)
    sender_origin = models.CharField(max_length=200,null=False)
    froms = models.CharField(max_length=200,null=False)
    tos = models.CharField(max_length=200,null=False)
    item_description = models.TextField(null=False)
    reciver_name = models.CharField(max_length=200,null=False)
    reciver_email = models.EmailField(max_length=200,null=False)
    reciver_address = models.TextField(null=False)
    reciver_phone = models.CharField(max_length=200,null=False)
    Weight_And_Dimension = models.CharField(max_length=200,null=False)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender_name

class Timeline(models.Model):
    trackingid = models.CharField(max_length=10,null=True,default='')
    Date= models.DateField(null=False)
    Time= models.TimeField(null=False)
    Activity= models.CharField(max_length=200,null=False,choices=Status)
    Location= models.CharField(max_length=400,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.trackingid


class Tracking(models.Model):
    trackingid = models.CharField(max_length=10,null=True, unique=True,default='')
    Estimated_Date_of_Departuer = models.DateField(null=False)
    Estimated_Date_of_Arrival = models.DateField(null=False)
    Sender_Name = models.CharField(max_length=400,null=False)
    Sender_Origin = models.CharField(max_length=200,null=False)
    From = models.CharField(max_length=400,null=False)
    To = models.CharField(max_length=400,null=False)
    Reciver_Name = models.CharField(max_length=400,null=False)
    Reciver_Email = models.EmailField(max_length=400,null=False)
    Reciver_Address = models.TextField(null=False)
    Reciver_Phone = models.CharField(max_length=200,null=False)
    Item_Description = models.CharField(max_length=200,null=False)
    Weight_And_Dimension = models.TextField(blank=True)
    timeline= models.ManyToManyField(Timeline,default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trackingid


