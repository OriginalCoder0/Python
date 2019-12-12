import json

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2014':
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        print(country_name + ": " + str(population))
