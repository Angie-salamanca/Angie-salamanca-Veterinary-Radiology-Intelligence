# 🩻 Veterinary Radiology Intelligence

Análisis de datos y dashboard interactivo sobre estudios de radiología veterinaria, construido con **Python, PostgreSQL, SQL y Streamlit**.

Parte de la suite de proyectos **VetInsight Analytics** — soluciones de analítica de datos aplicadas a medicina veterinaria.

---

## 📌 Descripción del proyecto

Este proyecto analiza un histórico de estudios radiográficos de una clínica veterinaria para responder preguntas clave del negocio: qué especies requieren más estudios, cómo se comporta la tasa de informes médicos según la cantidad de radiografías tomadas, y cómo evolucionan los casos a lo largo del tiempo.

El proyecto sigue un flujo de trabajo real de análisis de datos:

    Excel (datos crudos)
          ↓
    Limpieza con Pandas
          ↓
    Base de datos PostgreSQL
          ↓
    Consultas SQL
          ↓
    Dashboard interactivo en Streamlit (Plotly)

## ❓ Preguntas que responde

- ¿Qué especies requieren más estudios radiográficos?
- ¿Existe relación entre la cantidad de radiografías tomadas y la probabilidad de tener un informe médico?
- ¿Cómo varía el volumen de casos año a año?
- ¿Qué tan completos están los datos clínicos (fechas, especie)?

## 📊 Dashboard

El dashboard incluye:

- **KPIs de calidad de datos**: estudios totales, estudios con fecha registrada, fechas y especies faltantes.
- **Filtro por rango de años** en la barra lateral, aplicado a los análisis por especie y por tasa de informes.
- **Casos de radiología por especie**
- **Tasa de informes según cantidad de radiografías**
- **Casos de radiología por año** (vista completa, sin filtro)

<!-- ![Dashboard](images/dashboard/dashboard_preview.png) -->
*Captura del dashboard próximamente*

🔗 **(C:\Users\angie\OneDrive\Desktop\Veterinary-Radiology-Intelligence\images\dashboard\dashboard_preview.png)

## 🔍 Insights principales

- El dataset contiene **693 estudios radiográficos** en total, con **689 fechas registradas** (99.4% de completitud).
- La especie **canina** representa la mayoría de los estudios (496 casos), seguida de la **felina** (193 casos).
- Solo 3 registros presentan especie faltante, lo que indica una buena calidad general de los datos clínicos.

## 🛠️ Tecnologías utilizadas

- **Python** (Pandas, SQLAlchemy)
- **PostgreSQL**
- **SQL** (agregaciones, `FILTER`, `EXTRACT`, parámetros con nombre)
- **Streamlit**
- **Plotly**
- **Git / GitHub**

## 📁 Estructura del proyecto

    Veterinary-Radiology-Intelligence/
    │
    ├── app/
    │   └── app.py                  # Dashboard Streamlit
    │
    ├── data/
    │   ├── raw/                    # Datos originales (Excel)
    │   └── processed/              # Datos limpios (CSV)
    │
    ├── notebooks/
    │   ├── 01_Data_Understanding.ipynb
    │   ├── 02_Data_Cleaning.ipynb
    │   └── 03_Exploratory_Data_Analysis.ipynb
    │
    ├── sql/                        # Consultas SQL exploratorias
    ├── docs/                       # Diccionario de datos, metodología
    ├── reports/                    # Plan de limpieza, insights del EDA
    ├── images/                     # Capturas del dashboard y gráficos
    ├── tests/
    │
    ├── database.py                 # Conexión a PostgreSQL
    ├── queries.py                  # Consultas SQL parametrizadas
    ├── analysis.py                 # Funciones que devuelven DataFrames
    ├── visualizations.py           # Gráficos Plotly
    │
    ├── requirements.txt
    ├── PROJECT_CHART.md
    └── README.md

## ⚙️ Cómo correrlo localmente

    # Clonar el repositorio
    git clone [url-del-repositorio]
    cd Veterinary-Radiology-Intelligence

    # Crear y activar entorno virtual
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1        # Windows
    source .venv/bin/activate           # Mac/Linux

    # Instalar dependencias
    pip install -r requirements.txt

    # Correr el dashboard
    python -m streamlit run app/app.py

> Necesitas una base de datos PostgreSQL con la tabla `public.radiology` cargada, y configurar tu contraseña en `.streamlit/secrets.toml`.

## ⚠️ Limitaciones de los datos

- 4 registros no tienen fecha de examen registrada.
- 3 registros no tienen la especie identificada.
- Los datos provienen de una única clínica, por lo que los patrones no son necesariamente generalizables.

## 👩‍⚕️ Sobre este proyecto

Este proyecto combina experiencia clínica veterinaria con habilidades de ciencia de datos (Python, SQL, visualización), como parte de un portafolio orientado a roles de análisis de datos.

**Autora:** Angie SALAMANCA
[(https://www.linkedin.com/in/angie-salamanca-franco/?isSelfProfile=true&locale=fr)] · [(https://github.com/Angie-salamanca)]
[LinkedIn] · [GitHub]