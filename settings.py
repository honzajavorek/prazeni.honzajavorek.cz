
import platform

from danube_delta.settings import *  # NOQA


AUTHOR = 'Zuzka & Honza'
SITENAME = 'Pražení'
SITESUBTITLE = 'Nežít Brno'

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
