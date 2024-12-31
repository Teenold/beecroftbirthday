from django.shortcuts import render, redirect
from .models import Happy
# Create your views here.
def home(request):
    return render(request, "happy/index.html")

def inputmess(request):
    if request.method=="POST":
        first_name = request.POST.get("firstname")
        comment = request.POST.get("comment")
        
        new_person = Happy.objects.create(first_name=first_name, message=comment)
        new_person.save()
        return redirect('home')
    return render(request, "happy/mess.html")