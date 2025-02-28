
from countries import countries
from countries_details_dat import countries_data

# 1. Extract countries with 'land' 
countries_with_land = [country for country in countries if 'land' in country]

# 2. Count the number of languages spoken in each country
countries_language_count = {country['name']: len(country['languages']) for country in countries_data}
# 2. Count the number of languages spoken all over the world
all_languages = set()  
for country in countries_data:
    all_languages.update(country['languages'])
total_languages_spoken = len(all_languages) 
# 3. Find the most spoken languages
language_count = {}
for country in countries_data:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1
most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

# 4. Find the country with the largest population
largest_population_country = max(countries_data, key=lambda x: x['population'])

# Print Results
print("Countries with 'land' in their name:", countries_with_land)
print("\nNumber of languages spoken per country:", countries_language_count)
print("\nMost spoken languages:", most_spoken_languages)
print("\nCountry with the largest population:", largest_population_country)
