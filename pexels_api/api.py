# Author:           Arturo Aguilar Lagunas - https://github.com/AguilarLagunasArturo
# Pexels Website:   https://www.pexels.com
# Review:           Manuel Alfonso Ortiz Lopez - https://github.com/podraco

# class information:
#     Get json data from https://www.pexels.com
#     Search photos using Pexels API v1
#     Search popular photos using Pexels API v1
#     Search curated photos using Pexels API v1

# Dependencies:
#     requests

# General Imports
import requests
import traceback

# Imports Package modules.
from pexels_api.tools import Photo
from pexels_api.exceptions import (
    PexelsInvalidToken,
    PexelsInvalidPhtoID,
    PexelsConnectionClosed,
    PexelsInvalidQuery,
    PexelsForbidden,
    PexelsResouceUnavailable,
    PexelsUnkownException,
)
VALID_SIZES: list[str] = ["large", "medium", "small", ]
"List of valid Photo sizes supported by Pexels API v1."

VALID_ORIENTATIONS: list[str] = ["landscape", "portrait", "square", ]
"List of valid Photo Orientations supported by Pexels API v1."

VALID_LOCATIONS: list[str] = ["en-US", "pt-BR", "es-ES", "ca-ES", "de-DE", "it-IT", "fr-FR", "sv-SE", "id-ID", "pl-PL", "ja-JP", "zh-TW", "zh-CN",
                              "ko-KR", "th-TH", "nl-NL", "hu-HU", "vi-VN", "cs-CZ", "da-DK", "fi-FI", "uk-UA", "el-GR", "ro-RO", "nb-NO", "sk-SK", "tr-TR", "ru-RU", ]
"List of valid locations supported by Pexels API v1."

VALID_COLOR_NAMES: list[str] = ["red", "orange", "yellow", "green", "turquoise",
                          "blue", "violet", "pink", "brown", "black", "gray", "white", ]
"List of valid color names supported by Pexels API v1"


