import requests


def name_trunc(input_string: str) -> str:

    count = 0
    output_string = ""

    for letter in input_string:
        output_string += letter
        count += 1
        if count == 3:
            return output_string


def fuel_percentage():
    headers = {
        'Accept': 'application/json'
    }

    url = "https://api.carbonintensity.org.uk/generation"

    r = requests.get(url, params={}, headers=headers)

    data = r.json()

    actual = (data['data']['generationmix'][3])
    fuel_type = actual['fuel']
    percentage = actual['perc']

    output = f"{percentage}% of electrical generation is provided by {fuel_type}."

    return output
