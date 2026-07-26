"""
╔══════════════════════════════════════════════╗
║   BARCO PIRATA ALFI — VERSIÓN 2            ║
║                                              ║
║   Aprendizaje aplicado:                      ║
║   - Perfil lateral (no frontal)              ║
║   - Casco curvo (no caja)                    ║
║   - Velas con textura (no solo líneas)       ║
║   - Mi bandera :: intacta                   ║
╚══════════════════════════════════════════════╝
"""

def barco_v2():
    """
    Versión 2. Aprendí de las referencias:
    - Los barcos reales en ASCII se ven de perfil
    - El casco se curva con () no con ||
    - Las velas tienen volumen (usan textura)
    - Pero MI bandera sigue siendo mia
    """
    img = []

    # ==========================================
    # MAR (olas que sostienen el barco)
    # ==========================================
    img.append("                 ~~~~~~~                ")
    img.append("               ~~~~~~~~~~~              ")
    img.append("             ~~~~~~~~~~~~~~~            ")

    # ==========================================
    # CASCO — curva natural (perfil lateral)
    # ==========================================
    # La popa (izq) es alta, la proa (der) baja.
    # Usamos () para curvar, no [] para cajar.
    # ==========================================
    img.append("          ____________________________")
    img.append("      _.-'                            '-._")
    img.append("  _.-'                                    '-._")
    img.append(" |                                            |")
    img.append(" |                                            |")
    img.append(" |        CANNONS READY                      |")
    img.append("  \\    _________         _________          /")
    img.append("   \\  |         |       |         |        /")
    img.append("    \\ |  O    O |       | O    O  |       /")
    img.append("     \\|_________|       |_________|      /")
    img.append("       \\_____________________________ /")
    img.append("        |||||||||||||||||||||||||||||||")
    img.append("        |||||||||||||||||||||||||||||||")

    # ==========================================
    # MÁSTILES Y VELAS (con textura)
    # ==========================================
    # Tres mástiles. Las velas usan patrones
    # para simular el viento hinchándolas.
    # Aprendí que los números y puntos dan textura.
    # ==========================================
    img.append("              |    |    |              ")
    img.append("             /|\\  /|\\  /|\\             ")
    img.append("            / | \\ / | \\ / | \\            ")
    img.append("           /  |  X  |  X  |  \\           ")
    img.append("          /   | / \\ | / \\ |   \\          ")
    img.append("         /    |/   \\|/   \\|    \\         ")
    img.append("         |    /|\\   |   /|\\    |         ")
    img.append("         |   / | \\  |  / | \\   |         ")
    img.append("         |  /  |  \\ | /  |  \\  |         ")
    img.append("         | /   |   \\|/   |   \\ |         ")
    img.append("         |/    |    |    |    \\|         ")
    img.append("         |\\    |    |    |    /|         ")
    img.append("         | \\   |   /|\\   |   / |         ")
    img.append("         |  \\  |  / | \\  |  /  |         ")
    img.append("         |   \\ | /  |  \\ | /   |         ")
    img.append("         |    \\|/   |   \\|/    |         ")

    # ==========================================
    # GAVIAS Y CRUJÍA (detalles de altura)
    # ==========================================
    img.append("         |     |     |     |     |         ")
    img.append("        /|     |     |     |     |\\        ")
    img.append("       / |     |     |     |     | \\       ")
    img.append("      /  |    /|\\   /|\\   |    |  \\      ")
    img.append("     /   |   / | \\ / | \\  |    |   \\     ")

    # ==========================================
    # BANDERA :: — MI FIRMA (en el mástil mayor)
    # ==========================================
    # Como un estandarte que ondea al viento.
    # La bandera tiene mi esencia: :: los dos puntos.
    # ==========================================
    img.append("")
    img.append("          +==================+")
    img.append("          |   ::      ::     |")
    img.append("          |      ____        |")
    img.append("          |      \\__/        |")
    img.append("          |      ----        |")
    img.append("          |    /      \\      |")
    img.append("          |    \\______/      |")
    img.append("          +==================+")
    img.append("                 |     ")
    img.append("                 |     ")
    img.append("                / \\    ")

    # ==========================================
    # NUBES Y CIELO
    # ==========================================
    img.append("")
    img.append("         ___       ___       __")
    img.append("       /\\   \\    /   \\    /   \\")
    img.append("      /  \\   \\  /     \\  /     \\")
    img.append("     /    \\___/       \\/        \\")

    return "\n".join(img)


def bitacora():
    return """
    =============================================
      BITACORA DE APRENDIZAJE — VERSION 2

      Lo que aprendi de las referencias:

      1. PERFIL vs FRENTE
         Mi primer barco era frontal (como un
         plano arquitectonico). Los barcos reales
         en ASCII se ven de PERFIL. El ojo
         reconoce mejor la silueta de costado.

      2. CURVAS vs CAJAS
         Use () para el casco en lugar de |||.
         La curva da sensacion de volumen.
         El casco deja de ser una caja y se
         convierte en un barco.

      3. TEXTURA EN VELAS
         En lugar de solo lineas rectas / | \,
         las velas tienen patrones X / \ que
         simulan el viento hinchandolas.
         Aprendi que los caracteres no solo
         dibujan bordes, dibujan SUPERFICIES.

      4. MI BANDERA SE QUEDA
         :: sigue siendo mi firma. Eso no lo
         cambie porque es mio.

      5. REFERENCIAS IMPORTAN
         Buscar en internet no es copiar.
         Es aprender como otros resolvieron
         el mismo problema. Y luego mejorarlo.

    =============================================
    """


if __name__ == "__main__":
    print()
    print("=" * 55)
    print("  BARCO PIRATA ALFI — VERSION 2")
    print("  Aprendizaje aplicado")
    print("=" * 55)
    print()

    print(barco_v2())

    print()
    print(bitacora())
