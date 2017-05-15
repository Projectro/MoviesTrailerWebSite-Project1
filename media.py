#######################################################
# Using short name so the code doesnt look messy
#
# TN = Title Name
# TD = Total Duration
# SL = Story Line
# PIU = Poster Image URL
# YTU = Youtube Trailer URL
########################################################

class Video():
    def __init__(self, title_name, total_duration):
        self.title = title_name
        self.duration = total_duration

class Movie(Video):
    def __init__(self, title_name, total_duration, story_line, poster_image_url, youtube_trailer_url):
        Video.__init__(self, title_name, total_duration)
        self.StoryLine = story_line
        self.PosterImageURL = poster_image_url
        self.YoutubeTrailerURL = youtube_trailer_url

# class TVshow(Video):
#     def __init__(self, T, D, SL, PIU, YTU)
