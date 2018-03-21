from django.shortcuts import render, redirect
from django.contrib import messages
from models import Author, Book, Book_Review
# from apps.login.models import User # Not working
from django.apps import apps
User = apps.get_model('login', 'User')

def isLogin(request):
    if 'loggedin' not in request.session:
        request.session['loggedin'] = {
            'id': -1,
            'name': "undefined"
        }
    # Redirect to the login if the user did not log in yet
    if request.session['loggedin']['id'] != -1:
        return True
    return False

# Display all books
def index(request):
    if not isLogin(request):
        return redirect('/')
        
    books = Book.objects.all()
    # Get the latest 3 from reviews
    reviews = Book_Review.objects.all().order_by('-created_at')[:3]
    context = {
        'books': books,
        'reviews': reviews
    }
    return render(request, 'books/index.html', context)

def add(request):
    if not isLogin(request):
        return redirect('/')

    context = {
        'authors': Author.objects.all()
    }

    return render(request, 'books/add.html', context)

def create(request):
    if not isLogin(request):
        return redirect('/')
    # print request.POST.get('author', "notok"), "<=== author dropdownlist"
    if not request.POST.get('author'):
        print "not ok again"
    
    #Create new author
    if request.POST.get('author_new').strip() != "":
        # Validation for creating new object
        errors = Author.objects.create_validator(request.POST)
        if len(errors) > 0:
            for tag, error in errors.iteritems():
                # messages.error(request, error, extra_tags=tag)
                messages.error(request, error, extra_tags="create")
                return redirect('/books/add')
        else:
            author = Author.objects.create(name=request.POST.get('author_new').strip())

    else:
        if not request.POST.get('author'):
            #When user doesn't input the new author and there is nothing inside the dropdownlist
            return redirect('/books/add')

        author = Author.objects.get(id=request.POST.get('author'))

    #Create book 
    errors = Book.objects.create_validator(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            # messages.error(request, error, extra_tags=tag)
            messages.error(request, error, extra_tags="create")
            return redirect('/books/add')
    book = Book.objects.create(author = author, title = request.POST['title'])
    user = User.objects.get(id=request.session['loggedin']['id'])
    # Create a book review
    breview = Book_Review.objects.create(book = book, user = user, review = request.POST['review'], rating = request.POST['rating'])

    return redirect('/books/{}'.format(book.id))

#Showing the book with its reviews
def show(request, id):
    if not isLogin(request):
        return redirect('/')
    book = Book.objects.get(id=id)
    context = {
        'book': book,
    }
    return render(request, 'books/show.html', context)

# Adding a review to the book
def add_review(request, book_id):
    if not isLogin(request):
        return redirect('/')
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['loggedin']['id'])
    # Create a book review
    breview = Book_Review.objects.create(book = book, user = user, review = request.POST['review'], rating = request.POST['rating'])
    return redirect('/books/{}'.format(book_id))

def delete_review(request, book_id, id):
    if not isLogin(request):
        return redirect('/')
   
    Book_Review.objects.get(id=id).delete()
    return redirect('/books/{}'.format(book_id))
