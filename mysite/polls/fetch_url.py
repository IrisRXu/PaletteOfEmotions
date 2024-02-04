import openai
import re
import requests
import random


# Set your OpenAI API key here
openai.api_key = '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'

# without highlight
'''
def fetch_artwork_details_with_images(query):
    def save_artwork_ids_with_images(query):
        ids_with_images = []
        search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}&hasImages=true"
        search_response = requests.get(search_url)

        if search_response.status_code == 200:
            data = search_response.json()
            if data['total'] > 0 and data.get('objectIDs'):
                for i in data['objectIDs']:
                    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}"
                    object_response = requests.get(object_url)

                    if object_response.status_code == 200:
                        object_data = object_response.json()
                        if object_data.get("primaryImage"):
                            ids_with_images.append(i)
                return ids_with_images
        return []

    ids_with_images = save_artwork_ids_with_images(query)
    artworks_details = []  # 2D array to hold the ID and title
    titles = []  # List to hold the titles of the artworks

    for i in ids_with_images:
        object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}"
        object_response = requests.get(object_url)

        if object_response.status_code == 200:
            object_data = object_response.json()

            if object_data.get("title"):
                titles.append(object_data.get("title"))
                artworks_details.append([i, object_data.get("title")])

    titles_string = ", ".join(titles)
    return artworks_details, titles_string


def extract_artwork_name_from_quotes(text):
    # Pattern to capture text following "Name:" until a newline or the end of the string
    pattern = r'Name:\s*(.+)'
    match = re.search(pattern, text)

    if match:
        # Return the captured group, which is the artwork name following "Name:"
        return match.group(1).strip()  # Using strip() to remove any trailing whitespace
    else:
        return None


def extract(text):
    # Pattern to capture text following "Name:" until a newline or the end of the string
    pattern = r'Reason:\s*(.+)'
    match = re.search(pattern, text)

    if match:
        # Return the captured group, which is the artwork name following "Name:"
        return match.group(1).strip()  # Using strip() to remove any trailing whitespace
    else:
        return None


def find(namelist, mood):
    prompt = (f"Given the artwork I provide you, "
              f"\n\n{namelist}\n\n return only one work that is mostly in the theme of {mood}"
              f" you must must follow this output format:"
              f" reason: "
              f" Name: "
              )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", temperature=0.5,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700  # Adjust based on your needs
    )

    result = response['choices'][0]['message']['content'].strip()
    return result


def extract_mood(text):
    """
    Extracts the word immediately following 'adjective:' in the provided text.

    Parameters:
    - text (str): The string containing 'adjective:' followed by the mood.

    Returns:
    - str: The extracted mood, or None if not found.
    """
    # Regular expression pattern to find 'adjective:' followed by any word (\w+)
    # \w+ matches one or more word characters (letters, digits, or underscores)
    pattern = r'adjective:\s*(\w+)'
    match = re.search(pattern, text)

    if match:
        return match.group(1)  # Return the captured group, which is the mood word
    else:
        return None


def get_artwork_image(id):
    # Step 1: Search for the artwork by title
    ids_with_images = []

    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
    object_response = requests.get(object_url)
    object_data = object_response.json()
    print(f"https://www.metmuseum.org/art/collection/search/{id}")

    return object_data.get("primaryImage")


def conclude_emotion(feeling):
    # Corrected API call as per the new OpenAI API version

    prompt = (f"Given the feeling of the user"
              f"\n\n{feeling}\n\n"
              f"conclude the user input using only one adjective and don't use word such as content"
              f"which has multiple meanings. use word as easy as happy, sad, and exciting"
              f"your output should only follow the format I provide"
              f"adjective: "
              )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", temperature=0.9,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700  # Adjust based on your needs
    )

    result = response['choices'][0]['message']['content'].strip()

    return result
'''
'''
def fetch_artwork_details_with_images(query):
    def save_artwork_ids_with_images(query):
        ids_with_images = []
        search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}&hasImages=true&isHighlight=true"
        search_response = requests.get(search_url)

        if search_response.status_code == 200:
            data = search_response.json()
            if data['total'] > 0 and data.get('objectIDs'):
                for i in data['objectIDs']:
                    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}"
                    object_response = requests.get(object_url)

                    if object_response.status_code == 200:
                        object_data = object_response.json()
                        if object_data.get("primaryImage"):
                            ids_with_images.append(i)
                return ids_with_images
        return []

    ids_with_images = save_artwork_ids_with_images(query)
    artworks_details = []  # 2D array to hold the ID and title
    titles = []  # List to hold the titles of the artworks

    for i in ids_with_images:
        object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}"
        object_response = requests.get(object_url)

        if object_response.status_code == 200:
            object_data = object_response.json()

            if object_data.get("title"):
                titles.append(object_data.get("title"))
                artworks_details.append([i, object_data.get("title")])

    titles_string = ", ".join(titles)
    return artworks_details, titles_string


def extract_artwork_name_from_quotes(text):
    # Pattern to capture text following "Name:" until a newline or the end of the string
    pattern = r'Name:\s*(.+)'
    match = re.search(pattern, text)

    if match:
        # Return the captured group, which is the artwork name following "Name:"
        return match.group(1).strip()  # Using strip() to remove any trailing whitespace
    else:
        return None


def extract(text):
    # Pattern to capture text following "Name:" until a newline or the end of the string
    pattern = r'Reason:\s*(.+)'
    match = re.search(pattern, text)

    if match:
        # Return the captured group, which is the artwork name following "Name:"
        return match.group(1).strip()  # Using strip() to remove any trailing whitespace
    else:
        return None


def find(namelist, mood):
    prompt = (f"Given the titles of the artwork"
              f"\n\n{namelist}\n\n"
              f" return the work that is mostly related to the mood {mood}"
              f" you must follow this output format:"
              f" reason:"
              f" Name:"
              )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700  # Adjust based on your needs
    )

    result = response['choices'][0]['message']['content'].strip()
    return result


def extract_mood(text):
    """
    Extracts the word immediately following 'adjective:' in the provided text.

    Parameters:
    - text (str): The string containing 'adjective:' followed by the mood.

    Returns:
    - str: The extracted mood, or None if not found.
    """
    # Regular expression pattern to find 'adjective:' followed by any word (\w+)
    # \w+ matches one or more word characters (letters, digits, or underscores)
    pattern = r'adjective:\s*(\w+)'
    match = re.search(pattern, text)

    if match:
        return match.group(1)  # Return the captured group, which is the mood word
    else:
        return None


def get_artwork_image(id):
    # Step 1: Search for the artwork by title
    ids_with_images = []

    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
    object_response = requests.get(object_url)
    object_data = object_response.json()
    print(f"https://www.metmuseum.org/art/collection/search/{id}")

    return object_data.get("primaryImage")


def conclude_emotion(feeling):
    # Corrected API call as per the new OpenAI API version

    prompt = (f"Given the feeling of the user"
              f"\n\n{feeling}\n\n"
              f"conclude the mood of the user using only one adjective and don't use word such as content"
              f"which has multiple meanings. use word as easy as happy, sad, and exciting"
              f"your output should only follow the format I provide"
              f"adjective: "
              )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", temperature=0.9,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700  # Adjust based on your needs
    )

    result = response['choices'][0]['message']['content'].strip()

    return result
'''

