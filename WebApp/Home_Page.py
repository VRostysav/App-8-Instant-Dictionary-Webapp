import justpy as jp
from WebApp import layout
from WebApp import page


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        page_container = jp.QPageContainer(a=lay)

        div = jp.Div(a=page_container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page',
               classes='text-4xl m-2')
        jp.Div(a=div, text="""
        It is a long established fact that a reader will be distracted 
        by the readable content of a page when looking at its layout. 
        The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, 
        as opposed to using 'Content here, content here', making it look like readable English. 
        Many desktop publishing packages and web page editors now use Lorem Ipsum 
        as their default model text, and a search for 'lorem ipsum' will uncover 
        many web sites still in their infancy. Various versions have evolved over the years, 
        sometimes by accident, sometimes on purpose (injected humour and the like).
        """, classes='text-lg')
        return wp



