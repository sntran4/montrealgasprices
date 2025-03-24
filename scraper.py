from bs4 import BeautifulSoup
import requests


def scrape_montreal_gas_prices():
    url = "https://www.gasbuddy.com/gasprices/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0",
    }
    session = requests.Session()
    session.get(url, headers=headers)
    page = session.get(f"{url}quebec/montreal", headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    price_boxes = soup.find_all("div", class_="panel__panel___3Q2zW panel__white___19KTz colors__bgWhite___1stjL panel__bordered___1Xe-S panel__rounded___2etNE GenericStationListItem-module__station___1O4vF")
    return get_prices(price_boxes)


def get_prices(price_boxes):
    station_and_prices = {}
    index = 0
    for box in price_boxes:
        station_elem = box.find("a")
        station = station_elem.text
        price_elem = box.find("span", class_="text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL")
        price = price_elem.text
        station_and_prices[index] = {
            "gas_station": station,
            "price": price
        }
        index += 1
    return station_and_prices


if __name__ == "__main__":
    scrape_montreal_gas_prices()
