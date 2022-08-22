# Author:           Voltaic314
# Pexels Website:   https://www.pexels.com
## This class is for the sole purpose of parsing json info from Pexels to get video links for nature poster script. 
## Feel free to use this however you want, but I did cut out a lot of other things that you could use maybe if you have other purposes. 
## for the link on where I got this info, check out the pexels api docs here: https://www.pexels.com/api/documentation/ 
## if the above link is dead, just search "pexels api documentation" and you'll probalby find it. 
## if any of you have specific questions on how I did this, I encourage you to learn more about how objects and classes work in Python as well as JSON parsing. 

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
        return self.url.split("/")[-2].replace("-{}".format(self.id), "")
    @property
    def duration(self):
      return self.__video["duration"]
