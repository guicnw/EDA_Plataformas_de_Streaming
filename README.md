# Análisis Exploratorio de Contenido de Plataformas de Streaming

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre tres plataformas de streaming populares en España: **Netflix**, **Amazon Prime Video** y **HBO Max**. El análisis se complementa con rankings de **IMDb** y mis propias valoraciones personales como espectador, con el objetivo de identificar cuál es la plataforma más adecuada desde múltiples enfoques: cantidad de contenido, calidad, disponibilidad por región y afinidad con los gustos personales.

---

## Objetivos del Proyecto

- Comparar **cantidad de contenido** entre plataformas.
- Evaluar la **calidad promedio** de los títulos usando datos de IMDb.
- Estudiar la **distribución de géneros** y la proporción entre películas y series.
- Analizar la **disponibilidad regional** de contenidos (España, EE.UU., México).
- Relacionar los catálogos con:
  - El **Top 250 de IMDb** (películas y series).
  - Mis **valoraciones personales en IMDb**.
- Contrastar la oferta de contenido con los **precios de suscripción actuales**.

---

## Estructura del Proyecto

```
.
├── main.ipynb               # Notebook principal con el análisis final
├── README.md                # Este archivo
├── Memoria                  # Documento de memoria del proyecto (PDF)
├── Presentación             # Versión PDF de la presentación final
└── src
    ├── data                 # Datos limpios utilizados en el análisis
    ├── img                  # Gráficos generados
    ├── notebooks            # Notebooks de prueba y desarrollo
    └── utils
        └── limpieza.py      # Clase de limpieza usada para los datasets
```

---

## Visualizaciones Destacadas

- Comparativas de cantidad y calidad por plataforma.
- Disponibilidad de títulos del Top IMDb por plataforma.
- Densidad de lanzamientos por año.
- Análisis de gustos personales por género y año.
- Mapa de calor de distribución de contenido por categoría temporal.

---

## Tecnologías Utilizadas

- **Python** 3.11
- **Pandas** para manipulación de datos.
- **Matplotlib & Seaborn** para visualización.
- **Jupyter Notebooks** dentro de **Visual Studio Code**.

---

## Cómo Ejecutar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/eda-streaming.git
   cd eda-streaming
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Abre `main.ipynb` en Jupyter o Visual Studio Code y ejecuta el análisis paso a paso.

---

## Datos

Los datasets utilizados han sido limpiados y normalizados para asegurar consistencia. Solo se han subido versiones ligeras de los mismos si su tamaño original excedía el límite recomendado para GitHub.

---

## Notas Finales

Este proyecto combina análisis de datos con elementos personales para ofrecer una visión integral sobre qué plataforma de streaming se adapta mejor, tanto en términos objetivos como subjetivos. Representa un trabajo completo de exploración, visualización y reflexión, aplicable a distintos perfiles de usuarios.

Autor: Guillermo Castillón Novo  
Año: 2024



