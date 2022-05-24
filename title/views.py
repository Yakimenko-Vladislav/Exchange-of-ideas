from django.shortcuts import render, redirect
from .models import Idea
from .models import Reviewer
from .forms import IdeaForm
from ipware import get_client_ip


def page1(request):
    ideas = Idea.objects.order_by('-rating')
    return render(request, 'title/page1.html', {'ideas': ideas})


def idea(request):
    point = request.GET.get('point')
    point = Idea.objects.filter(id=point)[0]
    address = Reviewer.objects.filter(ip=get_client_ip(request)[0])
    address = address.filter(nickname=point.moniker)
    check = not address.exists()
    if request.method == 'POST' and check:
        appraise = int(request.POST.get('rating', default=0))
        point.rating = point.rating + appraise
        point.save()
        address = Reviewer(ip=get_client_ip(request)[0], nickname=point.moniker, appraising=appraise)
        address.save()
        return redirect('homepage')
    elif request.method == 'POST':
        address = address[0]
        appraise = int(request.POST.get('rating', default=0))
        point.rating = point.rating + appraise - address.appraising
        point.save()
        address.appraising = appraise
        address.save()
        return redirect('homepage')
    return render(request, 'title/idea.html', {'point': point, 'check': check})


def create(request):
    error = ''
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = 'Неверно введенные данные'
    form = IdeaForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'title/create.html', context)


def modifying(request):
    error = ''
    point = request.GET.get('point')
    point = Idea.objects.filter(id=point)[0]
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid() and point.password == form.cleaned_data['password']:
            address = Reviewer.objects.filter(nickname=point.moniker)
            address.delete()
            point.delete()
            form.save()
            return redirect('homepage')
        else:
            error = 'Неверно введенные данные'
    form = IdeaForm(initial={'moniker': point.moniker, 'content': point.content})
    context = {
        'form': form,
        'error': error,
        'point': point
    }
    return render(request, 'title/modifying.html', context)


def deleting(request):
    error = ''
    point = request.GET.get('point')
    point = Idea.objects.filter(id=point)[0]
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        form.is_valid()
        if point.password == form.cleaned_data['password']:
            address = Reviewer.objects.filter(nickname=point.moniker)
            address.delete()
            point.delete()
            return redirect('homepage')
        else:
            error = 'Неверно введенные данные'
    form = IdeaForm()
    context = {
        'form': form,
        'error': error,
        'point': point
    }
    return render(request, 'title/deleting.html', context)
