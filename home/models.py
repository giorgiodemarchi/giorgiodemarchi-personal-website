from django.db import models
from wagtail.models import Page
from blog.models import BlogPage, PortfolioPage


class HomePage(Page):
    """
    Main page
    """
    template = 'home/home_page.html'
    #banner_title = models.CharField(max_length=100, blank=False, null=True)

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['blog_post'] = self.get_children().type(BlogPage)
        context['portfolio_post'] = self.get_children().type(PortfolioPage)
        return context
