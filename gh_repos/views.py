from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """This is a initial view class."""

    def get(self, request, *args, **kwargs):
        """Simple view for index.html."""
        return render(request, 'index.html')
