
AUTHOR = 'Honza & Zuzka'
SITENAME = 'Pražení'


# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'
DEFAULT_LANG = 'cs'
DEFAULT_DATE_FORMAT = '%x'


# Blog settings
PATH = 'content'
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 80
DEFAULT_CATEGORY = 'blog'
MD_EXTENSIONS = ['headerid', 'extra']


# URL and save paths settings
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
URL_EXT = ''
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'


# Static paths will be copied under the same name
STATIC_PATHS = (
    'images',
    'files',
    'robots.txt',
    'favicon.ico',
    'CNAME',
)


# Generating
DELETE_OUTPUT_DIRECTORY = True


# Feeds
FEED_ALL_ATOM = 'feed.xml'
FEED_MAX_ITEMS = 50


CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
