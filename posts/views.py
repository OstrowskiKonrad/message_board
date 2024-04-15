from django.views.generic.list import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'