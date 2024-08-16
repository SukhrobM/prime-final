from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Gallery, Navigation, Painting, Terms
from django.urls import reverse
from .forms import RegisterForm


# Create your views here.
def home_page(request):
    categories = Navigation.objects.all()
    pictures = Gallery.objects.all()
    level = Painting.objects.all()
    context = {
        'categories': categories,
        'pictures': pictures,
        'level': level
    }
    return render(request, 'home.html', context)


def get_terms(request, id):
    content = get_object_or_404(Terms, id=id)
    level = Painting.objects.all()
    context = {
        'content': content,
        'level': level
    }
    return render(request, 'terms.html', context)


def get_category(request, id):
    exact_category = Navigation.objects.get(id=id)
    categories = Navigation.objects.all()
    level = Painting.objects.all()
    if exact_category.id == 3:
        to_gallery = reverse('gallery')
        return redirect(to_gallery)
    context = {
        'exact_category': exact_category,
        'categories': categories,
        'level': level
    }
    return render(request, 'categories.html', context)


def gallery(request, id=3):
    gallery_list = Gallery.objects.all()
    gallery_categories = get_object_or_404(Navigation, id=id)
    categories = Navigation.objects.all()
    level = Painting.objects.all()
    context = {
        'gallery_list': gallery_list,
        'gallery_categories': gallery_categories,
        'categories': categories,
        'level': level
    }
    return render(request, 'gallery.html', context)


def levels(request, id):
    level_categories = get_object_or_404(Painting, id=id)
    categories = Navigation.objects.all()
    level = Painting.objects.all()
    context = {
        'level_categories': level_categories,
        'categories': categories,
        'level': level
    }
    return render(request, 'level.html', context)


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password2 = form.clean_password2()
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username, password=password2, email=email)
            user.save()
            login(request, user)
            return redirect('/')

        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')