class API:
    """
    API class.

    Use this object as a Session instance.

    :param str PEXELS_API_KEY:
        PEXELS_API_KEY will be the API key provided by Pexels to your account.

    How do i get my Pexels API-TOKEN?
            1. First Get a look at Pexels Official Documentation. https://www.pexels.com/api/documentation/
            2. Then, Create a Pexels Account (if you don't have one already).
            3. Go to https://www.pexels.com/api/new/ and fill the form, after that, you will get your API Token.
            4. Provide the API Token to this class on instance Creation:

    .. code-block:: python

        from pexels_api import API
        API_TOKEN: str = "THIS_IS_AN_EXAMPLE_AND_INVALID_TOKEN_THIS_IS_AN_EXAMPLE_"
        Session = API(API_TOKEN)

    """

    PEXELS_AUTHORIZATION: dict = None
    """
    Pexels Credentials used on requests.
    this property is set by the __init__ method.
    """

    request: requests.models.Response = None
    """
    :ivar requests.models.Response request: Memory Storage of the Network Request.
        See `API.__request` for more information
    """

    json: dict = None
    """
    :ivar dict request: Json message from the request.
    see `API.__update_page_properties` for more information.
    """

    page: int = None
    """
    :ivar int page:
        Current page of the request.
        This is used by the search, cured and popular methods.

        see `API.__update_page_properties` for more information.
    """

    total_results: int = None
    """
    :ivar int total_results:
        Number of results from the search.
        see `API.__update_page_properties` for more information.
    """

    page_results: int = None
    """
    :ivar int page_results:
        Number of Photos in the request.

        see `API.__update_page_properties` for more information.
    """

    has_next_page = None
    """
    :ivar bool has_next_page:
        Defines wheter the search page has or not another page to look forwards.
        see `API.__update_page_properties` for more information.
    """

    has_previous_page = None
    """
    :ivar bool has_previous_page:
        Defines wheter the search page has or not another page to look backwards.
        see `API.__update_page_properties` for more information.
    """

    next_page = None
    """
    :ivar str next_page:
        Request URL for the Next Page.
        see `API.__update_page_properties` for more information.
    """

    prev_page = None
    """
    :ivar str prev_page:
        Request URL for the previous Page.
        see `API.__update_page_properties` for more information.
    """

    def __init__(self, PEXELS_API_KEY: str = ''):
        "Initializes the object."
        self.PEXELS_AUTHORIZATION = {"Authorization": PEXELS_API_KEY}
        self.request = None
        self.json = None
        self.page = None
        self.total_results = None
        self.page_results = None
        self.has_next_page = None
        self.has_previous_page = None
        self.next_page = None
        self.prev_page = None

    def search(self, query: str = "",
               results_per_page: int = 15,
               page: int = 1,
               orientation: str = "",
               size: int = None,
               color: str = None,
               locale: str = None):
        """
        Return json for the given query.

        GET https://api.pexels.com/v1/search

        :param str query:
            REQUIRED

            Keyword to search in pexels. all spaces will be converted in "+". instead of %20

        :param int results_per_page:
            OPTIONAL

            Defines how many results are going to appear by page.

            Defaults to `15` elements.

        :param int page:
            OPTIONAL

            Index of the page to look up.
            Defaults to start on page `1`.

        :param str orientation:
            OPTIONAL

            Orientation of the image, it can either be
                1. `"landscape"` wider then higher.
                1. `"portrait"` higher than wider.
                1. `"square"` wide and height are the same.

        :param int size:
            OPTIONAL

            Size of the image to look up.
                1. `"large"` >= 24MP
                1. `"medium"` >= 12MP
                1. `"small"` >= 4MP
            The size displayed will be an aproximation.

        :param str color:
            OPTIONAL

            Predominant coloration of the image.

            String Options can be:
                1. `"red"`
                1. `"orange"`
                1. `"yellow"`
                1. `"green"`
                1. `"turquoise"`
                1. `"blue"`
                1. `"violet"`
                1. `"pink"`
                1. `"brown"`
                1. `"black"`
                1. `"gray"`
                1. `"white"`

            `Color` also accepts RGB Hex colors:
                example: `#ffffff`


        :param str locale:
            OPTIONAL

            Location where the image has been taken.
            Supperted Locations:
                1. `"en-US"`
                1. `"pt-BR"`
                1. `"es-ES"`
                1. `"ca-ES"`
                1. `"de-DE"`
                1. `"it-IT"`
                1. `"fr-FR"`
                1. `"sv-SE"`
                1. `"id-ID"`
                1. `"pl-PL"`
                1. `"ja-JP"`
                1. `"zh-TW"`
                1. `"zh-CN"`
                1. `"ko-KR"`
                1. `"th-TH"`
                1. `"nl-NL"`
                1. `"hu-HU"`
                1. `"vi-VN"`
                1. `"cs-CZ"`
                1. `"da-DK"`
                1. `"fi-FI"`
                1. `"uk-UA"`
                1. `"el-GR"`
                1. `"ro-RO"`
                1. `"nb-NO"`
                1. `"sk-SK"`
                1. `"tr-TR"`
                1. `"ru-RU"`


        """
        if not query:
            PexelsInvalidQuery(f"Error invalid query {query}")
        query = query.replace(" ", "+")
        url = "https://api.pexels.com/v1/search?query={}&per_page={}&page={}".format(
            query, results_per_page, page)
        data_pattern: dict = {
            "per_page": "&per_page={}",
            "page": "&page={}",
            "orientation": "&orientation={}",
            "size": "&size={}",
            "color": "&color={}",
            "locale": "&locale={}",
        }
        if orientation != None or orientation == "":
            orientation = orientation.lower()
            if orientation in VALID_ORIENTATIONS:
                url += data_pattern["orientation"].format(orientation)
            else:
                raise PexelsInvalidQuery(
                    f"""Invalid Argument `orientation` on query. {orientation} not in {VALID_ORIENTATIONS}""")

        if size != None or size == "":
            size = size.lower()
            if size in VALID_ORIENTATIONS:
                url += data_pattern["size"].format(size)
            else:
                raise PexelsInvalidQuery(
                    f"""Invalid Argument `size` on query. {size} not in {VALID_SIZES}""")

        if color != None or color == "":
            color = color.lower()
            if color in VALID_COLOR_NAMES or color[0] == "#":
                url += data_pattern["color"].format(color)
            else:
                raise PexelsInvalidQuery(
                    f"""Invalid Argument `size` on query. {color} not in {VALID_COLOR_NAMES}""")
        if locale != None or locale == "":
            locale = locale.lower()
            if locale in VALID_LOCATIONS:
                url += data_pattern["locale"].format(locale)
            else:
                raise PexelsInvalidQuery(
                    f"""Invalid Argument `size` on query. {locale} not in {VALID_LOCATIONS}""")

        self.__request(url)
        # If there is no json data return None
        if self.request:
            return self.json
        raise PexelsInvalidQuery(
            f"Invalid Query, unable to search for ({query})")

    def popular(self, results_per_page: int = 15, page: int = 1):
        """
        Return json with popular photos of the current page.

        :param int results_per_page:
            OPTIONAL

            Defines how many results are going to appear by page.

            Defaults to `15` elements.

        :param int page:
            OPTIONAL

            Index of the page to look up.
            Defaults to start on page `1`.

        """
        url = "https://api.pexels.com/v1/popular?per_page={}&page={}".format(
            results_per_page, page)
        self.__request(url)
        # If there is no json data return None
        if self.request:
            return self.json
        raise PexelsInvalidQuery(
            "Invalid Query, unable to request Popular Photos list.")

    def curated(self, results_per_page: int = 15, page: int = 1):
        """
        Return json with curated photos of the current page.

        :param int results_per_page:
            OPTIONAL

            Defines how many results are going to appear by page.

            Defaults to `15` elements.

        :param int page:
            OPTIONAL

            Index of the page to look up.
            Defaults to start on page `1`.

        """
        url = "https://api.pexels.com/v1/curated?per_page={}&page={}".format(
            results_per_page, page)
        self.__request(url)
        # If there is no json data return None
        if self.request:
            return self.json
        raise PexelsInvalidQuery(
            "Invalid Query, unable to request Curated Photos list.")

    def search_next_page(self):
        """
        Return json of the next page if available.

        Uses API.__request to generate next page.
        Requires self.has_next_page to work.
        """
        if self.has_next_page:
            self.__request(self.next_page)
        else:
            return None
        # If there is no json data return None
        return None if not self.request else self.json

    def search_previous_page(self):
        """Return json of the previous page if available."""
        if self.has_previous_page:
            self.__request(self.prev_page)
        else:
            return None
        # If there is no json data return None
        return None if not self.request else self.json

    def get_entries(self) -> list[Photo]:
        """
        Return a list of photo objects.

        Returns all connent in self.json["photos"] as Photo Objects.
        """
        if not self.json:
            return None
        return [Photo(json_photo) for json_photo in self.json["photos"]]

    def __request(self, url: str = '') -> requests.models.Response:
        """
        Private method that manages requests to Pexels.

        :param url: str
            Url to request infomration
        """
        try:
            self.request = requests.get(
                url, timeout=15, headers=self.PEXELS_AUTHORIZATION)
            self.__update_page_properties()
            return self.request
        except requests.exceptions.RequestException as error:
            self.request = None
            raise PexelsConnectionClosed(
                "Unable to connect with Pexels Services. Please, Check your internect connection\n\t"
                "PARENT: 'requests.exceptions.RequestException'\n\t"
                f"TYPE  :{type(error)}\n\t"
                f"ERROR :{error}\n\t"
                f"TRACEBACK: {traceback.format_exc()}"
                )

    def __update_page_properties(self) -> bool:
        """
        Update the Session properties and page data.

        This method will add all properites from any kind of search method used.

        Will return `True` if the request was correct.
        """
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
                self.has_next_page = True
            except:
                self.next_page = None
                self.has_next_page = False
            try:
                self.prev_page = self.json["prev_page"]
                self.has_previous_page = True
            except:
                self.prev_page = None
                self.has_previous_page = False
            return True
        else:
            msg = (
                "Invalid Response from server or Token provided.\n\t"
                f"Request: {self.request}\n\t"
                f"API KEY: {self.PEXELS_AUTHORIZATION}"
            )
            self.request = None
            raise PexelsInvalidToken(msg)

    def get_photo_by_id(self, id: str = "") -> Photo:
        """
        Get a photo by it's Pexel's Image ID.

        GET https://api.pexels.com/v1/photos/:id

        ID needs to be an integer String.

        :param id: Union[str|int]
            ID of the image to request.

        see: `"https://www.pexels.com/api/documentation/#photos-show"` for more
        information.
        """
        try:
            url = "https://api.pexels.com/v1/photos/{}".format(id)
            self.__request(url)
            # If there is no json data return None
            if self.request:
                return Photo(self.json)
        except Exception as error:
            raise PexelsUnkownException(
                "Unknown Error.\n\t"
                f"TYPE  : {type(error)}\n\t"
                f"ERROR : {error}\n\t"
                f"traceback: {traceback.format_exc()}"
            )
        return None
