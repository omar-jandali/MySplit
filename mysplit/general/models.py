from django.db import models
from django.contrib.auth.models import User, UserManager

# the following is the users profile model
class Profile(models.Model):
    # users basic info
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=25, default='first')
    l_name = models.CharField(max_length=25, default='last')
    bio = models.CharField(max_length=220, default='bio')
    # users location
    street = models.CharField(max_length=200, default='street address')
    city = models.CharField(max_length=100, default='city')
    state = models.CharField(max_length=22, default='CA')
    zip_code = models.IntegerField(default=12345)
    # users other profile info
    phone = models.IntegerField(default="000-ooo-oooo")
    dob = models.DateField(default='1950-01-01')
    gender = models.CharField(max_length=5, default='Other')
    # lob = industry/occupation
    lob = models.CharField(max_length=40, default='occupation')
    # dba = Company Name
    dba = models.CharField(max_length=40, default='comapny')
    account_type = models.CharField(max_length=20, default='INDIVIDUAL')
    synapse_id = models.CharField(max_length=200, default='123456789')
    created = models.DateTimeField(auto_now_add=True)

# the following is the model for sending friend requests
class Request(models.Model):
    # user = person who sent the request
    user = models.CharField(max_length=22, default='current_user')
    # requested = person who received the request
    requested = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

# the following are models for accepted friend requests
class Friend(models.Model):
    # user = person who accepted the request
    user = models.CharField(max_length=22, default='current_user')
    # freind = person who sent the original request
    friend = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)

# all of the current users activity
class UserActivity(models.Model):
    # users reference/id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # types of activity
    account = models.CharField(max_length=150, null=True)
    # expense = models.ForeignKey(Expense, null=True, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, null=True, on_delete=models.CASCADE)
    # the activity description
    description = models.CharField(max_length=200, default='some action')
    # sets reference if it is required/provided
    reference = models.IntegerField(default = '101', null = True)
    # type of activity
    category = models.IntegerField(default=1)
    # seen or not seen
    status = models.SmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

# Privacy sotres every users different privacy settings for viewing profiles
class Privacy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 1 = everyone
    # 2 = friends
    # 3 = me
    groups = models.SmallIntegerField(default=1)
    friends = models.SmallIntegerField(default=1)
    expenses = models.SmallIntegerField(default=1)
    searchable = models.SmallIntegerField(default=1)
