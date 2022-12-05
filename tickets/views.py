from django.shortcuts import render
from django.http.response import JsonResponse,Response
from .models import Guest,Movie,Reservation
from .serializers import ReservationSerializer,MovieSerializer,GuestSerializer
from rest_framework.decorators import api_view
# Create your views here.

# def no_rest_no_model(request):
#     guests =[
#         {
#             'id': 1,
#             'Name': 'omar',
#             'mobile': 123456
                
#         },
        
#         {
#             'id': 2,
#             'Name': 'Ahmed',
#             'mobile':456789
#         }
#     ]
#     return JsonResponse (guests, safe = False)

# def no_rest_from_model(request):
#     data = Guest.objects.all()
#     response = {
#         'guests': list(data.values('name','mobile'))
#     }
#     return JsonResponse(response)


api_view(['GET','POST'])
def FBV_List(request):
    
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests,many=True)
        return Response (serializer.data)
    
    
