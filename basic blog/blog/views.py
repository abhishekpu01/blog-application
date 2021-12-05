from django.shortcuts import render , redirect
from blog.forms import ContactForm ,CreatePostForm 
from blog.models import Contact , Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
#views
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    posts = Post.objects.filter(Type ="public")
    context = {
        'posts':posts
    }
    return render(request , 'blog/index.html' , context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['Name']
            Age = form.cleaned_data['Age']
            email = form.cleaned_data['email']
            Phoneno = form.cleaned_data['Phoneno']
            Query = form.cleaned_data['Query']
            contact = Contact(Name = Name , Age = Age , Email = email , Phoneno = Phoneno , Query = Query)
            contact.save()
            messages.success(request , 'Your Query has been submitted successfully')
            return redirect('home')
        
        else:
            messages.warning(request , form.errors)
            return redirect('contact')

    context = {
        'form':form
    }
    return render(request , 'blog/contact.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method =='POST':
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1==password2:
                if User.objects.filter(email=email).exists():
                    messages.warning(request , 'The Email you entered is already an existing user')
                    if User.object.filter(username = username).exists():
                        messages.warning(request , 'Username you entered is not available')
                    if len(password1)<=8:
                        messages.warning('Enter password more than 8 Characters')
                    return redirect('signup')
                else:
                    user = User(username = username , first_name = first_name , last_name = last_name , email = email)
                    user.set_password(password1)
                    user.save()
                    return redirect('login')
            else:
                messages.WARNING(request , 'Please enter both password same')
                return redirect('signup')
        return render(request , 'blog/signup.html')

def log_it_in(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    else:
        if request.method =="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request , user)
                return redirect('dashboard')
            else:
                messages.warning(request , 'Invalid Credentials')
                return redirect('login')

        return render(request , 'blog/login.html')

def log_Out(request):
    logout(request)
    return redirect('/')


def CreatePost(request):
    if request.user.is_authenticated:
        user = request.user
        form = CreatePostForm()
        if request.method =="POST":
            form = CreatePostForm(request.POST)
            if form.is_valid():
                Title = form.cleaned_data['Title']
                Content = form.cleaned_data['Content']
                Category = form.cleaned_data['Type']
                post = Post(Title = Title , Content = Content , Type = Category , Creator = user)
                post.save()
                messages.success(request , 'Your Post have been saved')
                return redirect('dashboard')
            else:
                messages.warning(request , 'Please enter the fields correctly')
                return redirect('CreatePost')
        context = {
            'form':form
        }
        return render (request , 'blog/postform.html' , context)

    else:
        return redirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        posts = Post.objects.filter(Creator = user)
        context = {
            'posts':posts
        }
        return render(request , 'blog/dashboard.html' , context)

    else:
        return redirect('/')

def Update(request , pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if user.is_authenticated and post.Creator == user:
        form = CreatePostForm(instance = post)
        if request.method =="POST":
            form = CreatePostForm(request.POST , instance = post)
            if form.is_valid():
                form.save()
                messages.success(request , 'Your post with postid ' +str(post.id)+ ' is updated successfully')
                return redirect('dashboard')
        context ={
            'form':form
        }
        return render(request , 'blog/postform.html' , context)

    elif post.Creator is not user and user.is_authenticated:
        return redirect('dashboard')

    else:
        return redirect('/')

def SeePost(request , pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if post.Creator == user and post.Type =="private":
        context={
            'post':post
        }
        return render(request , 'blog/post.html' , context)
    
    elif post.Creator is not user and post.Type == "public":
        context={
            'post':post
        }
        return render(request , 'blog/post.html' , context)
    
    elif post.Creator == user and post.Type =="public":
        context={
            'post':post
        }
        return render(request , 'blog/post.html' , context) 

    else:
        return redirect('/')       

#The below logic is for private posts but some how i manage to merge it in SeePost Function
'''def SeePrivatePost(request , pk):
    user = request.user
    post = Post.object.get(id=pk , Creator=user , Type="private")
    if user.is_authenticated:
        context={
            'post':post
        } 
        return render(request , 'blog/privatepost.html' , context)
    else:
        return redirect('/')'''





