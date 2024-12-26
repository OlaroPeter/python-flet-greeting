import flet as 

def main(page: ft.Page):
    def on_button_click(e):
        output.value = f"Hello, {name_field.value}!"
        page.update()

    name_field = ft.TextField(label="Enter your name")
    output = ft.Text(value="")
    greet_button = ft.ElevatedButton(text="Greet", on_click=on_button_click)

    page.add(name_field, greet_button, output)

ft.app(target=main)
