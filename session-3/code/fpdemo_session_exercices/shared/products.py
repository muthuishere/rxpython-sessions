import json
from pathlib import Path


def get_products():
    current_path_of_folder = str(Path(__file__).parent.absolute())
    file = open( current_path_of_folder + '\\products.json')
    products = json.load(file)
    file.close()
    return products