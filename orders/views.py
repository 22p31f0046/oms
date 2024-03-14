from django.shortcuts import render,redirect
from django.http import HttpResponse

from orders.forms import orderhere
from .models import orders_list
# Create your views here.
def orderslist(request):

    data=orders_list.objects.all()
    print('data from products table',data)

    content={
        'data':data
    }
    return render(request,'orders.html',context=content)

def addorders(request):
    if request.method == 'POST':
        form = orderhere(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders/')
    else:
        form = orderhere()

    return render(request, 'addorders.html', {'form': form})