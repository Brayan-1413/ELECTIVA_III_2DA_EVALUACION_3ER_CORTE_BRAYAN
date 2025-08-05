from tkinter import *
import tkinter as tk
from tkinter import messagebox
from resources.modules.window_size_control.centrar_ventana import centrar_pantalla
from functools import partial
import random

#------------------------------------Recursos------------------------------------#

USER_CREDENTIALS = {"invitado":"0000",
                    "brayan": "1234"}

dark_colors = {
    'bg': '#17161b',
    'fg': 'white',
    'entry_bg': 'gray25',
    'entry_fg': 'white',
    'button_bg': '#17161b',
    'button_fg': 'white'
}

image_paths = {
    'show': './resources/images/show_ico.png',
    'hide': './resources/images/hide_ico.png',
    'user': './resources/images/user_ico.png',
    'presenter': './resources/images/presentador.png',
    'trivial': './resources/images/trivial_ico.png',
    'instructions': './resources/images/instructions_ico.png',
    'credits': './resources/images/credits_ico.png',
    'exit': './resources/images/exit_ico.png'
}

state = {}

usuario_actual = None
puntaje = 0
pregunta_actual = 0
ventana_trivia = None
preguntas_seleccionadas = []
frame_izquierdo = None
feedback_label = None

#------------------------------------PREGUNTAS------------------------------------#
preguntas = [
    {"pregunta": "¿Cuál es el lenguaje principal de programación de IA?", "opciones": ["Python", "Java", "C++", "Ruby"], "respuesta": "Python"},
    {"pregunta": "¿Cuál es el sistema operativo más usado?", "opciones": ["Linux", "Windows", "macOS", "Android"], "respuesta": "Windows"},
    {"pregunta": "¿Qué lenguaje es mejor para análisis de datos?", "opciones": ["Python", "JavaScript", "C#", "PHP"], "respuesta": "Python"},
    {"pregunta": "¿HTML es un lenguaje de?", "opciones": ["Programación", "Marcado", "Base de datos", "Estilos"], "respuesta": "Marcado"},
    {"pregunta": "¿CSS se usa para?", "opciones": ["Dar estilo", "Programar", "Crear lógica", "Datos"], "respuesta": "Dar estilo"},
    {"pregunta": "¿Cuál es un sistema de control de versiones?", "opciones": ["Git", "Excel", "Notepad", "Paint"], "respuesta": "Git"},
    {"pregunta": "¿Qué es Python?", "opciones": ["Un lenguaje", "Un editor", "Una base de datos", "Un navegador"], "respuesta": "Un lenguaje"},
    {"pregunta": "¿Cuál es el navegador de Google?", "opciones": ["Edge", "Firefox", "Safari", "Chrome"], "respuesta": "Chrome"},
    {"pregunta": "¿Qué lenguaje se usa en el lado cliente (web)?", "opciones": ["PHP", "JavaScript", "Python", "SQL"], "respuesta": "JavaScript"},
    {"pregunta": "¿Qué extensión tiene un archivo de Python?", "opciones": [".py", ".html", ".exe", ".java"], "respuesta": ".py"},
    {"pregunta": "¿Dónde se almacena la información en una base de datos relacional?", "opciones": ["Archivos", "Tablas", "Imagenes", "Funciones"], "respuesta": "Tablas"},
    {"pregunta": "¿Qué lenguaje se usa con bases de datos?", "opciones": ["SQL", "HTML", "CSS", "Python"], "respuesta": "SQL"},
    {"pregunta": "¿Qué tipo de lenguaje es Java?", "opciones": ["Compilado", "Interpretado", "Ambos", "Ninguno"], "respuesta": "Compilado"},
    {"pregunta": "¿Con qué lenguaje se desarrolla Android?", "opciones": ["Java", "Swift", "PHP", "HTML"], "respuesta": "Java"},
    {"pregunta": "¿Qué herramienta es para virtualizar?", "opciones": ["VMware", "VS Code", "Photoshop", "MySQL"], "respuesta": "VMware"}
]

