import requests
from utils.csv_utils import write_csv

metadata_url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
base_url = "http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{0}')"


def get_metadata():
    r = requests.get(metadata_url)
    metadata_json = r.json()
    metadata_items = metadata_json.get("value")
    print("Metadata:")
    print(metadata_items[0].keys())


def get_data(sercodigo):
    url_to_get = base_url.format(sercodigo)
    print(f"Requesting data to {url_to_get}")
    r = requests.get(url_to_get)
    data_json = r.json()
    data_items = data_json.get("value")
    print(f"get_data got {len(data_items)} items for sercodigo={sercodigo}")
    header = list(data_items[0].keys())
    data_to_write = [list(item.values()) for item in data_items]
    write_csv(data_to_write, header, f"data/{sercodigo}.csv")


def get_ipea_data(codes_to_get):
    print(f"Looking for codes in file {codes_to_get} on IPEA API.")
    f = open(codes_to_get, "r")
    codes = f.readlines()
    for code in codes:
        get_data(code.rstrip("\n"))
    f.close()


if __name__ == "__main__":
    get_data("PRECOS_INPCBR")
