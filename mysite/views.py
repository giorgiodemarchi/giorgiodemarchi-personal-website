from django.shortcuts import render
from blog.models import BlogPage, PortfolioPage

# Create your views here.

def homepage_view(request):

    blog_post = BlogPage.objects.order_by('-date')
    latest_post = BlogPage.objects.order_by('-date')[0:1]
    portfolio_post = PortfolioPage.objects.order_by('-date')

    return render(request, 'home/home_page.html', {"blog_post":blog_post, "portfolio_post":portfolio_post, "latest_post":latest_post})
