from flet import (
    flet, 
    Page, 
    Column, 
    Row, 
    alignment, 
    padding, 
    ResponsiveRow, border, 
    Container, 
    Text, 
    margin, 
    LinearGradient,
    PopupMenuButton,
    PopupMenuItem
)

def main(page:Page):
    #title
    page.title = "Portfolio"

    def _on_page_resize(e):
        _nav.controls[0].visible = False if page.width <= 600 else True
        _min_nav_bar.visible = True if page.width <= 600 else False
        page.update()


    def _change_text_colour(e):
        e.control.content.color = '#475569' if e.control.content.color == 'white' else 'white'
        e.control.content.update() 

        # if e.control.content.color == 'black':
        #     e.control.content.color = 'blue800'
        #     e.control.content.update() 
        # else:
        #     e.control.content.color = 'black'
        #     e.control.content.update() 

    #navbar
    _nav = Row(
        alignment="end",
        controls=[
            Container(
                padding=padding.only(right=20),
                height=64,
                content=Row(
                    controls=[
                        Container(
                            on_hover=lambda e: _change_text_colour(e),
                            content=Text('About Me', weight='w600', color='white')),
                        Container(
                            on_hover=lambda e: _change_text_colour(e),
                            content=Text('Contact', weight='w600', color='white')),
                        Container(
                            on_hover=lambda e: _change_text_colour(e),
                            content=Text('Services', weight='w600', color='white'),)
                    ]
                )
            )
        ]
    )

    #minmized nav bar
    _min_nav_bar = Row(
        visible=False,
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="About Me"),
                    PopupMenuItem(text="Contact"),
                    PopupMenuItem(text="Services")
                ]
            )
        ]
    )

    #titles
    _titles = ResponsiveRow(
        alignment='center', 
        controls=[
            Container(
                col={'xs':12, 'sm':10, 'md':10, 'lg':10, 'xl':12},
                alignment=alignment.top_center,
                padding=padding.only(top=20),
                content=Text('Line Indent\n Portfolio & Projects', size=45, weight='w600', text_align='center',)
            )
        ]
    )
    
    #sub_title
    _sub_title = ResponsiveRow(
        alignment='center', 
        controls=[
            Container(
                col={'xs':12, 'sm':10, 'md':10, 'lg':10, 'xl':12},
                alignment=alignment.top_center,
                padding=padding.only(top=20),
                content=Text('Welcome to my portfolio! \nHave a look around and contact me if you find anything interesting.', text_align='center', size=16, weight='w500')
            )
        ]
    )

    #main_column
    _main_col = Column()
    _main_col.controls.append(_nav)
    _main_col.controls.append(_min_nav_bar)
    _main_col.controls.append(_titles)
    _main_col.controls.append(_sub_title)

    #background container
    _background = Container(
        height=page.height,
        expand=True,
        margin=-10, 
        gradient=LinearGradient(
            begin=alignment.bottom_left, end=alignment.top_right, colors=['#13547a','#0f172a']
            ),
        content=_main_col,
        )
    
    page.add(_background)

    #resize
    page.on_resize = _on_page_resize

if __name__ == "__main__":
    flet.app(target=main)