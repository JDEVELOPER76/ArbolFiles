import os
def listar_arbol(ruta_inicio, prefijo=""):
    try:
        elementos = sorted(os.listdir(ruta_inicio))
    except PermissionError:
        return

    i = 0

    while i < len(elementos):
        nombre = elementos[i]
        es_ultimo = i == len(elementos) - 1

        if es_ultimo:
            conector = "└── "
        else:
            conector = "├── "

        ruta_completa = os.path.join(ruta_inicio, nombre)

        print(f"{prefijo}{conector}{nombre}")

        if os.path.isdir(ruta_completa):
            if es_ultimo:
                extension_prefijo = "    "
            else:
                extension_prefijo = "│   "

            listar_arbol(ruta_completa, prefijo + extension_prefijo)

        i += 1


if __name__ == "__main__":
    carpeta_objetivo = "."

    print(f"Árbol de directorios de: {os.path.abspath(carpeta_objetivo)}")
    print(carpeta_objetivo)

    listar_arbol(carpeta_objetivo)