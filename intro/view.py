from django.http import HttpResponse

def index(request):
  
    return HttpResponse("<h1>Index</h1>")

def home(request):
      
     return HttpResponse("<h1>Home</h1>")

def about(request):
      
     return HttpResponse("<h1>About</h1>")  

def contact(request): 
    return HttpResponse("<h1>Contact</h1>")



    

