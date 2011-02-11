from django.template import TemplateDoesNotExist
from django.template.loader import BaseLoader
from jingo import env
import jinja2

class Loader(BaseLoader):
    """
    A file system and app directory loader for Jinja2.
    """
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        try:
            template = env.get_template(template_name)
            return template, template.filename
        except jinja2.TemplateNotFound:
            pass
        raise TemplateDoesNotExist(template_name)

