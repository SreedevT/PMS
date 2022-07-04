from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("THIS TEST")

def profile(request, pk):
    return HttpResponse(f"This is profile {pk.profile_pic}")
