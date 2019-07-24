# Author:           Arturo Aguilar Lagunas
# Pexels Website:   https://www.pexels.com
# Date:             17/07/2019
# You can:
    # Get json data from https://www.pexels.com
    # Search photos using pexels API v1
    # Search popular photos using pexels API v1
    # Search curated photos using pexels API v1
# Dependencies:
    # requests
# Pexels API usage:
    # To get access you have to add a HTTP Authorization header to each of your requests. (required)
    # Authorization: YOUR_API_KEY
    # Search: https://api.pexels.com/v1/search?query=example+query&per_page=15&page=1
        # query		Get photos related to this query. (required)
        # per_page	Defines the number of results per page. (optional, default: 15, max: 80)
        # page		Defines the number of the page. (optional, default: 1)
import requests
class pexels_api:
    def __init__(self, PEXELS_API_KEY):
        self.PEXELS_AUTHORIZATION = {"Authorization":PEXELS_API_KEY}
        self.request = None
        self.json = None
        self.page = None
        self.total_results = None
        self.page_results = None
        self.has_next = None
        self.has_prev = None
        self.next_page = None
        self.prev_page = None
    """ Returns json for the given query """
    def search(self, query, results_per_page=15, page=1):
        query = query.replace(" ", "+")
        url = "https://api.pexels.com/v1/search?query={}&per_page={}&page={}".format(query, results_per_page, page)
        self.__request(url)
        # If there is no json data return None
        return None if not self.request else self.json
    """ Return json with popular photos of the current page """
    def popular(self, results_per_page=15, page=1):
        url = "https://api.pexels.com/v1/popular?per_page={}&page={}".format(results_per_page, page)
        self.__request(url)
        # If there is no json data return None
        return None if not self.request else self.json
    """ Return json with curated photos of the current page """
    def curated(self, results_per_page=15, page=1):
        url = "https://api.pexels.com/v1/curated?per_page={}&page={}".format(results_per_page, page)
        self.__request(url)
        # If there is no json data return None
        return None if not self.request else self.json
    """ Returns json of the next page if available """
    def search_next_page(self):
        if self.has_next:
            self.__request(self.next_page)
        else:
            return None
        # If there is no json data return None
        return None if not self.request else self.json
    """ Returns json of the previous page if available """
    def search_previous_page(self):
        if self.has_prev:
            self.__request(self.prev_page)
        else:
            return None
        # If there is no json data return None
        return None if not self.request else self.json

    """ Returns a list of photo properties for each photo in the current page """
    def get_entries(self):
        if not self.json:
            return None
        return [photo_properties(photo) for photo in self.json["photos"]]

    """ Private methods """
    def __request(self, url):
        try:
            self.request = requests.get(url, timeout=15, headers=self.PEXELS_AUTHORIZATION)
            self.__update_page_properties()
        except requests.exceptions.RequestException:
            print("Request failed check your internet connection")
            print("Url: {}".format(url))
            self.request = None
            exit()
    def __update_page_properties(self):
        if self.request.ok:
            self.json = self.request.json()
            try:
                self.page = int(self.json["page"])
            except:
                self.page = None
            try:
                self.total_results = int(self.json["total_results"])
            except:
                self.total_results = None
            try:
                self.page_results = len(self.json["photos"])
            except:
                self.page_results = None
            try:
                self.next_page = self.json["next_page"]
                self.has_next = True
            except:
                self.next_page = None
                self.has_next = False
            try:
                self.prev_page = self.json["prev_page"]
                self.has_prev = True
            except:
                self.prev_page = None
                self.has_prev = False
        else:
            print("Wrong response you might have a wrong API key")
            print(self.request)
            print("API key: {}".format(self.PEXELS_AUTHORIZATION))
            self.request = None
            exit()

""" Subclass """
class photo_properties:
    def __init__(self, json_photo):
        self.__photo = json_photo
    @property
    def id(self):
        return int(self.__photo["id"])
    @property
    def width(self):
        return int(self.__photo["width"])
    @property
    def height(self):
        return int(self.__photo["height"])
    @property
    def photographer(self):
        return self.__photo["photographer"]
    @property
    def url(self):
        return self.__photo["url"]
    @property
    def description(self):
        return self.url.split("/")[-2].replace("-{}".format(self.id), "")
    @property
    def src(self):
        return self.__photo["src"]
    @property
    def original(self):
        return self.src["original"]
    @property
    def compressed(self):
        return self.original + "?auto=compress"
    @property
    def large2x(self):
        return self.src["large2x"]
    @property
    def large(self):
        return self.src["large"]
    @property
    def medium(self):
        return self.src["medium"]
    @property
    def small(self):
        return self.src["small"]
    @property
    def portrait(self):
        return self.src["portrait"]
    @property
    def landscape(self):
        return self.src["landscape"]
    @property
    def tiny(self):
        return self.src["tiny"]
    @property
    def extension(self):
        return self.original.split(".")[-1]
