from django.db import models

# Create your models here.

# time to create some models:

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # will keep track of the date and time the record was created
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    # we leave zipcode as charfield since we will not be performing maths on the 
    # field and some countries have letters in the zip codes 
    def __str__(self):
        return('%s %s' % (self.first_name, self.last_name))  
    
# we head over to admin.py to write some python that will help us see the records 
# in the admin panel 