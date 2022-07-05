import requests
import random

def show_sides():
    url = "https://myqa.fleksa.com/pyapi/26/menu"

    json_data = list(requests.get(url).json()['sides'].values())
    item_names = []
    prices = []


    for item in json_data:
        if item['in_stock'] == True:
            item_names.append(list(item['name_json'].values())[0])
            prices.append(item['price'])

    # print("Please type your selection from the following sides listed below: \n")
    res = ""
    for i in range(0,5):
        res += "\nItem Name: " + item_names[random.randint(0, len(item_names))] + "\n" + "Price: €" + str(prices[random.randint(0, len(prices))]) + "\n"
    return res

