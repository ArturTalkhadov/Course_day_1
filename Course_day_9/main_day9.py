import os

def cls():
    """
    функция для очистки экрана
    """
    os.system('CLS')

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# function that will allow new countries
#added to the travel_log.
def add_new_country(add_country, visits_sum, list_city):
    """
    функция  добавления нового словаря в список словарей.
    """
    new_dict= dict(country = add_country, visits = visits_sum, cities = list_city)
    travel_log.append(new_dict)


#выводим результат
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
