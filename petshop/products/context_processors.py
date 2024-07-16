# products/context_processors.py
from .models import SubCategory, MainCategory,AnimalType


def animal_types_processor(request):
    animal_types = AnimalType.objects.prefetch_related('main_categories__sub_categories').all()
    return {'animal_types': animal_types}