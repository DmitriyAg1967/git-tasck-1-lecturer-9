import requests

if __name__ == '__main__':
    names = ['Hulk', 'Captain America', 'Thanos']
    for name in names:
        url = "https://superheroapi.com/api/2619421814940190/search/"+name
        intelligence = requests.get(url).json()['results'][0]['powerstats']['intelligence']
        superhero_intelligence = 0
        superhero_name = None
        if int(intelligence) > superhero_intelligence:
            superhero_intelligence = intelligence
            superhero_name = name
    print(f'Самый умный супегерой это: {superhero_name} его уровень интеллекта равен - {superhero_intelligence}')



