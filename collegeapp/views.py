# Create your views here.
from django.shortcuts import render_to_response
#from django.http import HttpResponse

class UrlHandlers():
    def __init__(self):
        pass
    def collegeadmin(self, request):
        return render_to_response('adminlogin.html')
