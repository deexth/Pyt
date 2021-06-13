#Function to return a single string of the form City, Country, such as Santiago, Chile
#now modfying the function so it can accept population City, Country - polulation xxx
def city(city, country, population=0):
    """Return a string representing a city-country pair."""

    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string
