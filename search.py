from pexels_api import API
import os
# Init api object with your Pexels API key
API_KEY = os.environ.get("PEXELS_API_KEY")
api = API(API_KEY)
# Search 'koala' photos
api.search("koala")
print("Total results: {}".format(api.total_results))
# Loop all the pages
while True:
    # Get all photos in the page
    photos = api.get_entries()
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
    # If there is no next page print the last page and end the loop
    if not api.has_next_page:
        print("Last page: {}".format(api.page))
        break
    # Search next page
    api.search_next_page()
