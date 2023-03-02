from WebApp.About_Page import About
from WebApp.Home_Page import Home
import justpy as jp

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)

jp.justpy(port=5354)