#------------------------------------FUNCIONES-------------------------------------#

#--------------------------------------LOGIN---------------------------------------#

def see_hide_password():
    if state["entry_password"].cget('show') == '*':
        state["button_see_password"].config(image=state["show_image"])
        state["entry_password"].config(show='')
    else:
        state["button_see_password"].config(image=state["hide_image"])
        state["entry_password"].config(show='*')

def validation(root_login):
    global usuario_actual
    user = state["entry_user"].get()
    password = state["entry_password"].get()

    if user in USER_CREDENTIALS and password == USER_CREDENTIALS[user]:
        usuario_actual = user
        messagebox.showinfo("Inicio de Sesión Exitoso", f"¡Bienvenido! {user}")
        root_login.destroy()
        mostrar_menu_principal()
    else:
        messagebox.showerror("Inicio de Sesión Fallido", "Usuario o contraseña inválidos.")

def login_interface():
    root_login = Tk()
    root_login.title('Login')
    root_login.resizable(False, False)
    root_login.configure(bg=dark_colors['bg'])
    centrar_pantalla(root_login, 450, 470)

    state["show_image"] = PhotoImage(file=image_paths['show'])
    state["hide_image"] = PhotoImage(file=image_paths['hide'])
    state["user_image"] = PhotoImage(file=image_paths['user'])

    Label(root_login, image=state["user_image"], bg=dark_colors['bg']).place(x=160, y=0)
    Label(root_login, text='Inicio de Sesión', font=("Microsoft YaHei UI Light", 20, 'bold'),
        bg=dark_colors['bg'], fg=dark_colors['fg']).place(x=120, y=150)

    Label(root_login, text='Username', font=("Microsoft YaHei UI Light", 12, 'bold'),
        bg=dark_colors['bg'], fg=dark_colors['fg']).place(x=10, y=230)
    state["entry_user"] = Entry(root_login, font=("Microsoft YaHei UI Light", 12), width=35, bd=0,
                                bg=dark_colors['entry_bg'], fg=dark_colors['entry_fg'], insertbackground=dark_colors['entry_fg'])
    state["entry_user"].place(x=100, y=230)
    Frame(root_login, width=317, height=2, bg="#387DFF").place(x=100, y=250)

    Label(root_login, text='Password', font=("Microsoft YaHei UI Light", 12, 'bold'),
        bg=dark_colors['bg'], fg=dark_colors['fg']).place(x=10, y=290)
    state["entry_password"] = Entry(root_login, show='*', font=("Microsoft YaHei UI Light", 12), width=35, bd=0,
                                    bg=dark_colors['entry_bg'], fg=dark_colors['entry_fg'], insertbackground=dark_colors['entry_fg'])
    state["entry_password"].place(x=100, y=290)
    Frame(root_login, width=317, height=2, bg="#387DFF").place(x=100, y=310)

    state["button_see_password"] = Button(root_login, image=state["hide_image"], command=see_hide_password, bd=0,
                                        bg=dark_colors['bg'], activebackground=dark_colors['bg'])
    state["button_see_password"].place(x=420, y=290)

    Button(root_login, text='Entrar', font=("Microsoft YaHei UI Light", 14, 'bold'),
        command=lambda: validation(root_login), width=10, bg=dark_colors['button_bg'],
        fg=dark_colors['button_fg'], activebackground=dark_colors['entry_bg'], activeforeground=dark_colors['fg']).place(x=165, y=350)

    root_login.mainloop()


#---------------------------------------MENU----------------------------------------#

