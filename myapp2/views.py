from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from.models import Books
from .forms import BookForm

def mainweb(request,id):
    mybook = Books.objects.get(id=id)
    template=loader.get_template('mainweb.html')
    context= {
        'mybook':mybook
    }

    return HttpResponse(template.render(context,request))

def owner(request):
    mybook = Books.objects.all().values()
    context ={
        'mybook':mybook
    }
    template=loader.get_template('owner.html')
    return HttpResponse(template.render(context,request))

@csrf_exempt
def add_newbook(request):
    if request.method=='POST':
        Bookname = request.POST.get('Bookname',)
        image = request.FILES['image']
        Authorname = request.POST.get('Authorname',)
        Price = request.POST.get('Price',)
        Ratings = request.POST.get('Ratings',)
        Description = request.POST.get('Description',)
        book= Books(Bookname=Bookname,image=image,Authorname=Authorname,Price=Price,Ratings=Ratings,Description=Description)
        book.save()
    template=loader.get_template('add_newbook.html')
    return HttpResponse(template.render())

def update(request,id):
    book=Books.objects.get(id=id)
    form = BookForm(request.POST,instance=book)
    if form.is_valid():
        form.save()
        template = loader.get_template('add_newbook.html')
        return HttpResponse(template.render())
    return render(request,'update.html',{'form':form,'book':book})

def buy(request):
    items = ['Harry Potter', 'Hunger Games', 'Twilight', 'To Kill A Mockingbird','The Falut in our Stars']
    template = loader.get_template('mainweb.html')
    return render(request, 'owner.html', {'items': items})

    

def hello(request):
    template=loader.get_template('hello.html')
    return HttpResponse(template.render())

# Create your views here.
