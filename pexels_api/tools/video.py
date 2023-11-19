# Author:           Logan Maupin
# Pexels Website:   https://www.pexels.com
# class information:
#     Get json data from https://www.pexels.com
#     Search videos using Pexels API
# Dependencies:
#     requests

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
    def image_preview(self):
        return self.__video['image']

    @property
    def description(self):
        return self.url.split("/")[-2].replace(f"-{self.id}", "").replace("-", " ")

    @property
    def duration(self):
        return self.__video["duration"]

    @property
    def highest_resolution_video(self):
        # Since each video will always have the same aspect ratio, just different resolutions....
        # It really doesn't matter whether we sort by width or height here, we're just looking for the
        # highest number.
        highest_resolution_video_dict = {}
        for dictionary in self.__video["video_files"]:
            if not highest_resolution_video_dict:
                highest_resolution_video_dict = dictionary
            else:
                if dictionary["width"] > highest_resolution_video_dict["width"]:
                    highest_resolution_video_dict = dictionary
        return highest_resolution_video_dict

    @property
    def highest_resolution_width(self):
        return int(self.highest_resolution_video['width'])

    @property
    def highest_resolution_height(self):
        return int(self.highest_resolution_video['height'])

    @property
    def link(self):
        return self.highest_resolution_video['link'].split("&")[0]

    @property
    def extension(self):
        return self.highest_resolution_video['file_type'].split("/")[-1]