def mostrar_menu_principal():
    menu = Tk()
    menu.title("Menú Principal - Trivia")
    menu.configure(bg=dark_colors['bg'])
    menu.state("zoomed")
    
    def iniciar_juego():
        menu.destroy()
        iniciar_trivia()

    def mostrar_creditos():
        messagebox.showinfo("Créditos", "Desarrollado por: Brayan Diaz\nCorreo: bd015620@gmail.com ")

    def mostrar_instrucciones():
        messagebox.showinfo("Instrucciones", "Contesta las preguntas. Cada acierto suma puntos.")

    state["trivial_ico"] = PhotoImage(file=image_paths['trivial'])
    state["instructions_ico"] = PhotoImage(file=image_paths['instructions'])
    state["credits_ico"] = PhotoImage(file=image_paths['credits'])
    state["exit_ico"] = PhotoImage(file=image_paths['exit'])

    Label(menu, text=f"¡Bienvenido {usuario_actual}!", font=("Microsoft YaHei UI Light", 32, 'bold'),
        bg=dark_colors['bg'], fg=dark_colors['fg']).pack(pady=(50, 10))

    Label(menu, text="Menú de la Trivia", font=("Microsoft YaHei UI Light", 22),
        bg=dark_colors['bg'], fg=dark_colors['fg']).pack(pady=(0, 30))

    frame_botones = tk.Frame(menu, bg=dark_colors['bg'])
    frame_botones.pack()

    botones = [
        ("Iniciar Trivia", iniciar_juego, state["trivial_ico"]),
        ("Instrucciones", mostrar_instrucciones, state["instructions_ico"]),
        ("Créditos", mostrar_creditos, state["credits_ico"]),
        ("Salir", menu.destroy, state["exit_ico"])
    ]

    for i, (texto, comando, imagen) in enumerate(botones):
        fila = i // 2
        columna = i % 2
        btn = Button(
            frame_botones,
            text=texto,
            image=imagen,
            compound="top",
            font=("Microsoft YaHei UI Light", 14, "bold"),
            bg=dark_colors['button_bg'],
            fg=dark_colors['button_fg'],
            activebackground=dark_colors['entry_bg'],
            activeforeground=dark_colors['fg'],
            command=comando,
            bd=0,
            width=150,
            height=170
        )
        btn.grid(row=fila, column=columna, padx=60, pady=30)

    menu.mainloop()


#--------------------------------------TRIVIA---------------------------------------#

def iniciar_trivia():
    global puntaje, pregunta_actual, ventana_trivia, preguntas_seleccionadas, frame_izquierdo
    puntaje = 0
    pregunta_actual = 0
    preguntas_seleccionadas = random.sample(preguntas, 10)

    ventana_trivia = tk.Tk()
    ventana_trivia.title("Trivia")
    ventana_trivia.configure(bg=dark_colors['bg'])
    ventana_trivia.state("zoomed")

    frame_principal = Frame(ventana_trivia, bg=dark_colors['bg'])
    frame_principal.pack(fill="both", expand=True)

    frame_izquierdo = Frame(frame_principal, bg=dark_colors['bg'], width=800)
    frame_izquierdo.pack(side="left", fill="both", expand=True)

    frame_derecho = Frame(frame_principal, bg=dark_colors['bg'], width=750)
    frame_derecho.pack(side="right", fill="y")

    try:
        presenter_image = PhotoImage(file=image_paths["presenter"])
        ventana_trivia.presenter_image = presenter_image
        Label(frame_derecho, image=ventana_trivia.presenter_image, bd=0,
            bg=dark_colors['bg']).pack(side="bottom", anchor="se", padx=20, pady=20)
    except Exception as e:
        print(f"Error al cargar imagen del presentador: {e}")

    mostrar_pregunta()

