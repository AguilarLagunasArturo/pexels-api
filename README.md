# Using Pexels API v1
Use *[pexels.py][2]* to search photos from [Pexels][0].
## Examples:
- *[search.py:][3]*  
Specify a query to search photos.
- *[pupular.py:][4]*  
Search popular photos.
- *[curated.py:][5]*  
Search curated photos.
- *[download.py:][6]*  
Download large amounts of photos with a query.

## Prerequisites:
- git
- python
    - requests

## Installation:
`git clone https://github.com/AguilarLagunasArturo/pexels-api.git`
## Documentation:
- [Class: page][7]
    - [Methods][8]
    - [Properties][9]
- [Class: photo][10]
    - [Methods][11]
    - [Properties][12]

## Class: page
#### `page(PEXELS_API_KEY)`  
Creates an instance of a *[page][7]* object.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|PEXELS_API_KEY |Yes|String|Your Pexels API key|
##### Returns:
An instance of a *[page][7]* object.
### Methods:
#### `page.search(query, photos_per_page=15, page=1)`  
Given a query requests data using Pexels API v1.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|query          |Yes|String|The topic to search|
|photos_per_page|No|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of the query in the specified page, `None` if the request fails.  

#### `page.popular(photos_per_page=15, page=1)`  
Requests popular data using Pexels API v1.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|photos_per_page|No|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of Pexels popular page in the specified page, `None` if the request fails.  
#### `page.curated(photos_per_page=15, page=1)`  
Requests curated data using Pexels API v1.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|photos_per_page|No|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of Pexels curated page in the specified page, `None` if the request fails.  
#### `page.search_next()`
Search the next page if available.  
##### Returns:
A dictionary containing json data of the next page, `None` if page not found.
#### `page.search_previous()`
Search the previous page if available.  
##### Returns:
A dictionary containing json data of the previous page, `None` if page not found.
#### `page.get_entries()`
Creates an instance of a *[photo][10]* object for each photo in the current page.  
##### Returns:
A list of *[photo][10]* objects.
### Properties:
By default the *[page][7]* properties are `None`. When *[page.seacrh()][13]*, *[page.popular()][14]*, *[page.curated()][15]* is performed the *[page][7]* properties are updated.
- #### page.request:
A *[requests][1]* object.  
*__Note:__*  `None` if request fails.
- #### page.json:
A dictionary with the data of the current page.  
- #### page.page:
Integer, number of the page.  
- #### page.total_results:
Integer, number of total results.  
*__Note:__*  `None` in *popular* or *curated* page.
- #### page.page_results:
Integer, number of results in the current page.  
*__Note:__*  `None` in *popular* or *curated* page.
- #### page.has_next:
`True` if there is a next page else `False`.
- #### page.has_prev:
`True` if there is a previous page else `False`.
- #### page.next_page:
Url to the next page.  
*__Note:__*  `None` if there is no next page.
- #### page.prev_page:
Url to the previous page.  
*__Note:__*  `None` if there is no previous page.

## Class: photo
#### `photo(json_photo)`
| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|json_photo |Yes|Dictionary|A dictionary containing json data of the photo of which you want the properties|

##### Returns:
An instance of a *[photo][10]* object.
### Methods:
### Properties:
- #### photo.id:
Integer, unique Pexels identifier.
- #### photo.width:
Integer, width of the original photo.
- #### photo.height:
Integer, height of the original photo.
- #### photo.photographer:
String, containing photo's photographer.
- #### photo.url:
String, containing photo's photographer.
- #### photo.description:
String, containing photo's description.
- #### photo.original:
String, containing photo's original size url.
- #### photo.compressed:
String, containing photo's compressed size url.
- #### photo.large2x:
String, containing photo's large2x size url.
- #### photo.large:
String, containing photo's large size url.
- #### photo.medium:
String, containing photo's medium size url.
- #### photo.small:
String, containing photo's small size url.
- #### photo.portrait:
String, containing photo's portrait size url.
- #### photo.landscape:
String, containing photo's landscape size url.
- #### photo.tiny:
String, containing photo's tiny size url.
- #### photo.extension:
String, containing photo extension.

<!-- References -->
[0]: https://pexels.com                         "Pexels website"
[1]: https://2.python-requests.org/en/master/   "requests documentation"
<!-- Documentation -->
[2]: /src/pexels.py                            "pexels.py"
[3]: /search.py                                "Using pexels.py to search photos"
[4]: /pupular.py                               "Using pexels.py to search popular photos"
[5]: /curated.py                               "Using pexels.py to search curated photos"
[6]: /download.py                              "Using pexels.py to download large amounts of photos"
[7]: #class-page                               "Class page"
[8]: #methods                                  "page methods"
[9]: #properties                               "page properties"
[10]: #class-photo                             "Class photo"
[11]: #methods-1                               "photo methods"
[12]: #properties-1                            "photo properties"
[13]: #pagesearchquery-photos_per_page15-page1 "page: search method"
[14]: #pagepopularresults_per_page15-page1     "page: popular method"
[15]: #pagecuratedresults_per_page=15-page1    "page: curated method"
[16]: #searchnext                              "page: search_next method"
[17]: #searchprevious                          "page: search_previous method"
[18]: #getentries                              "page: get_entries method"
