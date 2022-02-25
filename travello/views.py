from accounts.views import login
from django.shortcuts import render
from django.contrib.auth import authenticate
from . models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.desc = "The City Never Sleeps"
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer= False

    # dest2 = Destination()
    # dest2.name = 'Bangalore'
    # dest2.desc = 'The Green city '
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 500
    # dest2.offer=True

    # dest3 = Destination()
    # dest3.name = 'Delhi'
    # dest3.desc = 'The Capital city '
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 1000
    # dest3.offer=False
    # dests= [dest1, dest2, dest3]

    return render( request, 'index.html', {'dests': dests})


def destination(request, id):
    user = request.user
    dest=Destination.objects.get(id=id)
    #print(dest.name, dest.price, dest.desc)
    context={
        'dest' : dest

    }
    if user.is_authenticated:
        return render(request, 'destination.html', context )
    else:
        print("Please Login to View Details")
        return render(request,'login.html')    


    
    