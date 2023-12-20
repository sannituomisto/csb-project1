from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import RegisterForm
from django.contrib import messages


def signUpView(request):
    if request.method == 'GET':
    # if request.method == 'POST':
        form = RegisterForm(request.GET)
        #form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

# @login_required
def addView(request):
    username = request.user
    task = request.POST.get('content', '').strip()
    if len(task) > 0 and len(task) < 100:
        Task.objects.create(creator=username, content=task)
    else:
        messages.add_message(request, messages.INFO, "Task must be 0-100 characters.")
    return redirect('/')
		
# @login_required
def deleteView(request):
    taskid = request.POST.get('task_id')
    Task.objects.filter(pk=taskid).delete()
    return redirect('/')



# def homeView(request):
#     user=request.user
#     user_tasks=Task.objects.filter(creator=user)
#     return render(request, 'index.html', {"tasks": user_tasks})
@login_required
def homeView(request):
    user=request.user
    userid=user.id
    query = "SELECT * FROM app_task WHERE creator_id = %s" % userid
    user_tasks = Task.objects.raw(query)
    return render(request, 'index.html', {"tasks": user_tasks})


