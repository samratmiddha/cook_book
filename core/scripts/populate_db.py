import json
from core.models import Recipe


def populate():
    with open('core/constants/dummy_data.json','r') as file:
        file_content=file.read()
        recipes_data=json.loads(file_content)


    for recipe in recipes_data:
        Recipe.objects.create(title=recipe["title"],description=recipe["description"],is_public=True,ingredients=recipe["ingredients"],steps=recipe["steps"],image=recipe["image"])