def mostrar_pregunta():
    global pregunta_actual, frame_izquierdo

    for widget in frame_izquierdo.winfo_children():
        widget.destroy()

    if pregunta_actual >= len(preguntas_seleccionadas):
        mostrar_resultado()
        return

    Label(frame_izquierdo, text=f"Pregunta {pregunta_actual + 1} / {len(preguntas_seleccionadas)}",
        font=("Microsoft YaHei UI Light", 16, "bold"), bg=dark_colors['bg'], fg=dark_colors['fg']).pack(pady=(30, 10))

    frame_pregunta = Frame(frame_izquierdo, bg=dark_colors['bg'])
    frame_pregunta.pack(pady=20)

    pregunta_info = preguntas_seleccionadas[pregunta_actual]
    Label(frame_pregunta, text=pregunta_info["pregunta"], font=("Microsoft YaHei UI Light", 18),
        bg=dark_colors['bg'], fg=dark_colors['fg']).grid(row=0, column=0, columnspan=2, pady=10)

    opciones_botones = []

    for i, opcion in enumerate(pregunta_info["opciones"]):
        fila = (i // 2) + 1
        columna = i % 2
        btn = Button(frame_pregunta, text=opcion, font=("Arial", 14), width=20,
                    bg=dark_colors['button_bg'], fg=dark_colors['button_fg'],
                    activebackground=dark_colors['entry_bg'], activeforeground=dark_colors['fg'],
                    command=partial(verificar_respuesta, opcion))
        btn.grid(row=fila, column=columna, padx=10, pady=10)
        opciones_botones.append(btn)

    ventana_trivia.opciones_botones = opciones_botones

    feedback_label = Label(frame_izquierdo, text="", font=("Arial", 14, "italic"),
                        bg=dark_colors['bg'], fg="white")
    feedback_label.pack(pady=(20, 0))

    ventana_trivia.feedback_label = feedback_label

def verificar_respuesta(opcion_elegida):
    global puntaje, pregunta_actual

    for btn in ventana_trivia.opciones_botones:
        btn.config(state="disabled")

    correcta = preguntas_seleccionadas[pregunta_actual]["respuesta"]

    if opcion_elegida == correcta:
        puntaje += 1
        ventana_trivia.feedback_label.config(text="¡Correcto!", fg="lightgreen")
    else:
        ventana_trivia.feedback_label.config(text=f"Respuesta correcta: {correcta}", fg="red")

    ventana_trivia.after(1500, siguiente_pregunta)

def siguiente_pregunta():
    global pregunta_actual
    pregunta_actual += 1
    mostrar_pregunta()

def mostrar_resultado():
    global frame_izquierdo

    for widget in frame_izquierdo.winfo_children():
        widget.destroy()

    frame_resultado = Frame(frame_izquierdo, bg=dark_colors['bg'])
    frame_resultado.pack(pady=100)

    Label(frame_resultado, text="¡Has completado la trivia!", font=("Microsoft YaHei UI Light", 22, "bold"),
        bg=dark_colors['bg'], fg=dark_colors['fg']).pack(pady=10)

    total = len(preguntas_seleccionadas)
    Label(frame_resultado, text=f"Puntaje final: {puntaje} / {total}", font=("Microsoft YaHei UI Light", 18),
        bg=dark_colors['bg'], fg=dark_colors['fg']).pack(pady=10)

    if puntaje == total:
        mensaje = "¡Perfecto!"
    elif puntaje >= total // 2:
        mensaje = "¡Buen trabajo!"
    else:
        mensaje = "Puedes mejorar."

    Label(frame_resultado, text=mensaje, font=("Microsoft YaHei UI Light", 16),
        bg=dark_colors['bg'], fg=dark_colors['fg']).pack(pady=5)

    Button(frame_resultado, text="Volver al menú", font=("Microsoft YaHei UI Light", 14),
        command=lambda: [ventana_trivia.destroy(), mostrar_menu_principal()],
        bg=dark_colors['button_bg'], fg=dark_colors['button_fg'], activebackground=dark_colors['entry_bg'], activeforeground=dark_colors['fg']).pack(pady=20)

#---------------------------------------MAIN----------------------------------------#

if __name__ == '__main__':
    login_interface()