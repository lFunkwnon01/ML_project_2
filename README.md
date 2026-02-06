🎬 Visualización de Machine Learning con Manim



Este repositorio contiene el código fuente para generar videos educativos sobre algoritmos fundamentales de Machine Learning, específicamente enfocados en \*\*Clasificación Binaria\*\*, \*\*SVM (Support Vector Machines)\*\* y el \*\*Kernel Trick\*\*.



Las animaciones han sido desarrolladas utilizando \[Manim](https://www.manim.community/), una librería de Python para animaciones matemáticas programáticas.



\## 📂 Contenido del Proyecto



El proyecto se divide en tres módulos principales:



\*   \*\*Regresión Logística (`Regresion\_logistica.py`):\*\* Visualiza el flujo completo de la regresión logística: desde el cálculo del score lineal, pasando por la función sigmoide para obtener probabilidades, hasta la definición de la frontera de decisión y la evaluación con métricas (Accuracy, Precision, Recall).

\*   \*\*SVM y el Kernel Trick (`KernelTrick (1)\_con\_kernel (1).py`):\*\* Una explicación visual profunda sobre cómo tratar datos no separables linealmente (como el problema XOR). Muestra el mapeo de características de 2D a 3D y una visualización geométrica del Kernel RBF (Gaussiano).

\*   \*\*SVM Lineal (`MachineLearning2\_sinkernel.py`):\*\* Enfoque en la separación de clases mediante hiperplanos de máximo margen en espacios de características originales sin transformaciones de kernel.



---



\## 🛠️ Requisitos (Requirements)



Para poder ejecutar y compilar estos videos, necesitas tener instalado lo siguiente:



1\.  \*\*Python 3.8 o superior.\*\*

2\.  \*\*Manim y sus dependencias del sistema:\*\*

&nbsp;   \*   FFmpeg (para renderizado de video).

&nbsp;   \*   LaTeX (opcional, para renderizar fórmulas matemáticas de alta calidad).

&nbsp;   \*   Pango, Cairo y otras librerías gráficas.



\*\*Instalación de la librería de Python:\*\*

```bash

pip install manim

```



---



\## 🚀 Cómo Ejecutar y Compilar (How to Build)



Para generar los videos a partir de los archivos `.py`, debes usar la terminal dentro de la carpeta del proyecto.



\*\*1. Compilar la animación de Regresión Logística:\*\*

```bash

manim -pql Regresion\_logistica.py ClassificationRegressionDemo

```



\*\*2. Compilar la animación del Kernel Trick (3D):\*\*

```bash

manim -pql "KernelTrick (1)\_con\_kernel (1).py" KernelTrickFull

```



\*\*Explicación de los comandos:\*\*

\*   `manim`: Invoca la herramienta.

\*   `-p`: (Preview) Abre el video automáticamente al finalizar.

\*   `ql`: (Quality Low) Renderiza a 480p para pruebas rápidas. Usa `-pqh` para alta calidad (1080p).

\*   `archivo.py`: El nombre del script.

\*   `NombreClase`: El nombre de la clase dentro del script que deseas renderizar.



---



\## 📊 Conceptos Explicados en los Videos



\*   \*\*Frontera de Decisión:\*\* La línea o plano que divide las clases.

\*   \*\*Función Sigmoide:\*\* Usada para convertir scores en probabilidades entre 0 y 1.

\*   \*\*Feature Expansion:\*\* El proceso de elevar datos a dimensiones superiores para hacerlos separables.

\*   \*\*Kernel RBF:\*\* Cómo medir la similitud entre puntos usando distancias euclidianas en un espacio infinito.



---



\## 📝 Notas sobre los archivos cargados



\*   \*\*Regresion\_logistica.py\*\*: Este archivo contiene la lógica para animar la transición de un modelo lineal a uno de clasificación binaria, incluyendo una demostración con un dataset de gran escala (500 puntos).

\*   \*\*MachineLearning2\_sinkernel.py\*\*: Estos documentos pueden solo ser usados en ejecución de código. Actualmente el sistema detecta que el archivo está vacío o no tiene texto extraíble; asegúrate de que contenga la clase de Manim antes de intentar la compilación.

\*   \*\*KernelTrick (1)\_con\_kernel (1).py\*\*: Contiene escenas complejas en 3D y transformaciones matemáticas de Taylor. Requiere una GPU o mayor tiempo de procesamiento CPU dependiendo de la calidad de renderizado elegida.



---



\## 📚 Recursos Adicionales



\*   \[Documentación oficial de Manim](https://docs.manim.community/)

\*   \[Galería de ejemplos de Manim](https://docs.manim.community/en/stable/examples.html)

\*   \[Canal de 3Blue1Brown (creador original de Manim)](https://www.youtube.com/@3blue1brown)



---



\## 👥 Autores



Proyecto desarrollado como material educativo para el curso de Machine Learning.



---



\## 📄 Licencia



Este proyecto es de uso educativo.



