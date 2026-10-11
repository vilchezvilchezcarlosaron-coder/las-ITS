"""
PROYECTO CyT - App Educativa sobre ITS
Prototipo virtual guiado por las capacidades de diseño de CyT
Competencia: Diseña y construye soluciones tecnológicas para resolver problemas de su entorno

Requisitos: Python 3 (Tkinter viene incluido)
Cómo correr: python app_its_educativa.py
"""

import tkinter as tk
from tkinter import messagebox, font

# ---------- Colores (mismo estilo de la presentación) ----------
BG = "#F1ECDF"
NAVY = "#1F3DA8"
INK = "#1A1A1A"
MUTED = "#6B6B6B"
WHITE = "#FFFFFF"
SAGE = "#8FA67E"
CARD_BG = "#FFFFFF"

# ---------- Datos de las ITS ----------
ITS_DATA = {
    "Clamidia": {
        "tipo": "Bacteria",
        "info": "Es una de las ITS más comunes en jóvenes. Muchas veces no presenta síntomas, por eso es importante hacerse pruebas. Se transmite por contacto sexual y se cura con antibióticos si se detecta a tiempo.",
        "prevencion": "Uso correcto del preservativo + pruebas regulares."
    },
    "Gonorrea": {
        "tipo": "Bacteria",
        "info": "Puede afectar genitales, garganta y ojos. A veces no da síntomas claros. Se transmite por contacto sexual y se trata con antibióticos.",
        "prevencion": "Preservativo + evitar contacto con fluidos infectados."
    },
    "Sífilis": {
        "tipo": "Bacteria",
        "info": "Se desarrolla por etapas. En etapas tempranas se cura con antibióticos. Si no se trata puede causar problemas graves a largo plazo.",
        "prevencion": "Preservativo + pruebas de sangre periódicas."
    },
    "VPH": {
        "tipo": "Virus",
        "info": "Virus del Papiloma Humano. Algunos tipos pueden causar verrugas o, a largo plazo, ciertos tipos de cáncer. Existe vacuna efectiva.",
        "prevencion": "Vacuna contra el VPH + uso de preservativo."
    },
    "Herpes genital": {
        "tipo": "Virus",
        "info": "Causa llagas o ampollas. No tiene cura, pero se controla con medicamentos antivirales. Se puede transmitir incluso sin síntomas visibles.",
        "prevencion": "Preservativo + evitar contacto cuando hay brotes."
    },
    "VIH": {
        "tipo": "Virus",
        "info": "Afecta el sistema inmunológico. Con tratamiento antirretroviral se controla y se puede vivir una vida saludable. No se transmite por abrazos, besos o compartir comida.",
        "prevencion": "Preservativo + no compartir agujas + tratamiento si es necesario."
    },
}

PREVENCION_TIPS = [
    "Usa preservativo de forma correcta y constante en todas las relaciones (vaginales, anales y orales).",
    "Vacúnate contra el VPH y la Hepatitis B. Pregunta en tu centro de salud.",
    "Hazte pruebas de ITS si tienes vida sexual activa, aunque no tengas síntomas.",
    "Habla con tu pareja sobre protección y salud sexual. Es un acto de cuidado.",
    "Reduce el número de parejas sexuales para disminuir el riesgo de exposición.",
    "Nunca compartas agujas, jeringas ni juguetes sexuales sin limpiar.",
    "Si tienes síntomas o dudas, acude a un profesional de la salud. No te automediques.",
]

