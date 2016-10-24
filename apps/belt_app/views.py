from django.shortcuts import render,redirect
from .models import User,TravelSchedule
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"belt_app/index.html")
def register(request):
    if request.method == "POST":
        user1={
        'fname':request.POST['name'],
        'username':request.POST['username'],
        'password':request.POST['Password'],
        'cpassword':request.POST['cpassword'],
        }
        user=User.objects.validate(user1)
        if 'error' in user:
            print user['error']
            context={
                'errors':user['error']
            }
            return render(request,"belt_app/index.html",context)
        else:
            context={
            'msg':"you have successfully registered",
            'user':user
            }
        return render(request,"belt_app/index.html",context)
    # else:
    #     return redirect('/')
def login(request):
    if request.method == "POST":

        user=User.objects.login(request.POST)
        # print type(user)
        if 'error' in user:
            print user['error']
            context={
                'errors':user['error']
            }
            return render(request,"belt_app/index.html",context)
        else:

            request.session['name']=user['user'].name
            request.session['userid']=user['user'].id
        return redirect("belt:show")
def show(request):
    context={
    'user':User.objects.get(id=request.session['userid']),
    'trips':TravelSchedule.objects.all()
    }
    return render(request,"belt_app/show.html",context)
# def add(request):
#      return render(request,"belt_app/addtrip.html")
def addtrip(request):
    print request.method
    if request.method== "POST":
        # trip=TravelSchedule.objects.validate_trip(request.POST)
        # if trip:
        user=User.objects.get(id=request.session['userid'])
        print request.POST
        print "*********"
        valid=TravelSchedule.objects.validate_trip(request.POST)
        if valid[0] == False:
            print "false"
            print_messages(request, valid[1])
            return redirect('belt:addtrip')
        else:
            print "true"
            TravelSchedule.objects.create(destination=request.POST['destination'],description=request.POST['description'],traveldate_from=request.POST['datetravel_from'],traveldate_to=request.POST['datetravel_to'],user=user)
            return redirect('belt:show')
    else:
        return render(request,"belt_app/addtrip.html")
def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)
def join(request,id):
    if request.method== "POST":
        this_trip=TravelSchedule.objects.get(id=id)
        this_user=User.objects.get(id=request.session['userid'])
        this_trip.join.add(this_user)
        context={
            'user':this_user,
            'trips':TravelSchedule.objects.all()
                }
        return render(request,"belt_app/show.html",context)
    else:
        return redirect(request,"belt_app/show.html")
def logout(request):
    request.session.clear()
    return redirect('belt:index')
def goback(request):
    return redirect('belt:show')
def destination(request,id):
    context={
    'trips':TravelSchedule.objects.get(id=id),
    }
    return render(request,"belt_app/destination.html",context)
