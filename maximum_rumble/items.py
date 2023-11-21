# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChannelItem(scrapy.Item):
    channel_name = scrapy.Field()
    channel_is_verified = scrapy.Field()
    number_of_followers = scrapy.Field()
    videos_urls = scrapy.Field()

class VideoItem(scrapy.Item):
    video_title = scrapy.Field()
    video_url = scrapy.Field()
    date = scrapy.Field()
    views = scrapy.Field()
    likes = scrapy.Field()
    dislikes = scrapy.Field()
    recommended_videos = scrapy.Field()
    recommended_videos_channels_name = scrapy.Field()
