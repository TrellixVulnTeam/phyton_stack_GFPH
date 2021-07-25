from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,Message,Comment

# Create your views here.
def  success(request):
    if "logged_user" not in request.session:
        messages.error(request,"There is not logged user!! Log in first!")
        return redirect('/')
    msgs = Message.objects.all()
    usrs = User.objects.all()
    cmnts = Comment.objects.all()
    logged_user = User.objects.get(id=request.session['logged_user'])
    context = {
        'name' : logged_user.fname,
        'logged_user' : logged_user.id,
        'msgs' : msgs,
        'usrs' : usrs,
        'cmnts' : cmnts
    }
    return render(request,'welcome.html',context)

def newMessage(request):
    if request.method == "POST":
        if "logged_user" not in request.session:
            messages.error(request,"There is not logged user!! Log in first!")
            return redirect('/')
        user_message = User.objects.get(id=request.POST['pk'])
        Message.objects.create(user=user_message,message=request.POST['message'])

    return redirect('/wall/')

def newComment(request):
    if request.method == "POST":
        if "logged_user" not in request.session:
            messages.error(request,"There is not logged user!! Log in first!")
            return redirect('/')
        user_comment = User.objects.get(id=request.POST['loguserid'])
        user_message = Message.objects.get(id=request.POST['msguid'])
        Comment.objects.create(message=user_message,user=user_comment,comment=request.POST['comment'])
    return redirect('/wall/')


def delete(request,pk):
    msg_to_del = Message.objects.get(id =pk)
    msg_to_del.delete()
    return redirect('/wall')