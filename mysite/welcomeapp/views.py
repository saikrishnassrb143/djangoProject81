from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    res=HttpResponse("""<html>
    <body bgcolor=red>
    <h3><center>*****welcome manikanta*****</center></h3>
    </body>
    </html>""")
    return res
  
