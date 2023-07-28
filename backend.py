import requests

API_KEY = "aa7d006ca5fe0eaf26c5fb679ea83399"


def get_data(place, forcasted_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcasted_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "main":
    print(get_data(place="Tokyo", forcasted_days=2))
