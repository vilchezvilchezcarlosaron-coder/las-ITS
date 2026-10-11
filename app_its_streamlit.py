"""
App Educativa ITS - Versión Streamlit
Proyecto CyT - Carlos Aron Vilchez Vilchez - Cuarto A
Profesora: Indira Tufino
"""

import streamlit as st

# ---------- Configuración de la página ----------
st.set_page_config(
    page_title="App Educativa ITS | Proyecto CyT",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------- Datos ----------
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

# ---------- Sidebar / Menú ----------
st.sidebar.title("🩺 App Educativa ITS")
st.sidebar.markdown("---")
pagina = st.sidebar.radio(
    "Menú principal",
    ["Inicio", "Información sobre ITS", "Prevención", "Quiz interactivo", "Acerca del proyecto"]
)
st.sidebar.markdown("---")
st.sidebar.caption("Proyecto CyT · Cuarto A")
st.sidebar.caption("Carlos Aron Vilchez Vilchez")
st.sidebar.caption("Prof. Indira Tufino")

# ---------- Páginas ----------
if pagina == "Inicio":
    st.title("App Educativa ITS")
    st.subheader("Proyecto de Ciencia y Tecnología")
    st.markdown("""
    Esta aplicación es un **prototipo educativo** creado para informar de forma clara y sin prejuicios sobre las Infecciones de Transmisión Sexual (ITS).

    ### Capacidades de diseño aplicadas:
    1. **Determina** una alternativa de solución tecnológica  
    2. **Diseña** la alternativa de solución tecnológica  
    3. **Implementa y valida** la alternativa de solución tecnológica  
    4. **Evalúa y comunica** el funcionamiento y los impactos  

    ---
    **Importante:** Esta app es solo educativa.  
    No reemplaza la atención de un profesional de la salud.
    """)
    st.info("👈 Usa el menú de la izquierda para navegar")

elif pagina == "Información sobre ITS":
    st.title("Información sobre ITS")
    st.write("Selecciona una infección para ver más detalles:")

    its_seleccionada = st.selectbox("Elige una ITS:", list(ITS_DATA.keys()))

    data = ITS_DATA[its_seleccionada]

    st.markdown(f"### {its_seleccionada}")
    st.markdown(f"**Tipo:** {data['tipo']}")

    st.markdown("#### ¿Qué es?")
    st.write(data["info"])

    st.markdown("#### Prevención clave")
    st.success(data["prevencion"])

elif pagina == "Prevención":
    st.title("Prevención")
    st.write("La mejor herramienta es informarse y cuidarse:")

    for i, tip in enumerate(PREVENCION_TIPS, 1):
        st.markdown(f"**{i}.** {tip}")

    st.warning("Recuerda: el preservativo + información + pruebas = la mejor protección.")

elif pagina == "Quiz interactivo":
    st.title("Quiz interactivo")
    st.write("Responde las siguientes preguntas para poner a prueba lo que aprendiste.")

    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
        st.session_state.quiz_respondidas = 0
        st.session_state.respuestas = {}

    for i, q in enumerate(QUIZ):
        st.markdown(f"### Pregunta {i+1}")
        respuesta = st.radio(
            q["pregunta"],
            q["opciones"],
            key=f"q_{i}",
            index=None
        )

        if respuesta is not None:
            st.session_state.respuestas[i] = respuesta
            if q["opciones"].index(respuesta) == q["correcta"]:
                st.success("¡Correcto!")
            else:
                st.error("Incorrecto. Revisa la información de la app.")

    if st.button("Ver resultado final"):
        score = 0
        for i, q in enumerate(QUIZ):
            if i in st.session_state.respuestas:
                if q["opciones"].index(st.session_state.respuestas[i]) == q["correcta"]:
                    score += 1
        porcentaje = int((score / len(QUIZ)) * 100)
        st.markdown(f"## Resultado: {score} de {len(QUIZ)} ({porcentaje}%)")

        if porcentaje >= 80:
            st.balloons()
            st.success("¡Excelente! Dominas bien el tema.")
        elif porcentaje >= 50:
            st.info("Bien. Repasa un poco más las secciones de información.")
        else:
            st.warning("Te recomendamos revisar la información de la app y volver a intentarlo.")

elif pagina == "Acerca del proyecto":
    st.title("Acerca del proyecto")
    st.markdown("""
    **Estudiante:** Carlos Aron Vilchez Vilchez  
    **Grado y Sección:** Cuarto A  
    **Profesora:** Indira Tufino  
    **Área:** Ciencia y Tecnología (CyT)

    ---

    ### Competencia trabajada:
    > *Diseña y construye soluciones tecnológicas para resolver problemas de su entorno*

    ### Capacidades aplicadas:
    1. **Determina** una alternativa de solución tecnológica  
    2. **Diseña** la alternativa de solución tecnológica  
    3. **Implementa y valida** la alternativa de solución tecnológica  
    4. **Evalúa y comunica** el funcionamiento y los impactos  

    ---

    **Problema:** Desinformación y estigma sobre las ITS en adolescentes.  
    **Solución:** App educativa interactiva y accesible.
    """)
