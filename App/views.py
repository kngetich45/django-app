from django.shortcuts import render
from App.models import Member
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

#My imports
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def frontend(request):
    return render(request, "frontend.html")

#--------------- backend ---------------------------|
# Backend section.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):

    if 'q' in request.GET:
        q = request.GET['q']
        all_member_list = Member.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q)
        ).order_by('-created_at')
    else:
        all_member_list = Member.objects.all().order_by('-created_at')

    paginator = Paginator(all_member_list, 4)
    page = request.GET.get('page')
    all_member = paginator.get_page(page)
    return render(request, "backend.html", {"members":all_member})

# Add new members
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def add_member(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('username') and request.POST.get('phone') and request.POST.get('location') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('bio'):
            member = Member()
            member.name = request.POST.get('name')
            member.username = request.POST.get('username')
            member.phone = request.POST.get('phone')
            member.email = request.POST.get('email')
            member.age = request.POST.get('age')
            member.gender = request.POST.get('gender')
            member.bio = request.POST.get('bio')
            member.location = request.POST.get('location')
            member.save()
            messages.success(request, "New member added successully !!")
            return HttpResponseRedirect('/backend')
    else:
            return render(request, 'add.html')

# Fuction to access the members individually
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def member(request, member_id):
    member = Member.objects.get(id = member_id)
    if member != None:
        return render(request, "edit_member.html", {'member':member})


# Functions to edit the members
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_member(request):
    if request.method == "POST":
        member = Member.objects.get(id= request.POST.get('id'))
        if member != None:
            member.name = request.POST.get('name')
            member.username = request.POST.get('username')
            member.age = request.POST.get('age')
            member.gender = request.POST.get('gender')
            member.location = request.POST.get('location')
            member.phone = request.POST.get('phone')
            member.bio = request.POST.get('bio')
            member.email = request.POST.get('email')
            member.save()

            messages.success(request, "members updated successully !!")
            return HttpResponseRedirect('/backend')


# Functions to Delete the member
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def delete_member(request, member_id):
    member = Member.objects.get(id = member_id)
    member.delete()

    messages.success(request, "Member deleted successully !!")
    return HttpResponseRedirect('/backend')

 