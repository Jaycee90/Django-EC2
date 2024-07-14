from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("<h1>Pet Adoption System</h1>")

def test(request):
    return HttpResponse("I am the King of the forest, Can you adopt me?")