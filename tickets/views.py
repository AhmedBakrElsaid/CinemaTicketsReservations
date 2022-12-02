from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

def no_rest_no_model(request):
    guests =[
        {
            'id': 1,
            'Name': 'omar',
            'mobile': 123456
                
        },
        
        {
            'id': 2,
            'Name': 'Ahmed',
            'mobile':456789
        }
    ]
    return JsonResponse (guests, safe = False)