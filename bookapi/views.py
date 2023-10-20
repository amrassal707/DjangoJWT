from .models import book
from .serializers import bookserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle 
from .throttles import tencallsperminute
# Create your views here.
@api_view(['GET','POST'])
def readBooks(request):
    if request.method == 'GET' :
        bookitems= book.objects.all()
        booktitlefilter= request.query_params.get('title')
        # write the model member variable first in the filter method
        if booktitlefilter:
            bookitems = bookitems.filter(title= booktitlefilter) 
        serializedbooks= bookserializers(bookitems, many= True)
        
        return Response(serializedbooks.data)
        
    
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response('this is a secret message')


@api_view()
@permission_classes([IsAuthenticated])
# here we apply both the authentication using JWT and authoriztion by DRF
def manager_view(request):
    
    if request.user.groups.filter(name= 'Manager').exists():
        return Response('this is for a manager')
    else :
        return Response('you are not a manager')

@api_view()
@throttle_classes([AnonRateThrottle])
#this throttling function is for un-authenticated user, we just apply rate limiting
def throttle(request):
    return Response('successfull')

@api_view()
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
# here we apply both authentication and rate limiting 
def throttleAuth(request):
    return Response("authentication is good")


@api_view()
@throttle_classes([tencallsperminute])
@permission_classes([IsAuthenticated])
# here we apply both authentication and custom rate limiting 
def throttlesfortenminutes(request):
    return Response("authentication is good for 10 minutes")