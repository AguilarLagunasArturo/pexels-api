from src.pexels import pexels_api
import requests

PEXELS_API_KEY = "563492ad6f9170000100000150556b6073604f86abed1feccc6bd0d8"
pexels = pexels_api(PEXELS_API_KEY)

pexels.search("woman in black")
while True:
    for photo in pexels.get_entries():
        print("-------------------------------------")
        print("Photo id: ",photo.id)
        print("Photo width: ", photo.width)
        print("Photo height: ", photo.height)
        print("Photo url: ", photo.url)
        print("Photographer: ",photo.photographer)
        print("Photo original size: ", photo.original)
        print("Photo description: ", photo.description)
        print("Photo extension: ", photo.extension)
        print("Photo sizes:")
        for size, url in photo.src.items():
            print("\t{}: {}".format(size, url))
    if not pexels.search_next_page():
        print("end page: {}".format(pexels.page))
        break
