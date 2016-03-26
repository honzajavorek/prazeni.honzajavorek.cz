
import platform

from danube_delta.settings import *  # NOQA


# Authors
AUTHOR = 'Zuzka & Honza'
ABOUT_HEADING = AUTHOR

SITENAME = 'Pražení'
SITESUBTITLE = 'Nežít Brno'

ABOUT = '''
V roce 2014 jsme se odstěhovali z Brna do Prahy. Trauma z toho máme tak silné,
že jsme si v rámci terapie založili tenhle blog o tom, jak se s tím
vyrovnáváme. Naši kámoši v Brně ho čtou a ťukaj si na čelo.
'''
ABOUT_IMAGE = 'images/about.jpg'


# Production settings
if PRODUCTION:
    SITEURL = 'http://prazeni.honzajavorek.cz'


# Default author
if platform.system() == 'Darwin':
    DEFAULT_AUTHOR = 'Honza'
elif platform.system() == 'Windows':
    DEFAULT_AUTHOR = 'Zuzka'
else:
    DEFAULT_AUTHOR = AUTHOR


# Theming
DISQUS_SITENAME = 'prazeni'
GOOGLE_ANALYTICS = 'UA-1316071-18'
GOOGLE_FONTS = ['PT Sans', 'Wellfleet']
