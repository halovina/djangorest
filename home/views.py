from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeIndex(TemplateView):
    template_name = 'home/index.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
