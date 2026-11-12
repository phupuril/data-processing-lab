import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature',
                lambda temps: sum(float(t) for t in temps) / len(temps),
                cities))
print()

# Print all cities in Germany
germany = filter_items(lambda city: city['country'] == 'Germany', cities)
for city in germany:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
spain = filter_items(
    lambda city: city['country'] == 'Spain' and float(city['temperature']) > 12,
    cities
)
for city in spain:
    print(city)
print()

# Count the number of unique countries
print(aggregate('country', lambda countries: len(set(countries)), cities))
print()

# Print the average temperature for all the cities in Germany
print(aggregate('temperature',
                lambda temps: sum(float(t) for t in temps) / len(temps),
                germany))
print()

# Print the max temperature for all the cities in Italy
italy = filter_items(lambda city: city['country'] == 'Italy', cities)
print(aggregate('temperature', lambda temps: max(float(t) for t in temps), italy))
print()