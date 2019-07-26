from src.pexels import page
import os
# Init page object with your Pexels API key
API_KEY = os.environ.get("PEXELS_API_KEY")
pexels_page = page(API_KEY)
# Search 'koala' photos
pexels_page.search("koala")
print("Total results: {}".format(pexels_page.total_results))
# Loop all the pages
while True:
    # Get all photos in the page
    photos = pexels_page.get_entries()
    # For each photo print its properties
    for photo in photos:
        print("-----------------------------------------------")
        print("Photo id: {}".format(photo.id))
        print("Photo width: {}".format(photo.width))
        print("Photo height: {}".format(photo.height))
        print("Photo url: {}".format(photo.url))
        print("Photographer: {}".format(photo.photographer))
        print("Photo description: {}".format(photo.description))
        print("Photo extension: {}".format(photo.extension))
        print("Photo sizes:")
        print("\toriginal: {}".format(photo.original))
        print("\tcompressed: {}".format(photo.compressed))
        print("\tlarge2x: {}".format(photo.large2x))
        print("\tlarge: {}".format(photo.large))
        print("\tmedium: {}".format(photo.medium))
        print("\tsmall: {}".format(photo.small))
        print("\ttiny: {}".format(photo.tiny))
        print("\tportrait: {}".format(photo.portrait))
        print("\tlandscape: {}".format(photo.landscape))
    # Search next page. If there is no next page print the last page and end the loop
    if not pexels_page.search_next():
        print("Last page: {}".format(pexels_page.page))
        break
