from django.shortcuts import render, redirect

from web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, ProfileDeleteForm
from web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as e:
        return None


def index(request):
    profile = get_profile()
    has_profile = True
    if profile is None:
        has_profile = False
    context = {
        'has_profile': has_profile
    }
    return render(request, 'index.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile-create.html',
        context,
    )


def catalogue_page(request):
    profile = get_profile()
    cars = Car.objects.all()
    cars_count = Car.objects.count()
    context = {
        'profile': profile,
        'cars': cars,
        'cars_count': cars_count,
    }
    return render(request, 'catalogue.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'form': form,
    }

    return render(
        request,
        'car-create.html',
        context,
    )


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car
    }

    return render(
        request,
        'car-details.html',
        context,
    )


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'form': form,
        'car': car,
    }

    return render(
        request,
        'car-edit.html',
        context,
    )


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'form': form,
        'car': car,
    }

    return render(
        request,
        'car-delete.html',
        context,
    )


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = sum([c.price for c in cars])

    context = {
        'profile': profile,
        'total_price': total_price,
    }

    return render(
        request,
        'profile-details.html',
        context,
    )


def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,

    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile-delete.html',
        context,
    )
