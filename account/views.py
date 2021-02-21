from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm , User
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib import messages
# Create your views here.

 
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {'form':form}
                
        return render(request,'signup.html', context = context)

    else:
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            # try:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
            user.save()
            return redirect('registration')
            # except:
            #     messages.error(request,'User Name is All Ready Exist !! ')
            #     return render(request,'signup.html')  
        # form = UserCreationForm(request.POST)
        # context = {'form':form}
        # if form.is_valid():
        #     user = form.save()
        #     if user is not None:
        #         return redirect('login')
        # else:
        #     return render(request,'signup.html', context = context)



def login(request):
    if request.method != 'POST':
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        # print('form is not valid')
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            print('user name is :', user)
            print(username,password)
            if user is not None:
                loginUser(request, user)
                print('login user ', loginUser)
                return redirect('dashboard')
            else:
                messages.error(request,'Envalid Username or Password !!')
                return render(request,'login.html')    
        else:
            messages.error(request,'Envalid Username or Password !!')
            context = {'form':form}
            return render(request,'login.html', context=context)



def dashboard(request):
    return render(request,'dashboard.html')

def registration(request):
    return render(request,'registration.html')   

def manual(request):
    return render(request,'manual.html')   

def form16(request):
    return render(request,'form16.html')   




def signout(request):
    logout(request)
    return redirect('login')