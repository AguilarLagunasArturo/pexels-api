# Author:           Voltaic314
# Pexels Website:   https://www.pexels.com
## This class is for the sole purpose of parsing json info from Pexels to get video links.
## Feel free to use this however you want, but I did cut out a lot of other things that you could use maybe if you have other purposes. 
## for the link on where I got this info, check out the pexels api docs here: https://www.pexels.com/api/documentation/ 

class Video:
    def __init__(self, json_video):
        self.__video = json_video
        
    @property
    def id(self):
        return int(self.__video["id"])
    
    @property
    def width(self):
        return int(self.__video["width"])
    
    @property
    def height(self):
        return int(self.__video["height"])
    
    @property
    def videographer(self):
        return self.__video["user"]["name"]
    
    @property
    def url(self):
        return self.__video["url"]
    
    @property
    def description(self):
        return self.url.split("/")[-2].replace(f"-{self.id}", "").replace("-", " "))
    
    @property
    def duration(self):
      return self.__video["duration"]

    @property
    def highest_resolution_video(self):
        # Since each video will always have the same aspect ratio, just different resolutions....
        # It really doesn't matter whether we sort by width or height here, we're just looking for the 
        # highest number. 
        return (max(l, key=lambda x: x['videos']['video_files']['width']))
        
    @property
    def highest_resolution_width(self):
        return int(self.highest_resolution_video['width'])
    
    @property
    def highest_resolution_height(self):
        return int(self.highest_resolution_video['height'])

    @property
    def link(self):
        return self.highest_resolution_video['link']
