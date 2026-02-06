# 🎬 Visualización de Machine Learning con Manim

Este repositorio contiene el código fuente para generar videos educativos sobre algoritmos fundamentales de Machine Learning, enfocados específicamente en **Clasificación Binaria**, **SVM (Support Vector Machines)** y el **Kernel Trick**.

Las animaciones han sido desarrolladas utilizando [Manim](https://www.manim.community/), una librería de Python para animaciones matemáticas programáticas.

---

## 📂 Contenido del Proyecto

El proyecto se divide en tres módulos principales:

* **Regresión Logística (`Regresion_logistica.py`):**  
  Visualiza el flujo completo de la regresión logística: desde el cálculo del score lineal, pasando por la función sigmoide para obtener probabilidades, hasta la definición de la frontera de decisión y la evaluación con métricas (Accuracy, Precision, Recall).

* **SVM y el Kernel Trick (`KernelTrick (1)_con_kernel (1).py`):**  
  Una explicación visual profunda sobre cómo tratar datos no separables linealmente (como el problema XOR). Incluye mapeo de características de 2D a 3D y una visualización geométrica del Kernel RBF (Gaussiano).

* **SVM Lineal (`MachineLearning2_sinkernel.py`):**  
  Enfoque en la separación de clases mediante hiperplanos de máximo margen en espacios de características originales sin transformaciones de kernel.

---

## 🛠️ Requisitos (Requirements)

Para poder ejecutar y compilar estos videos, necesitas:

1. **Python 3.8 o superior.**  
2. **Manim y sus dependencias del sistema:**  
   * FFmpeg (para renderizado de video)  
   * LaTeX (opcional, para fórmulas)  
   * Pango, Cairo y otras librerías gráficas  

### Instalación de Manim

```bash

pip install manim
```



### 🚀 Cómo Ejecutar y Compilar (How to Build)
Para generar los videos desde los archivos .py, usa la terminal dentro de la carpeta del proyecto.

1. Compilar la animación de Regresión Logística
```bash

manim -pql Regresion_logistica.py ClassificationRegressionDemo
```
2. Compilar la animación del Kernel Trick (3D)

   
```bash

manim -pql "KernelTrick (1)_con_kernel (1).py" KernelTrickFull
```
Explicación de los comandos
manim: Ejecuta la herramienta.
-p: Modo Preview (abre el video automáticamente).
-ql: Calidad baja (480p).
Usa -pqh para alta calidad (1080p).
archivo.py: Script a renderizar.
NombreClase: Clase dentro del script que contiene la animación.
### 📊 Conceptos Explicados en los Videos
Frontera de Decisión: Línea o plano que divide las clases.
Función Sigmoide: Transforma scores en probabilidades entre 0 y 1.
Feature Expansion: Expansión de características para hacer datos separables.
Kernel RBF: Función de similitud basada en distancia euclidiana.
### 📝 Notas sobre los Archivos
Regresion_logistica.py: Incluye demostración con un dataset de 500 puntos.
MachineLearning2_sinkernel.py:
Si aparece vacío, verifica que contenga la clase de Manim antes de compilar.
KernelTrick (1)_con_kernel (1).py:
Contiene escenas complejas 3D; puede requerir GPU o tiempo de renderizado elevado.
### 📚 Recursos Adicionales
Documentación oficial de Manim
Galería de ejemplos
Canal de 3Blue1Brown
### 👥 Autores
Proyecto desarrollado como material educativo para el curso de Machine Learning.

📄 Licencia
Este proyecto es de uso educativo.
