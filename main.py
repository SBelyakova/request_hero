import requests

class Hero():
  def __init__(self, hero_name):
    self.hero_name = hero_name

  def get_intelligence(self):
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{self.hero_name}')
    data = response.json()['results']
    for hero in data:
      if hero['name'] == self.hero_name:
        hero_intelligence = hero['powerstats']['intelligence']
    return hero_intelligence
    


heroes = [Hero('Hulk'), 
          Hero('Captain America'),
          Hero('Thanos')]

max_int = 0
for hero in heroes:
  intelligence = int(hero.get_intelligence())
  if max_int < intelligence:
    max_int = intelligence
    max_int_hero = hero.hero_name

print(f'Самый умный {max_int_hero} с показателем {max_int}')
    