def fetch_artwork_details_with_images(query):
    def save_artwork_ids_with_images(query):
        ids_with_images = []
        search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}&hasImages=true"
        search_response = requests.get(search_url)

        if search_response.status_code == 200:
            data = search_response.json()
            if data['total'] > 0 and data.get('objectIDs'):
                for i in data['objectIDs']:
                    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}"
                    object_response = requests.get(object_url)

                    if object_response.status_code == 200:
                        object_data = object_response.json()
                        if object_data.get("primaryImage"):
                            ids_with_images.append(i)
                return ids_with_images
        return []

    ids_with_images = save_artwork_ids_with_images(query)
    artworks_details = []  # 2D array to hold the ID and title
    titles = []  # List to hold the titles of the artworks

    for i in ids_with_images:
        object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}"
        object_response = requests.get(object_url)

        if object_response.status_code == 200:
            object_data = object_response.json()

            if object_data.get("title"):
                titles.append(object_data.get("title"))
                artworks_details.append([i, object_data.get("title")])

    num_items_to_select = min(10, len(titles))
    if num_items_to_select > 0:
        selected_indices = random.sample(range(len(titles)), num_items_to_select)
        titles = [titles[i] for i in selected_indices]
        artworks_details = [artworks_details[i] for i in selected_indices]

    titles_string = ", ".join(titles)
    return artworks_details, titles_string


