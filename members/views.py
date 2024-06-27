from django.shortcuts import render

# Create your views here.
def my_members(request):
    return render(request, 'members/members.html')