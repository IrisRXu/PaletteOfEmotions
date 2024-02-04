from django.shortcuts import render
from django.views import generic
from .fetch_url import *

user_text = ""
title = ""
test_path = "https://images.metmuseum.org/CRDImages/dp/original/DP884893.jpg"

def user_input(request):
    user_text = request.POST.get('user_text', '')  # Get user input from POST data
    response = conclude_emotion(user_text)
    mood = extract_mood(response)
    artworks, titles = fetch_artwork_details_with_images(mood)
    selected = find(titles, mood)
    title = extract_artwork_name_from_quotes(selected)
    for artwork in artworks:
        if artwork[1] == title:  # artwork[1] is the title in the [ID, title] pair
            art_id = artwork[0]
    image_path = get_artwork_image(art_id)
    explanation = give_explanation(title, user_text)
    return render(request, 'polls/input.html', {'selected': explanation, 'image_path': image_path})


def generate_image_page(request):
    dall_path = generate_image(title, user_text)
    return render(request, 'polls/generated.html', {'dall_path': dall_path})


class IndexView(generic.TemplateView):
    template_name = "polls/index.html"