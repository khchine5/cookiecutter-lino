# -*- coding: UTF-8 -*-

from lino.api import ad, _


class Plugin(ad.Plugin):
    "See :class:`lino.core.plugin.Plugin`."
    verbose_name = _("{{ cookiecutter.project_name }}")
