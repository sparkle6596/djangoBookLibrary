from django.shortcuts import render
from django.shortcuts import redirect



# Create your views here.
from .forms import AddBookForm ,UpdateBookForm,BookCreateModelForm,SearchForm,RegistrationForm,SignInForm
from  book.models import Books
from django.contrib.auth import authenticate,login,logout



def book_add(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == "GET":
            form = BookCreateModelForm()
            context["form"] = form
            return render(request, "addbook.html", context)
        elif request.method == "POST":
            context = {}
            form = BookCreateModelForm(request.POST)
    
            if form.is_valid():
                form.save()
                # context["form"] = form
                # book_name = form.cleaned_data["book_name"]
                # author= form.cleaned_data["author"]
                # category=form.cleaned_data["category"]
                # prices=form.cleaned_data["price"]
                # copies=form.cleaned_data["number_copies"]
                # print(book_name,author,category,prices,copies)
                # book=Books(book_name=book_name,author=author,category=category,price=prices,copies=copies)
                # book.save()
                return redirect("index")
            else:
                return render(request, "addbook.html",context)
    else:
        return redirect('singn')

def get_books(request):
    if request.user.is_authenticated:
        form=SearchForm()
        context = {}
        books=Books.objects.all()
        context["books"]=books
        context['form']=form
        if request.method=="POST":
            form=SearchForm(request.POST)
            if form.is_valid():
                book_name=form.cleaned_data["book_name"]
                books=Books.objects.filter(book_name__contains=book_name)
                context['books']=books
                return render(request,"book_list.html",context)
            else:
                context['form']=form
                return render(request, "book_list.html", context)
        return render(request, "book_list.html", context)
    else:
        return redirect('singn')

def book_details(request,id):
    if request.user.is_authenticated:
        book=Books.objects.get(id=id)
        context = {}
        context["book"]=book
        return render(request,"book_details.html",context)
    else:
        return redirect('singn')


def remove_book(request,id):
    if request.user.is_authenticated:
        book=Books.objects.get(id=id)
        book.delete()
        return redirect("books")
    else:
        return redirect('singn')
def update_book(request,id):
    if request.user.is_authenticated:
        book = Books.objects.get(id=id)
        form=BookCreateModelForm(instance=book)

        # form=BookCreateModelForm(initial={
        #     "book_name":book.book_name,
        #     "author":book.author,
        #     "category":book.category,
        #     "price":book.price,
        #     "number_copies":book.copies})
        context = {}
        context['form']=form
        if request.method=="POST":
            book = Books.objects.get(id=id)
            form=BookCreateModelForm(instance=book,data=request.POST)
            if form.is_valid():
                form.save()
            # form=BookCreateModelForm(request.POST)
            #
            # if form.is_valid():
            #     book.book_name=form.cleaned_data["book_name"]
            #     book.author=form.cleaned_data["author"]
            #     book.category=form.cleaned_data["category"]
            #     book.price=form.cleaned_data["price"]
            #     book.copies=form.cleaned_data["number_copies"]
            #     book.save()
                return redirect("books")
            else:
                form=BookCreateModelForm(request.POST)
                context["form"]=form
                print(form)
                return render(request, "edit.html", context)
        return render(request,"edit.html",context)
    else:
        return redirect('singn')


def create_account(request):
    form=RegistrationForm()
    context={'form':form}
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("account created")
            return redirect("singn")
        else:
            context["form"]=form
            return render(request, "createaccount.html", context)

    return render(request,"createaccount.html",context)


def singn_in(request):
    form=SignInForm()
    context={'form':form}
    if request.method=="POST":
        form=SignInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("index")
            else:
                context['form']=form
                return render(request, "signin.html", context)


        
    return render(request,"signin.html",context)


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("singn")
    else:
        return redirect('singn')