def extract_artwork_name_from_quotes(text):
    # Pattern to capture text following "Name:" until a newline or the end of the string
    pattern = r'Name:\s*(.+)'
    match = re.search(pattern, text)

    if match:
        # Return the captured group, which is the artwork name following "Name:"
        return match.group(1).strip()  # Using strip() to remove any trailing whitespace
    else:
        return None


def extract(text):
    # Pattern to capture text following "Name:" until a newline or the end of the string
    pattern = r'Reason:\s*(.+)'
    match = re.search(pattern, text)

    if match:
        # Return the captured group, which is the artwork name following "Name:"
        return match.group(1).strip()  # Using strip() to remove any trailing whitespace
    else:
        return None


def find(namelist, mood):
    prompt = (f"Given the artwork I provide you, "
              f"\n\n{namelist}\n\n return only one work that is mostly in the theme of {mood}"
              f" you must must follow this output format:"
              f" reason: "
              f" Name: "
              )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", temperature=0.5,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700  # Adjust based on your needs
    )

    result = response['choices'][0]['message']['content'].strip()
    return result


def extract_mood(text):
    """
    Extracts the word immediately following 'adjective:' in the provided text.

    Parameters:
    - text (str): The string containing 'adjective:' followed by the mood.

    Returns:
    - str: The extracted mood, or None if not found.
    """
    # Regular expression pattern to find 'adjective:' followed by any word (\w+)
    # \w+ matches one or more word characters (letters, digits, or underscores)
    pattern = r'adjective:\s*(\w+)'
    match = re.search(pattern, text)

    if match:
        return match.group(1)  # Return the captured group, which is the mood word
    else:
        return None


def get_artwork_image(id):
    # Step 1: Search for the artwork by title
    ids_with_images = []

    object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
    object_response = requests.get(object_url)
    object_data = object_response.json()
    print(f"https://www.metmuseum.org/art/collection/search/{id}")

    return object_data.get("primaryImage")


def conclude_emotion(feeling):
    # Corrected API call as per the new OpenAI API version

    prompt = (f"Given the feeling of the user"
              f"\n\n{feeling}\n\n"
              f"conclude the user input using only one adjective and don't use word such as content"
              f"which has multiple meanings. use word as easy as happy, sad, and exciting"
              f"your output should only follow the format I provide"
              f"adjective: "
              )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", temperature=0.9,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700  # Adjust based on your needs
    )

    result = response['choices'][0]['message']['content'].strip()

    return result



# generate with Dalle
def generate_image(response1, user_text):

    try:
        # Formulating the prompt for DALL-E
        prompt = f"Create a new image inspired by the artwork '{response1}' and the person who has the mood '{user_text}'."

        # Generating the image with DALL-E
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Generate 1 image
            size="1024x1024"  # Image size
        )

        # Assuming the response includes URLs to the generated images
        image_urls = [data['url'] for data in response['data']]

        if image_urls:
            return image_urls[0]  # Return the first image URL
        else:
            return "No image was generated."

    except Exception as e:
        return f"An error occurred: {str(e)}"

def give_explanation(title, user_text):
    prompt = (f"Please just repeat the title '{title}' and a colon then the second line should be an explanation of why could this artwork (do not state the artist name nor the date) correspond to the feeling of the person who input '{user_text}' "
              )

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview", temperature=0.5,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700  # Adjust based on your needs
    )

    result = response['choices'][0]['message']['content'].strip()
    return result