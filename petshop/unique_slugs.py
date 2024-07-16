import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petshop.settings')
django.setup()

from django.utils.text import slugify
from products.models import Category

def ensure_unique_slugs():
    for category in Category.objects.all():
        unique_slug = slugify(category.name)
        original_slug = unique_slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exclude(id=category.id).exists():
            unique_slug = f"{original_slug}-{counter}"
            counter += 1
        category.slug = unique_slug
        category.save()

if __name__ == "__main__":
    ensure_unique_slugs()
