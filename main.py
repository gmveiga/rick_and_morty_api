import requests
import json
import random

male_character_id = 244
female_character_id = 4
min_episodes = 3

def get_character(id):
    api_response = requests.get(f"https://rickandmortyapi.com/api/character/{id}")
    return json.loads(api_response.text)

def get_episodes(urls):
    ids = ','.join(list(map(lambda url: url.split('/')[-1], urls))) 
    api_episodes_response = requests.get(f"https://rickandmortyapi.com/api/episode/{ids}")
    return json.loads(api_episodes_response.text)

characters = {
    'male': get_character(male_character_id),
    'female': get_character(female_character_id)
}

for gender in characters:
    episode_urls = random.sample(characters[gender]['episode'], min_episodes)
    characters[gender]['episodes'] = get_episodes(episode_urls)