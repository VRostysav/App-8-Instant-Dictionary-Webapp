import justpy as jp


class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view='hHh lpR fFf')
        header = jp.Header(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model=True, side='left',
                            border=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg  text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/home', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu',
                clikc=cls.move_drawer, drawer=drawer)

        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')
        page_container = jp.QPageContainer(a=layout)
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

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value=True

