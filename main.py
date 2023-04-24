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
    PopupMenuItem,
    Icon,
    icons,
    IconButton,
    transform,
    animation,
)
import time

def main(page:Page):
    #title
    page.title = "Portfolio"

    def _on_page_resize(e):
        _nav.controls[0].visible = False if page.width <= 600 else True
        _min_nav_bar.visible = True if page.width <= 600 else False
        page.update()

    def _animate_social_media_buttons(e):
        _icon_text_.offset = transform.Offset(0, 0.05) if e.data == "true" else transform.Offset(0, -1.1)
        _icon_text_.opacity = 0 if e.data == "true" else 10
        _icon_text_.update()
        for btn in _social_buttons.controls[:]:
            btn.offset = transform.Offset(0, 0.15) if e.data == "true" else transform.Offset(0, -0.9)
            btn.opacity = 10 if e.data == "true" else  0
            btn.update()

    # delayed animated social media button         
    # import time
    # def _animate_social_media_buttons(e):
    #     if e.data == "true":
    #         _icon_text_.offset, _icon_text_.opacity = transform.Offset(0, 0.05), 0
    #         _icon_text_.update()
    #         for btn in _social_buttons.controls[:]:
    #             btn.offset, btn.opacity = transform.Offset(0, 0.15), 10 
    #             time.sleep(0.1)
    #             btn.update()
    #     else:
    #         for btn in _social_buttons.controls[:]:
    #             btn.offset, btn.opacity = transform.Offset(0, -0.9), 0
    #             btn.update()
    #             time.sleep(0.1)
    #         _icon_text_.offset, _icon_text_.opacity = transform.Offset(0, -1.1), 10
    #         _icon_text_.update()


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
                padding=20,
                content=Text('Welcome to my portfolio! \nHave a look around and contact me if you find anything interesting.', text_align='center', size=16, weight='w500')
            )
        ]
    )

    #social media buttons

    #icons list

    _icons_list = [icons.FACEBOOK,icons.SHARE_SHARP,icons.EMAIL_SHARP] 

    _social_buttons = Row(
            alignment='center',
            vertical_alignment='center',
        )

    _icon_text_ = Text(
        'Connect!',
        size=16,
        color='white',
        weight='w800',
        offset=transform.Offset(0, -1.1),
        animate_offset=animation.Animation(duration=1000, curve='elasticOut'),
        animate_opacity=10,

    )

    for icon in _icons_list:
        _icon = IconButton(
            icon=icon,
            icon_size=22,
            icon_color="white",
            offset=transform.Offset(0, -0.9),
            animate_offset=animation.Animation(duration=1000, curve='elasticOut'),
            animate_opacity=10,
            opacity=0,
        )

        _social_buttons.controls.append(_icon)

    _icon_container = Container(
        width=145,
        height=50,
        bgcolor='blue800',
        border_radius=8,
        alignment=alignment.center,
        on_hover = lambda e: _animate_social_media_buttons(e),
        content=Column(
            spacing=0,
            alignment='center',
            horizontal_alignment='center',
            controls=[
                _social_buttons,
                Row(
                    alignment='center',
                    controls=[
                        _icon_text_
                    ]
                )
            ]
        )
    )

    #portfolio grid responsive
    _items = ["1", "2", "3", "4", "5", "6", "7", "8"]

    _item_row = ResponsiveRow(alignment='start')
    _container_item = Container(
        padding=20,
        content=_item_row,
    )

    for item in _items:
        _item_container = Container(
            width=300, height=300, bgcolor='white', padding=35, border_radius=12, alignment=alignment.center, aspect_ratio=1,
            col={'xs':12, 'sm':4, 'md':4, 'lg':6, 'xl':4},
            content=
                Container(
                    bgcolor='black', border_radius=8, alignment=alignment.center, aspect_ratio=1,
                    content=Text(f'{item}', size=21),
                ),
        )
        _item_row.controls.append(_item_container)

    #main_column    
    _main_col = Column(horizontal_alignment='center', scroll='auto')
    _main_col.controls.append(_nav)
    _main_col.controls.append(_min_nav_bar)
    _main_col.controls.append(_titles)
    _main_col.controls.append(_sub_title)
    _main_col.controls.append(Container(padding=padding.only(top=10)))
    _main_col.controls.append(_icon_container)
    _main_col.controls.append(Container(padding=padding.only(bottom=40)))
    _main_col.controls.append(_container_item)

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
    # flet.app(target=main, view=flet.WEB_BROWSER)
