from django.shortcuts import render, redirect

from .models import Link
from .forms import MyModelForm, SigningForm
from django.contrib import admin
from django.urls import path
from django.contrib.auth import login


def add_content(request):
    if request.method=='POST':
        data = MyModelForm(request.POST)
        if data.is_valid():
            bruh = data.save(commit=False)
            bruh.user = request.user
            bruh.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        data = MyModelForm()

    data = [None] * 100
    data[0] =Link.objects.filter(user=request.user, urgency=5)
    data[1] = Link.objects.filter(user=request.user, urgency=4)
    data[2] = Link.objects.filter(user=request.user, urgency=3)
    data[3] = Link.objects.filter(user=request.user, urgency=2)
    data[4] = Link.objects.filter(user=request.user, urgency=1)

    return render(request, 'themain/index.html', {'data': data, 'range': range(5)})




def delete_link(request, item_id):
    try:
        link = Link.objects.get(id=item_id)
        link.delete()
        return redirect('http://127.0.0.1:8000/')
    except Link.DoesNotExist:
        raise Http404("Link not found")

def signing(request):
    if request.method=='POST':
        form = SigningForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('add_content')
    else:
        form = SigningForm()
    return render(request, 'themain/signing.html', {'form': form})
