from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not isLogin(request):
        return redirect('/')

    return render(request, 'books/index.html')

def add(request):
    if not isLogin(request):
        return redirect('/')

    return render(request, 'books/add.html')

def create(request):
    if not isLogin(request):
        return redirect('/')

    return render(request, 'books/add.html')

def show(request, id):
    if not isLogin(request):
        return redirect('/')
        
    return render(request, 'books/show.html')


def isLogin(request):
    # Redirect to the login if the user did not log in yet
    if request.session['loggedin']['id'] != -1:
        return True
    return False