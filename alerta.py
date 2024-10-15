import flet as ft

def main(page: ft.Page):
    ad1 = ft.AlertDialog(
        title=ft.Text(value='Aviso importante!'),
        content=ft.Text(value="Isso é uma alerta!"),
        content_padding=ft.padding.all(30),
        inset_padding=ft.padding.all(10),
        modal=False,
        shape=ft.RoundedRectangleBorder(radius=5),
        on_dismiss=lambda e: print("Alerta foi fechado"),
    )
    page.dialog = ad1
    ad1.open = True
    page.update()

    if __name__ == "__main__":
        ft.app(target=main)

   
