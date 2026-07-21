# Sistema de Gestión de Pedidos y Descuentos

Este repositorio contiene un script ejecutable escrito en Python que simula un sistema de menú de productos, cálculo automático de promociones por categorías y gestión de entregas (para llevar o consumir en el local).

---

## 📌 Características principales

- **Menú interactivo:** Muestra una lista estructurada de productos con su categoría y precio base.
- **Reglas de negocio automáticas:** Evalúa la categoría del producto seleccionado y determina el umbral de precio (`umbral_precio`) necesario para aplicar un porcentaje de descuento.
- **Opción de empaque:** Permite seleccionar si el pedido es para llevar o para consumir en el local, aplicando un recargo por empaque cuando corresponda.
- **Validación de entradas:** Implementa funciones de control de excepciones (`try-except`) para evitar errores por entradas inválidas en la terminal.

---

## 🛠️ Requisitos e Instalación

### Prerrequisitos

- **Python 3.8+** (Probado y compatible con intérpretes estándar de Python).
- **Git** (Para la clonación e interacción con el repositorio).

### Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```

2. Accede al directorio del proyecto:
   ```bash
   cd TU_REPOSITORIO
   ```

---

## 🚀 Uso del Programa

Para ejecutar la aplicación desde la terminal de comandos (`bash`, `zsh` o `fish`), ejecuta el siguiente comando:

```bash
python main.py
```

---

## 💻 Comandos para Subir el Código a GitHub

Si deseas inicializar o actualizar este proyecto en tu repositorio remoto de GitHub, ejecuta los siguientes comandos en tu terminal:

```bash
# 1. Inicializar el repositorio local (si no se ha hecho previamente)
git init

# 2. Agregar los archivos al área de preparación (staging area)
git add main.py README.md

# 3. Registrar los cambios con un mensaje explicativo
git commit -m "feat: implementa seleccion automatica de umbral y opcion para llevar"

# 4. Establecer la rama principal
git branch -M main

# 5. Vincular el repositorio local con el remoto en GitHub
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git

# 6. Subir los cambios a GitHub
git push -u origin main
```
