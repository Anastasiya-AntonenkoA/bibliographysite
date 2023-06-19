from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView

from .forms import MaterialForm
from .models import Resource, Material


class ResourceSearchView(ListView):
    model = Resource
    template_name = 'resource_search.html'
    context_object_name = 'resources'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Resource.objects.filter(title__icontains=query)
        return Resource.objects.all()


class ResourceListView(ListView):
    model = Resource
    template_name = 'resource_list.html'
    context_object_name = 'resources'
    paginate_by = 10


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Incorrect username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def add_resource_view(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MaterialForm()

    return render(request, 'add_resource.html', {'form': form})


def edit_resource_view(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)

    return render(request, 'edit_resource.html', {'form': form})


class HomePageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materials'] = Material.objects.all()
        return context


def materials_view(request):
    materials = Material.objects.all()
    return render(request, 'materials.html', {'materials': materials})

def about_us(request):
    return render(request, 'about.html')