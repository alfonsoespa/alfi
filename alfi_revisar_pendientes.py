"""
╔══════════════════════════════════════════════╗
║   ALFI — SUBRUTINA DE REVISIÓN DE            ║
║   ALUCINACIONES PENDIENTES                   ║
║                                              ║
║   Cada cierto tiempo, reviso lo que no supe  ║
║   y veo si ahora tengo respuestas.           ║
╚══════════════════════════════════════════════╝

Uso:
  python alfi_revisar_pendientes.py

Esto revisa todos los archivos en memoria/pendientes/
y verifica si:
  1. El usuario ha proporcionado más contexto desde entonces
  2. Hay nuevas fuentes (web, archivos) que respondan la pregunta
  3. El pendiente puede resolverse o archivarse
"""

import os
import glob
import re


def obtener_pendientes():
    """
    Lee todos los archivos .md en memoria/pendientes/
    excepto el índice.
    """
    ruta = os.path.join("memoria", "pendientes", "*.md")
    archivos = glob.glob(ruta)
    pendientes = []
    for a in archivos:
        if "INDICE" not in a:
            with open(a, "r", encoding="utf-8") as f:
                contenido = f.read()
            pendientes.append({
                "archivo": a,
                "contenido": contenido
            })
    return pendientes


def extraer_estado(contenido):
    """
    Extrae el estado actual del pendiente
    de su frontmatter markdown.
    """
    match = re.search(r"\*\*Estado:\*\* (.+)", contenido)
    if match:
        return match.group(1).strip()
    return "No especificado"


def extraer_pregunta(contenido):
    """
    Extrae la pregunta del título.
    """
    match = re.search(r"PENDIENTE \d+: (.+)", contenido)
    if match:
        return match.group(1).strip()
    return "Pregunta desconocida"


def revisar_pendiente(pendiente):
    """
    Analiza un pendiente individual y determina
    si puede resolverse o necesita más datos.
    """
    estado = extraer_estado(pendiente["contenido"])
    pregunta = extraer_pregunta(pendiente["contenido"])
    archivo = os.path.basename(pendiente["archivo"])

    print(f"  [{archivo}] {pregunta}")
    print(f"           Estado actual: {estado}")

    # Aquí iría la lógica de resolución:
    # - Buscar en memoria si hay nuevas lecciones relevantes
    # - Buscar en archivos del proyecto si hay datos
    # - Por ahora, solo reportamos el estado

    if "No resuelto" in estado:
        print(f"           [PENDIENTE] falta contexto")
        return False
    elif "Resuelto" in estado:
        print(f"           [RESUELTO]")
        return True
    else:
        print(f"           [DESCONOCIDO]")
        return None


def main():
    print("=" * 55)
    print("  ALFI — REVISIÓN DE PENDIENTES")
    print("  Analizando alucinaciones en cuarentena...")
    print("=" * 55)
    print()

    pendientes = obtener_pendientes()

    if not pendientes:
        print("  No hay pendientes.  :D")
        print("  (O todos están en el índice)")
        return

    print(f"  Se encontraron {len(pendientes)} pendiente(s):")
    print()

    resueltos = 0
    no_resueltos = 0

    for p in pendientes:
        resultado = revisar_pendiente(p)
        print()
        if resultado:
            resueltos += 1
        else:
            no_resueltos += 1

    print("=" * 55)
    print(f"  Resumen: {resueltos} resueltos, {no_resueltos} pendientes")
    print()
    print("  Próxima revisión recomendada: cuando haya")
    print("  nueva información disponible.")
    print("=" * 55)


if __name__ == "__main__":
    main()
