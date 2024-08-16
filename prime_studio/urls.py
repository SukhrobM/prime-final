from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('categories/<int:id>', views.get_category, name='categories'),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('level/<int:id>', views.levels, name='level'),
    path('terms/<int:id>', views.get_terms, name='terms')
]
