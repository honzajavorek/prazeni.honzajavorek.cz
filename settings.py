
import platform

from danube_delta.settings import *  # NOQA


AUTHOR = 'Zuzka & Honza'
SITENAME = 'Pražení'

if PRODUCTION:
    SITEURL = 'http://prazeni.honzajavorek.cz'


# Default author
if platform.system() == 'Darwin':
    DEFAULT_AUTHOR = 'Honza'
elif platform.system() == 'Windows':
    DEFAULT_AUTHOR = 'Zuzka'
else:
    DEFAULT_AUTHOR = AUTHOR
