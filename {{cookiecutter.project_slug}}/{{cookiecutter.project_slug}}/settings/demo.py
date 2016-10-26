import datetime

from ..settings import *


class Site(Site):
    """Defines and instantiates a demo version of {{ cookiecutter.project_slug }}."""

    the_demo_date = datetime.date(2015, 5, 23)

    languages = "en de fr"



SITE = Site(globals())