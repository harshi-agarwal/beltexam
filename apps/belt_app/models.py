from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import datetime
# Create your models here.
class UserManager(models.Manager):
    def validate(self,user):
        name_regex = re.compile(r'^[a-zA-Z]+$')
        username_regex = re.compile(r'^[a-zA-Z0-9.+_-]+$')
        if len(user['fname'])<3 and not name_regex.match(user['fname']):
            print "false name"
            return{'error': "Invalid name!"}
        elif not username_regex.match(user['username']):
            print "false username"
            return{'error': "Invalid username Address!"}
        elif len(user['password']) <8:
            print "false password"
            return{'error':"too short password"}
        elif not user['cpassword'] == user['password']:
            # print user['password']
            # print user['cpassword']
            print "false confirm password"
            return {'error':"password and confirm password do not match"}
        else:
            print "true"
            # print user
            pass2=user['password']
            pass3=pass2.encode()
            hashed= bcrypt.hashpw(pass3,bcrypt.gensalt())
            # print hashed
            # pass1= bcrypt.hashpw(pass3,hashed)
            # print pass1
            User.objects.create( name=user['fname'],username=user['username'],Password=hashed)
            return {'user':user}
    def login(self,user):
        print user
        user_log=self.filter(username=user['username'])
        if user_log:
            print user_log
            pass2=user['Password']
            pass3=pass2.encode()
            if bcrypt.hashpw(pass3,user_log[0].Password.encode())== user_log[0].Password:
                print user_log[0].id
                return {'user':user_log[0]}
            # else:
        return{'error':"username or password failed"}
class TravelScheduleManager(models.Manager):
    def validate_trip(self,param):
        errors=[]
        if len(param['destination'])<1:
            errors.append("destination cannot be blank")
        if len(param['description'])<1:
            errors.append("description cannot be empty")
        if len(param['datetravel_from'])<1 and len(param['datetravel_to'])<1:
             errors.append("date cannot be empty")
        if param['datetravel_from'] > str(datetime.date.today()) and param['datetravel_to'] > str(datetime.date.today()):
            errors.append("please enter the future dates")
        if param['datetravel_from'] < param['datetravel_to']:
            errors.append("date travel to cannot be less than date travel from")
        if len(errors)>0:
            return (False,errors)
        else:
            print "True"
            return (True,True)

class User(models.Model):
    name= models.CharField(max_length=30)
    username= models.CharField(max_length=40)
    Password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



    objects=UserManager()

class TravelSchedule(models.Model):
    destination=models.CharField(max_length=40)
    description=models.TextField()
    traveldate_from = models.DateField(null=True)
    traveldate_to = models.DateField(null=True)
    user = models.ForeignKey(User,related_name="myschedule")
    join = models.ManyToManyField(User,related_name="joined_user")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects=TravelScheduleManager()
