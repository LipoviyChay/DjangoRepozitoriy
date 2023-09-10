from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .forms import AdvForm
from .models import Advertisement

User=get_user_model()
# Create your views here.
def index_(request):
    title=request.GET.get('query')
    if title:
        advertisements=Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context={'advertisements': advertisements,
             'title': title}
    return render(request, 'advert/index.html', context)
def top_sellers(request):
    users=User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context={'users':users}
    return render(request, 'advert/top-sellers.html', context)
@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method=='POST':
        form = AdvForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement=form.save(commit=False)
            advertisement.user=request.user
            advertisement.save()
            url=reverse('main-page')
            return redirect(url)
    else:
        form=AdvForm
    form=AdvForm()
    context={'form':form}
    return render(request, 'advert/advertisement-post.html', context)

def advertisement_detail(request, pk):
    advertisement=Advertisement.objects.get(id=pk)
    context = {'advertisement': advertisement}
    return render(request, 'advert/advertisement.html', context)