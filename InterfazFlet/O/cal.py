import flet as ft

def main(page:ft.Page):

    def binario(e):
        if dd1.value == "BINARIO" and dd2.value == "BINARIO":
            salida.value = entrada.value
        elif dd1.value == "BINARIO" and dd2.value == "TERNARIO":
            pos = len(entrada)
            dec = 0
            for i in reversed(enter):
                if i == "1":
                    dec = dec + pow(2,(len(entrada) - pos))
                pos = pos - 1
            n = dec
            nums = []
            while n:
                n, r = divmod(n, 3)
                nums.append(str(r))
            salida.value = ''.join(reversed(nums))
            page.update()
        elif dd1.value == "BINARIO" and dd2.value == "CUATERNARIO":
            pos = len(entrada)
            dec = 0
            for i in reversed(enter):
                if i == "1":
                    dec = dec + pow(2,(len(entrada) - pos))
                pos = pos - 1
            n = dec
            nums = []
            while n:
                n, r = divmod(n, 4)
                nums.append(str(r))
            salida.value = ''.join(reversed(nums))
            page.update()
        elif dd1.value == "BINARIO" and dd2.value == "OCTAL":
            pos = len(entrada)
            dec = 0
            for i in reversed(enter):
                if i == "1":
                    dec = dec + pow(2,(len(entrada) - pos))
                pos = pos - 1
            salida.value = oct(int(dec))[2::]
            page.update()
        elif dd1.value == "BINARIO" and dd2.value == "DECIMAL":
            enter = entrada.value
            pos = len(entrada)
            dec = 0
            for i in reversed(enter):
                if i == "1":
                    dec = dec + pow(2,(len(entrada) - pos))
                pos = pos - 1
            salida.value = str(dec)
            page.update()
        elif dd1.value == "BINARIO" and dd2.value == "HEXADECIMAL":
            pos = len(entrada)
            dec = 0
            for i in reversed(enter):
                if i == "1":
                    dec = dec + pow(2,(len(entrada) - pos))
                pos = pos - 1
            salida.value = hex(int(dec))[2::]
            page.update()

    def ternario(e):
        if dd1.value == "TERNARIO" and dd2.value == "DECIMAL":
            
            
    def decimal(e):
        if dd1.value == "DECIMAL" and dd2.value == "BINARIO":
            salida.value = bin(int(entrada.value))[2::]
            page.update()
        elif dd1.value == "DECIMAL" and dd2.value == "TERNARIO":
            n = salida.value
            nums = []
            while n:
                n, r = divmod(n, 3)
                nums.append(str(r))
            salida.value = ''.join(reversed(nums))
            page.update()
        elif dd1.value == "DECIMAL" and dd2.value == "CUATERNARIO":
            n = salida.value
            nums = []
            while n:
                n, r = divmod(n, 4)
                nums.append(str(r))
            salida.value = ''.join(reversed(nums))
            page.update()
        elif dd1.value == "DECIMAL" and dd2.value == "OCTAL":
            salida.value = oct(int(entrada.value))[2::]
            page.update()
        elif dd1.value == "DECIMAL" and dd2.value == "DECIMAL":
            salida.value = entrada.value
            page.update()
        elif dd1.value == "DECIMAL" and dd2.value == "HEXADECIMAL":
            salida.value = hex(int(entrada.value))[2::]
            page.update()

    page.bgcolor= ft.colors.BLUE_ACCENT_400
    page.window_height = "300"
    page.window_width = "750"
    page.window_center()

    entrada = ft.TextField(
        label="Entrada",
        bgcolor= ft.colors.BLUE_800,
        width= 300,
        height= 70
    )

    salida = ft.TextField(
        label="Salida",
        bgcolor= ft.colors.BLUE_800,
        width= 300,
        height= 70
    )

    dd1 = ft.Dropdown(
        hint_text= "SISTEMA DE ENTRADA",
        width=250,
        options=[
            ft.dropdown.Option("BINARIO"),
            ft.dropdown.Option("TERNARIO"),
            ft.dropdown.Option("CUATERNARIO"),
            ft.dropdown.Option("OCTAL"),
            ft.dropdown.Option("DECIMAL"),
            ft.dropdown.Option("HEXADECIMAL")
        ],
    )

    dd2 = ft.Dropdown(
        hint_text= "SISTEMA DE SALIDA",
        width=250,
        options=[
            ft.dropdown.Option("BINARIO"),
            ft.dropdown.Option("TERNARIO"),
            ft.dropdown.Option("CUATERNARIO"),
            ft.dropdown.Option("OCTAL"),
            ft.dropdown.Option("DECIMAL"),
            ft.dropdown.Option("HEXADECIMAL")
        ],
    )

    b1 = ft.ElevatedButton(
        text = "AC",
        bgcolor= ft.colors.BLUE_800
    )

    b2 = ft.ElevatedButton(
        text = "="
    )

    contenedor1 = ft.Container(
        content= ft.Column([entrada, salida], alignment=ft.MainAxisAlignment.START,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER),

        padding= 10,
        margin = 10,
        bgcolor= ft.colors.BLUE_500,
        width= 400,
        height= 160,
        border_radius= 30
    )
    contenedor2 = ft.Container(
        content= ft.Column([dd1, dd2], alignment=ft.MainAxisAlignment.START,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER),
        
        padding= 10,
        margin = 10,
        bgcolor= ft.colors.BLUE_500,
        width= 260,
        height= 160,
        border_radius= 30
    )

    row1 = ft.Row([contenedor1, contenedor2])
    page.add(row1)

    row2 = ft.Row([b1, b2], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.END)
    page.add(row2)

ft.app(target=main)