QUIZ = [
    {
        "pregunta": "¿Qué significa ITS?",
        "opciones": ["Infección de Transmisión Sexual", "Enfermedad Tropical Severa", "Infección Total del Sistema"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuál es la diferencia principal entre ITS y ETS?",
        "opciones": [
            "ITS es más amplio: incluye infecciones con o sin síntomas",
            "No hay diferencia, son lo mismo",
            "ETS solo afecta a adultos"
        ],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuál de estas ITS se puede prevenir con vacuna?",
        "opciones": ["Clamidia", "VPH", "Gonorrea"],
        "correcta": 1
    },
    {
        "pregunta": "¿Muchas ITS no presentan síntomas?",
        "opciones": ["Falso", "Verdadero", "Solo en adultos"],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuál es la mejor forma de prevenir la mayoría de ITS?",
        "opciones": [
            "Usar preservativo correctamente",
            "Ducharse después de tener relaciones",
            "Tomar antibióticos por cuenta propia"
        ],
        "correcta": 0
    },
]


class AppITS:
    def __init__(self, root):
        self.root = root
        self.root.title("App Educativa ITS - Proyecto CyT")
        self.root.geometry("720x560")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.quiz_index = 0
        self.quiz_score = 0

        # Fuentes
        self.font_title = font.Font(family="Helvetica", size=20, weight="bold")
        self.font_subtitle = font.Font(family="Helvetica", size=14, weight="bold")
        self.font_body = font.Font(family="Helvetica", size=12)
        self.font_small = font.Font(family="Helvetica", size=11)

        self.mostrar_menu()

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def boton(self, parent, texto, comando, color=NAVY):
        btn = tk.Button(
            parent,
            text=texto,
            command=comando,
            bg=color,
            fg=WHITE,
            font=self.font_body,
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2",
            activebackground="#16308a",
            activeforeground=WHITE,
        )
        return btn

    # ==================== MENÚ PRINCIPAL ====================
    def mostrar_menu(self):
        self.limpiar()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=40, pady=30)

        tk.Label(
            frame,
            text="App Educativa ITS",
            font=self.font_title,
            bg=BG,
            fg=INK
        ).pack(pady=(10, 5))

        tk.Label(
            frame,
            text="Proyecto de Ciencia y Tecnología · Capacidades de Diseño",
            font=self.font_small,
            bg=BG,
            fg=MUTED
        ).pack(pady=(0, 25))

        tk.Label(
            frame,
            text="Elige una sección:",
            font=self.font_subtitle,
            bg=BG,
            fg=INK
        ).pack(pady=(0, 15))

        self.boton(frame, "1.  Información sobre ITS", self.mostrar_its).pack(pady=6, fill="x")
        self.boton(frame, "2.  Prevención", self.mostrar_prevencion).pack(pady=6, fill="x")
        self.boton(frame, "3.  Quiz interactivo", self.iniciar_quiz).pack(pady=6, fill="x")
        self.boton(frame, "4.  Acerca del proyecto", self.mostrar_acerca).pack(pady=6, fill="x")

        tk.Label(
            frame,
            text="Recuerda: esta app es educativa.\nNo reemplaza la atención de un profesional de la salud.",
            font=self.font_small,
            bg=BG,
            fg=MUTED,
            justify="center"
        ).pack(pady=(30, 0))

    # ==================== SECCIÓN ITS ====================
    def mostrar_its(self):
        self.limpiar()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=30, pady=20)

        tk.Label(
            frame,
            text="Información sobre ITS",
            font=self.font_title,
            bg=BG,
            fg=INK
        ).pack(pady=(5, 10))

        tk.Label(
            frame,
            text="Selecciona una infección para ver más detalles:",
            font=self.font_body,
            bg=BG,
            fg=MUTED
        ).pack(pady=(0, 15))

        # Botones de cada ITS
        grid = tk.Frame(frame, bg=BG)
        grid.pack()

        nombres = list(ITS_DATA.keys())
        for i, nombre in enumerate(nombres):
            fila = i // 3
            col = i % 3
            btn = self.boton(grid, nombre, lambda n=nombre: self.detalle_its(n))
            btn.grid(row=fila, column=col, padx=8, pady=8, sticky="ew")

        self.boton(frame, "← Volver al menú", self.mostrar_menu, color=MUTED).pack(pady=(25, 0))

    def detalle_its(self, nombre):
        self.limpiar()
        data = ITS_DATA[nombre]

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=40, pady=25)

        tk.Label(
            frame,
            text=nombre,
            font=self.font_title,
            bg=BG,
            fg=NAVY
        ).pack(pady=(5, 5))

        tk.Label(
            frame,
            text=f"Tipo: {data['tipo']}",
            font=self.font_subtitle,
            bg=BG,
            fg=SAGE
        ).pack(pady=(0, 15))

        # Card de información
        card = tk.Frame(frame, bg=WHITE, padx=20, pady=15)
        card.pack(fill="x", pady=5)

        tk.Label(
            card,
            text="¿Qué es?",
            font=self.font_subtitle,
            bg=WHITE,
            fg=INK
        ).pack(anchor="w")

        tk.Label(
            card,
            text=data["info"],
            font=self.font_body,
            bg=WHITE,
            fg=INK,
            wraplength=600,
            justify="left"
        ).pack(anchor="w", pady=(5, 10))

        tk.Label(
            card,
            text="Prevención clave:",
            font=self.font_subtitle,
            bg=WHITE,
            fg=INK
        ).pack(anchor="w")

        tk.Label(
            card,
            text=data["prevencion"],
            font=self.font_body,
            bg=WHITE,
            fg=INK,
            wraplength=600,
            justify="left"
        ).pack(anchor="w", pady=(5, 0))

        self.boton(frame, "← Volver a la lista", self.mostrar_its, color=MUTED).pack(pady=(25, 0))

    # ==================== PREVENCIÓN ====================
    def mostrar_prevencion(self):
        self.limpiar()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=35, pady=20)

        tk.Label(
            frame,
            text="Prevención",
            font=self.font_title,
            bg=BG,
            fg=INK
        ).pack(pady=(5, 5))

        tk.Label(
            frame,
            text="La mejor herramienta es informarse y cuidarse",
            font=self.font_body,
            bg=BG,
            fg=MUTED
        ).pack(pady=(0, 15))

        # Lista de tips con scroll visual simple
        for i, tip in enumerate(PREVENCION_TIPS, 1):
            row = tk.Frame(frame, bg=WHITE, padx=12, pady=8)
            row.pack(fill="x", pady=4)

            tk.Label(
                row,
                text=f"{i}.",
                font=self.font_subtitle,
                bg=WHITE,
                fg=NAVY,
                width=3
            ).pack(side="left")

            tk.Label(
                row,
                text=tip,
                font=self.font_small,
                bg=WHITE,
                fg=INK,
                wraplength=580,
                justify="left"
            ).pack(side="left", fill="x")

        self.boton(frame, "← Volver al menú", self.mostrar_menu, color=MUTED).pack(pady=(20, 0))

    # ==================== QUIZ ====================
    def iniciar_quiz(self):
        self.quiz_index = 0
        self.quiz_score = 0
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        self.limpiar()

        if self.quiz_index >= len(QUIZ):
            self.mostrar_resultado_quiz()
            return

        q = QUIZ[self.quiz_index]

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=40, pady=25)

        tk.Label(
            frame,
            text=f"Pregunta {self.quiz_index + 1} de {len(QUIZ)}",
            font=self.font_small,
            bg=BG,
            fg=MUTED
        ).pack(pady=(5, 10))

        tk.Label(
            frame,
            text=q["pregunta"],
            font=self.font_subtitle,
            bg=BG,
            fg=INK,
            wraplength=620,
            justify="center"
        ).pack(pady=(10, 25))

        for i, opcion in enumerate(q["opciones"]):
            self.boton(
                frame,
                opcion,
                lambda idx=i: self.responder(idx)
            ).pack(pady=6, fill="x")

    def responder(self, indice):
        correcta = QUIZ[self.quiz_index]["correcta"]
        if indice == correcta:
            self.quiz_score += 1
            messagebox.showinfo("¡Correcto!", "Muy bien, esa es la respuesta correcta.")
        else:
            messagebox.showwarning("Incorrecto", "No es la respuesta correcta. ¡Sigue intentando!")

        self.quiz_index += 1
        self.mostrar_pregunta()

    def mostrar_resultado_quiz(self):
        self.limpiar()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=40, pady=40)

        tk.Label(
            frame,
            text="Resultado del Quiz",
            font=self.font_title,
            bg=BG,
            fg=INK
        ).pack(pady=(20, 15))

        porcentaje = int((self.quiz_score / len(QUIZ)) * 100)

        tk.Label(
            frame,
            text=f"Obtuviste {self.quiz_score} de {len(QUIZ)} correctas",
            font=self.font_subtitle,
            bg=BG,
            fg=NAVY
        ).pack(pady=10)

        tk.Label(
            frame,
            text=f"({porcentaje}%)",
            font=self.font_title,
            bg=BG,
            fg=SAGE
        ).pack(pady=5)

        if porcentaje >= 80:
            mensaje = "¡Excelente! Dominas bien el tema."
        elif porcentaje >= 50:
            mensaje = "Bien. Repasa un poco más las secciones de información."
        else:
            mensaje = "Te recomendamos revisar la información de la app y volver a intentarlo."

        tk.Label(
            frame,
            text=mensaje,
            font=self.font_body,
            bg=BG,
            fg=INK,
            wraplength=500,
            justify="center"
        ).pack(pady=20)

        self.boton(frame, "Volver a intentar", self.iniciar_quiz).pack(pady=6, fill="x")
        self.boton(frame, "← Volver al menú", self.mostrar_menu, color=MUTED).pack(pady=6, fill="x")

    # ==================== ACERCA DEL PROYECTO ====================
    def mostrar_acerca(self):
        self.limpiar()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=40, pady=25)

        tk.Label(
            frame,
            text="Acerca del proyecto",
            font=self.font_title,
            bg=BG,
            fg=INK
        ).pack(pady=(5, 15))

        texto = (
            "Este prototipo forma parte de un proyecto de Ciencia y Tecnología.\n\n"
            "Competencia trabajada:\n"
            "«Diseña y construye soluciones tecnológicas para resolver problemas de su entorno»\n\n"
            "Capacidades aplicadas:\n"
            "1. Determina una alternativa de solución tecnológica\n"
            "2. Diseña la alternativa de solución tecnológica\n"
            "3. Implementa y valida la alternativa de solución tecnológica\n"
            "4. Evalúa y comunica el funcionamiento y los impactos\n\n"
            "Problema: desinformación y estigma sobre las ITS en adolescentes.\n"
            "Solución: app educativa interactiva y accesible."
        )

        tk.Label(
            frame,
            text=texto,
            font=self.font_body,
            bg=BG,
            fg=INK,
            justify="left",
            wraplength=620
        ).pack(anchor="w", pady=10)

        self.boton(frame, "← Volver al menú", self.mostrar_menu, color=MUTED).pack(pady=(20, 0))


# ---------- Ejecutar la app ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = AppITS(root)
    root.mainloop()
