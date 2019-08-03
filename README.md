# Using Pexels API v1 with Python
Use *[pexels_api][2]* to search photos from [Pexels][0].
## Dependencies:
- requests

## Installation:
`pip install pexels-api`

## Usage:
The following code shows you how to import the package and make a simple query to Pexels API v1. See more [examples][15] or the [documentation][16].
```python
# Import API class from pexels_api package
from pexels_api import API
# Type your Pexels API
PEXELS_API_KEY = 'YOUR-PEXELS-API-KEY'
# Create API object
api = API(PEXELS_API_KEY)
# Search five 'kitten' photos
api.search('kitten', page=1, results_per_page=5)
# Get photo entries
photos = api.get_entries()
# Loop the five photos
for photo in photos:
  # Print photographer
  print('Photographer: {}'.format(photo.photographer))
  # Print url
  print('Photo url: {}'.format(photo.url))
  # Print original size url
  print('Photo original size: {}'.format(photo.original))
```
## Examples:
- *[search.py:][3]*  
Specify a query to search photos.
- *[popular.py:][4]*  
Search popular photos.
- *[curated.py:][5]*  
Search curated photos.
- *[download.py:][6]*  
Download large amounts of photos with a query.

## Documentation:
- [Usage: pexels_api][7]
- [Class: API][7]
    - [Methods][8]
    - [Properties][9]
- [Class: Photo][10]
    - [Properties][11]

## Class: API
#### `API(PEXELS_API_KEY)`  
Creates an instance of a *[API][7]* object.

|Parameter|Required|Type|Description|
|:-|:-|:-|:-|
|PEXELS_API_KEY |Yes|String|Your Pexels API key|
##### Returns:
An instance of a *[API][7]* object.
### Methods:
#### `search(query, photos_per_page=15, page=1)`  
Given a query requests data using Pexels API v1.

|Parameter|Required|Type|Description|
|:-|:-|:-|:-|
|query          |Yes|String|The topic to search|
|photos_per_page|No. *(Default value: 15)*|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No. *(Default value: 1)*|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of the query in the specified page, `None` if the request fails.  

#### `popular(photos_per_page=15, page=1)`  
Requests popular data using Pexels API v1.

|Parameter|Required|Type|Description|
|:-|:-|:-|:-|
|photos_per_page|No. *(Default value: 15)*|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No. *(Default value: 1)*|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of Pexels popular page in the specified page, `None` if the request fails.  
#### `curated(photos_per_page=15, page=1)`  
Requests curated data using Pexels API v1.

|Parameter|Required|Type|Description|
|:-|:-|:-|:-|
|photos_per_page|No. *(Default value: 15)*|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No. *(Default value: 1)*|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of Pexels curated page in the specified page, `None` if the request fails.  
#### `search_next_page()`
Search the next page if available.  
##### Returns:
A dictionary containing json data of the next page, `None` if page not found.
#### `search_previous_page()`
Search the previous page if available.  
##### Returns:
A dictionary containing json data of the previous page, `None` if page not found.
#### `get_entries()`
Creates an instance of a *[Photo][10]* object for each photo in the current page.  
##### Returns:
A list of *[Photo][10]* objects.
### Properties:
By default the *[API][7]* properties are `None`. When *[seacrh()][12]*, *[popular()][13]* or *[curated()][14]* is performed the *[API][7]* properties are updated.  

|Property|Type|Description|
|:-|:-|:-|
|request|[requests][1] object|Current request, `None` if request fails|
|json|Dictionary|A dictionary with the data of the current page|  
|page|Integer|Number of the page|  
|total_results|Integer|Number of total results. (`None` in *popular* and *curated* page)|
|page_results|Integer|Number of results in the current page|  
|has_next_page|Boolean|`True` if there is a next page else `False`|
|has_previous_page|Boolean|`True` if there is a previous page else `False`|
|next_page|String|Url to the next page. (`None` if there is no next page)|
|prev_page|String|Url to the previous page. (`None` if there is no previous page)|

## Class: Photo
#### `Photo(json_photo)`
| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|json_photo |Yes|Dictionary|A dictionary containing json data of the photo of which you want the properties|

##### Returns:
An instance of a *[Photo][10]* object.
### Properties:
|Property|Type|Description|
|:-|:-|:-|
|id|Integer|Unique Pexels identifier|
|width|Integer|Width of the original photo|
|height|Integer|Height of the original photo|
|photographer|String|Photo's photographer|
|url|String|Photo's photographer|
|description|String|Photo's description|
|original|String|Photo's original size url|
|compressed|String|Photo's compressed size url|
|large2x|String|Photo's large2x size url|
|large|String|Photo's large size url|
|medium|String|Photo's medium size url|
|small|String|Photo's small size url|
|portrait|String|Photo's portrait size url|
|landscape|String|Photo's landscape size url|
|tiny|String|Photo's tiny size url|
|extension|String|Photo's extension|

<!-- References -->
[0]: https://pexels.com                        "Pexels website"
[1]: https://2.python-requests.org/en/master/  "Documentation: requests"
<!-- Documentation -->
[2]: /pexels_api                               "pexels_api package"
[3]: /examples/search.py                       "Using pexels_api to search photos"
[4]: /examples/popular.py                      "Using pexels_api to search popular photos"
[5]: /examples/curated.py                      "Using pexels_api to search curated photos"
[6]: /examples/download.py                     "Using pexels_api to download large amounts of photos"
[7]: #class-api                                "Class: API"
[8]: #methods                                  "API: methods"
[9]: #properties                               "API: properties"
[10]: #class-photo                             "Class: Photo"
[11]: #properties-1                            "Photo: properties"
[12]: #searchquery-photos_per_page15-page1     "API method: search"
[13]: #popularphotos_per_page15-page1          "API method: popular"
[14]: #curatedphotos_per_page15-page1          "API method: curated"
[15]: #examples                                "More pexels_api examples"
[16]: #documentation                           "pexels_api documentation"
