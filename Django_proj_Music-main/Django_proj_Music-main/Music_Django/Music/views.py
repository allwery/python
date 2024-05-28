from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


from .models import Concert, Buyer
from .forms import BuyingForm, BuyerForm
from django.template.context_processors import csrf


def concert_home(request):
    return HttpResponse('<h1> Home </h1>')


def concert_detail(request, id=None):
    instance = get_object_or_404(Concert, id=id)
    context = {
        'title':'Детали',
        'instance':instance,
    }
    return render(request, 'Music/concert_detail.html', context)


def buyer_detail(request, id=None):
    instance = get_object_or_404(Buyer, id=id)
    context = {
        'title':'Детали',
        'instance':instance,
    }
    return render(request, 'Music/buyer_detail.html', context)


def concert_list(request):
    queryset = Concert.objects.all()
    context = {
        'queryset':queryset,
        'title': 'Концерты'
    }
    return render(request, 'Music/index.html', context)


def buyer_list(request):
    queryset = Buyer.objects.all()
    context = {
        'queryset': queryset,
        'title': 'Покупатели'
    }
    return render(request, 'Music/buyer_list.html', context)


def buyer_update(request, id=None):
    instance = get_object_or_404(Buyer, id=id)
    form = BuyerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/Music')
    context = {
        'title':"Обновить данные",
        'instance':instance,
        'form':form,
        'what_to_do':'Обновить',
    }
    return render(request, 'Music/buyer_create.html', context)


"""def buyer_delete(request, id=None):
    instance = get_object_or_404(Buyer, id=id)
    instance.delete()
    return HttpResponseRedirect('/Music')"""


def buying_create(request):
    form = BuyingForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/Music')
    context = {
        'form':form,
    }
    return render(request, 'Music/buying_create.html', context)


def buyer_create(request):
    form = BuyerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/Music')
    context = {
        'form':form,
        'what_to_do':'Зарегестрироваться'
    }
    return render(request, 'Music/buyer_create.html', context)