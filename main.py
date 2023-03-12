import inspect

from WebApp.About_Page import About
from WebApp.Home_Page import Home
from WebApp.DictionaryPage import Dictionary
import justpy as jp
from WebApp import page

imports = list(globals().values())
for object in imports:
    if inspect.isclass(object):
        if issubclass(object, page.Page) and object is not page.Page:
            jp.Route(object.path, object.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=5354)
