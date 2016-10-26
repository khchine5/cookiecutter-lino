# -*- coding: UTF-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "{{ cookiecutter.project_name }}"
    version = '{{cookiecutter.version}}'

    url = "{{cookiecutter.domain_name}}"
    server_url = "{{cookiecutter.domain_name}}"

    demo_fixtures = ['std', 'demo', 'demo2']

    # project_model = 'tickets.Project'
    textfield_format = 'html'
    # user_types_module = 'lino_noi.lib.noi.roles'
    obj2text_template = "**{0}**"

    default_build_method = 'appyodt'
    migration_class = 'lino_noi.lib.noi.migrate.Migrator'