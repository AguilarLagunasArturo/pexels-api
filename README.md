# Using Pexels API v1
Use *[pexels.py](/src/pexels.py)* to search photos from [Pexels](https://pexels.com)
## Examples:
- *[search.py:](/src/search.py)*  
Specify a query to search
- *[pupular.py:](/src/pupular.py)*  
Search popular photos
- *[curated.py:](/src/curated.py)*  
Search curated photos
- *[download.py:](/src/download.py)*  
Download large amounts of photos with a query

## Prerequisites:
- git
- python
    - requests

## Installation:
git clone <https://github.com/AguilarLagunasArturo/pexels-api.git>

## Documentation:
- [Class: page](#class-page)
    - [Methods](#methods)
    - [Properties](#properties)
- [Class: photo](#class-photo)
    - [Methods](#methods-1)
    - [Properties](#properties-1)

## Class: page
#### `page(PEXELS_API_KEY)`  
Creates an instance of a *page* object.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|PEXELS_API_KEY |Yes|String|Your Pexels API key|
##### Returns:
An instance of a *page* object.
### Methods:
#### `page.search(query, photos_per_page=15, page=1)`  
Given a query requests data to Pexels API v1.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|query          |Yes|String|The topic to search|
|photos_per_page|No|Integer|Number of photos per page 1 minimum 80 maximum *__Note: Default value 15__*|
|page           |No|Integer|Specify the page to search *__Note: Default value 1__*|
##### Returns:
A dictionary containing json data of the results of the query in the specified page, `None` if the request fails.  

#### `page.popular(photos_per_page=15, page=1)`  
Requests popular data from Pexels API v1.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|photos_per_page|No|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of Pexels' popular page in the specified page, `None` if the request fails.  
#### `page.curated(photos_per_page=15, page=1)`  
Requests curated data from Pexels API v1.

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|photos_per_page|No|Integer|Number of photos per page 1 minimum 80 maximum|
|page           |No|Integer|Specify the page to search|
##### Returns:
A dictionary containing json data of the results of Pexels' curated page in the specified page, `None` if the request fails.  
#### `page.search_next()`
Search the next page if available.  
##### Returns:
A dictionary containing json data of the next page, `None` if page not found.
#### `page.search_previous()`
Search the previous page if available.  
##### Returns:
A dictionary containing json data of the previous page, `None` if page not found.
#### `page.get_entries()`
Creates an instance of a *[photo](#class-photo)* object for each photo in the current page.  
##### Returns:
A list of *[photo](#class-photo)* objects.
### Properties:
- #### page.request:
A *[requests][0]* object.  
*__Note:__*  `None` if request fails.
- #### page.json:
A dictionary with the data of the current page.  
*__Note:__*  `None` if request fails.
- #### page.page:
Integer, number of the page
- #### page.total_results:
Integer, total results.  
*__Note:__*  `None` in *popular* or *curated* page.
- #### page.page_results:
Integer, results in the current page  
*__Note:__*  `None` in *popular* or *curated* page.
- #### page.has_next:
`True` if there is a next page else `False`
- #### page.has_prev:
`True` if there is a previous page else `False`
- #### page.next_page:
Url to the next page.  
*__Note:__*  `None` if there is no next page.
- #### page.prev_page:
Url to the previous page.  
*__Note:__*  `None` if there is no previous page.
___
## Class: photo
```python
photo(json_photo)
```

| Parameter     | Required |Type  | Description     |
| :------------ | :- |:---- | :------------- |
|json_photo |Yes|Dictionary|A dictionary containing json data of the photo of which you want the properties|

##### Returns:
An instance of a *photo* object.
### Methods:
### Properties:
- #### photo.id:
~descrption  
- #### photo.width:
~descrption  
- #### photo.height:
~descrption  
- #### photo.photographer:
~descrption  
- #### photo.url:
~descrption  
- #### photo.description:
~descrption  
- #### photo.src:
~descrption  
- #### photo.original:
~descrption  
- #### photo.compressed:
~descrption  
- #### photo.large2x:
~descrption  
- #### photo.large:
~descrption  
- #### photo.medium:
~descrption  
- #### photo.small:
~descrption  
- #### photo.portrait:
~descrption  
- #### photo.landscape:
~descrption  
- #### photo.tiny:
~descrption  
- #### photo.extension:
~descrption

```python
import os
os.path.isdir("/")
page(PEXELS)
print(page.total_results)
```

[0]: https://2.python-requests.org/en/master/ "requests"
