from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import productlist
from .forms import addproducts
# Create your views here.
def productslist(request):

    data=productlist.objects.all()
    print('data from products table',data)

    content={
        'data':data
    }
    return render(request,'products.html',context=content)         

def addpro(request):
    if request.method == 'POST':
        form = addproducts(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products/')
    else:
        form = addproducts()
    
    return render(request,'addproducts.html',{'form':form})