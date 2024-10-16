import flet as ft
from button import app_button


def project_cell(name, logo_src, pull_time):
    cell = ft.Container(
        content=ft.Column(
            [
                ft.Image(src=logo_src, width=48, height=48, border_radius=8),
                ft.Column(
                    [
                        ft.Text(value=name, size=12, weight=ft.FontWeight.BOLD),
                        ft.Text(value=pull_time, color=ft.colors.with_opacity(0.3, '#000000'),
                                weight=ft.FontWeight.NORMAL),
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                app_button(1, '安装', '')
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        ),
        expand=True,
        # height=174,
        padding=16,
        bgcolor='#ffffff',
        border_radius=8,
    )
    return cell


def project_list(page, visible):
    page = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        project_cell('ChatChill', f'images/project_logo/ChatChill.png', '17：19'),
                        project_cell('ChatChill', f'images/project_logo/ChatChill.png', '17：19'),
                        project_cell('ChatChill', f'images/project_logo/ChatChill.png', '17：19'),
                    ],
                    # expand=True,
                ),
            ]
        ),
        # bgcolor='#123456',
        expand=True,
        border_radius=8,
        # height=page.height,
        visible=visible,
    )

    return page
