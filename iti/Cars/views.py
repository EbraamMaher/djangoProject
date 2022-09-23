from django.shortcuts import render
from Cars.forms import CarModelForm
from Cars.models import Car
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def CarsIndex(request):
    allcars = Car.get_all_cars()
    return render(request, "Cars/index.html", context={"Cars": allcars})


class CarDetails(DetailView):
    model = Car
    template_name = "Cars/show.html"


class CreateCarView(CreateView):
    template_name = "Cars/create.html"
    form_class = CarModelForm
    success_url = '/Cars/index'


class EditCarView(UpdateView):
    template_name = "Cars/edit.html"
    form_class = CarModelForm
    success_url = '/Cars/index'
    model = Car


class DeleteCarView(DeleteView):
    template_name = "Cars/delete.html"
    model = Car
    success_url = '/Cars/index'
