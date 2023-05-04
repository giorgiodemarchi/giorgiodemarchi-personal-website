from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


# Create your models here.

class BlogPage(Page):

    template = 'home/blog_post.html'

    date = models.DateField("Post date")
    body = RichTextField(blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('feed_image'),
    ]

    class Meta:
        ordering = ['-date']

class PortfolioPage(Page):

    template = 'home/blog_post.html'

    date = models.DateField("Post date")
    body = RichTextField(blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('feed_image'),
    ]

    class Meta:
        ordering = ['-date']
