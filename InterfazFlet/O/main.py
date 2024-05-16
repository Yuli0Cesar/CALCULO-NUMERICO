import flet as ft
import numpy as np

def main(page:ft.Page):

    def entrada(e):
        if(dimension.value.isdigit()):
            True
            page.update()
        else:
            page.dialog = alerta
            alerta.open = True
            page.update()

    def close(e):
        alerta.open = False
        dimension.value = ""
        page.update()

    def agg_matriz(e):
        #Definir valores random en la matriz
        matrizv = [[np.random.randint(1,999) for i in range(int(dimension.value))]for i in range(int(dimension.value))]
        A = np.array(matrizv)
        B = np.array(matrizv[-1])
        X0 = np.zeros(int(dimension.value))

        tolera = 0.00001
        iteramax = 100
# PROCEDIMIENTO
# Gauss-Seidel
        tamano = np.shape(A)
        n = tamano[0]
        m = tamano[1]
#  valores iniciales
        X = np.copy(X0)
        diferencia = np.ones(n, dtype=float)
        errado = 2*tolera
        itera = 0
        while not(errado<=tolera or itera>iteramax):
             # por fila
             for i in range(0,n,1):
                  # por columna
                  suma = 0 
                  for j in range(0,m,1):
                       # excepto diagonal de A
                       if (i!=j): 
                            suma = suma-A[i,j]*X[j]
        
                  nuevo = (B[i]+suma)/A[i,i]
                  diferencia[i] = np.abs(nuevo-X[i])
                  X[i] = nuevo
             errado = np.max(diferencia)
             itera = itera + 1
# Respuesta X en columna
        X = np.transpose([X])

        matriz.value = str(matrizv)
        vector.value = matrizv[-1]
        resultado.value = str(X)
        vectorxo.value = str(X0)
        page.update()

    def erase(e):
        dimension.value = ""
        matriz.value = ""
        vector.value = ""
        vectorxo.value = ""
        resultado.value = ""
        page.update()

    page.bgcolor= ft.colors.BLUE_ACCENT_400
    page.window_height = "500"
    page.window_width = "1150"
    page.window_center()

    dimension = ft.TextField(
        label="DIMENSION",
        bgcolor= ft.colors.BLUE_800,
        width= 300,
        autofocus= True,
        height= 70,
        on_change=entrada
    )

    matriz = ft.TextField(

        label="MATRIZ",
        bgcolor= ft.colors.BLUE_800,
        width=300,
        height=200,
        multiline= True,
        max_lines= 20,
        min_lines=20

    )

    b1 = ft.ElevatedButton(
        text="AC",
        bgcolor= ft.colors.BLUE_800,
        on_click=erase
    )

    b2 = ft.ElevatedButton(
        text="RND",
        bgcolor= ft.colors.BLUE_800,
        on_click= agg_matriz
    )

    vector = ft.TextField(

        label="VECTOR",
        bgcolor= ft.colors.BLUE_800,
        width=300,
        height=70

    )

    vectorxo = ft.TextField(

        label="VECTOR XO",
        bgcolor= ft.colors.BLUE_800,
        width=300,
        height=70

    )

    resultado = ft.TextField(

        label="RESULTADO",
        bgcolor= ft.colors.BLUE_800,
        width=300,
        height=200,
        multiline= True,
        max_lines= 20,
        min_lines=20

    )
    
    row1 = ft.Row(
        [b1,b2], vertical_alignment=ft.CrossAxisAlignment.END, alignment=ft.MainAxisAlignment.START, height=50
        )

    contenedor1 = ft.Container(
        content= ft.Column([dimension, matriz], alignment=ft.MainAxisAlignment.START,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER),
            
        padding= 10,
        margin = 10,
        bgcolor= ft.colors.BLUE_500,
        width= 400,
        height= 350,
        border_radius= 30
    )

    contenedor2 = ft.Container(
        content= ft.Column([row1, vector, vectorxo], alignment=ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,)
    )
    row2 = ft.Row(
        [contenedor2, resultado]
    )
    contenedor3 = ft.Container(
        content= ft.Column([row2], alignment=ft.MainAxisAlignment.START,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,),
        
        padding= 10,
        margin = 10,
        bgcolor= ft.colors.BLUE_500,
        width= 650,
        height= 250,
        border_radius= 30
    )

    row3 = ft.Row(
        [contenedor1, contenedor3]
    )

    alerta = ft.AlertDialog(
        modal=True,
        title=ft.Text("ADVERTENCIA"),
        content=ft.Text("No usar letras o decimales"),
        actions=[
            ft.TextButton("Aceptar", on_click= close)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("letra"),
    )
    
    page.add(row3)

    page.update()

ft.app(target=main)