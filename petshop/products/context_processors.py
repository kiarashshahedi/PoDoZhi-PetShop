# products/context_processors.py
from .models import SubCategory, MainCategory,Type


def animal_types_processor(request):
    animal_types = Type.objects.prefetch_related('main_categories__sub_categories').all()
    return {'animal_types': animal_types}