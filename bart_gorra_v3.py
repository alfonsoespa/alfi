"""
╔══════════════════════════════════════════════╗
║   BART SIMPSON - GORRA DE BÉISBOL v3       ║
║   Concepto: El pelo indomable               ║
║   La gorra está presente, pero el pelo      ║
║   de Bart es TAN grande que la rodea        ║
╚══════════════════════════════════════════════╝
"""


def bart_pelo_gorra():
    """
    Estrategia:
    - El PELO es el elemento principal (arriba y lados)
    - La GORRA está en el CENTRO, como una isla en medio del pelo
    - El pelo sale por ARRIBA de la gorra y por los LADOS
    - La visera asoma al FRENTE, con pelo rodeándola
    """
    img = []

    # ==========================================
    # CAPA 1: PELO SUPERIOR (domina la escena)
    # ==========================================
    img.append("           ,  .  ,  .  ,")
    img.append("         ,/\\/\\/\\/\\/\\/\\,")
    img.append("         \\/\\/\\/\\/\\/\\/")
    img.append("         \\/\\  /\\  /\\  /")

    # ==========================================
    # CAPA 2: GORRA (centrada, rodeada de pelo)
    # ==========================================
    # El pelo se aparta para mostrar la gorra
    # La gorra tiene su cúpula y panel frontal
    # ==========================================
    img.append("         /\\ \\/\"\"\"\"\"\\/ /\\")
    img.append("        /  \\/      \\/  \\")
    img.append("       /   |   __   |   \\")
    img.append("      /    |  /  \\  |    \\")
    img.append("      |    |  |  |  |    |")
    img.append("      |    |  \\__/  |    |")

    # ==========================================
    # CAPA 3: VISERA + PELO COSTADOS
    # ==========================================
    # La visera sobresale al frente
    # El pelo acompaña por los costados
    # ==========================================
    img.append("      |     \\      /     |")
    img.append("      |      \\    /      |")
    img.append("      |       '--'       |")
    img.append("       \\     /  \\      /")
    img.append("        \\   /    \\    /")
    img.append("         \\ /  /\\  \\  /")
    img.append("          /  /  \\  \\/")
    img.append("         /  /    \\  \\")

    # ==========================================
    # CAPA 4: OJOS + PELO INFERIOR
    # ==========================================
    img.append("        /  (@)  (@)  \\")
    img.append("       /    ----     \\")
    img.append("      /               \\")

    # ==========================================
    # CAPA 5: BOCA
    # ==========================================
    img.append("      |     ______     |")
    img.append("      |    /      \\    |")
    img.append("      |    \\______/    |")
    img.append("       \\             /")
    img.append("        \\           /")
    img.append("         \\_________/")

    # ==========================================
    # CAPA 6: CUELLO
    # ==========================================
    img.append("           |  |  |")
    img.append("           |  |  |")
    img.append("          /   |   \\")
    img.append("         /    |    \\")

    return "\n".join(img)


# Versión alternativa más simple y directa
def bart_gorra_simple():
    """
    Versión ultra simple:
    - Gorra pequeña arriba
    - Pelo grande debajo (como si la gorra no pudiera contenerlo)
    - Cara normal debajo
    """
    img = []

    # Gorra pequeña arriba
    img.append("            ,-\"\"\"\"-.")
    img.append("           /        \\")
    img.append("          |    __    |")
    img.append("          |   /  \\   |")
    img.append("          |   |  |   |")
    img.append("          |   \\__/   |")
    img.append("           \\        /")
    img.append("            \\      /")
    img.append("             '----'")

    # Pelo EXPLOTA desde debajo de la gorra
    img.append("          ,  ,  ,  ,  ,")
    img.append("        ,/\\/\\/\\/\\/\\/\\,")
    img.append("        \\/\\/\\/\\/\\/\\/")
    img.append("        \\/\\  /\\  /\\  /")

    # Transición pelo -> cara
    img.append("         \\ \\/ ) ( \\/ /")

    # Ojos
    img.append("          \\(@)  (@)/")

    # Boca burlona
    img.append("          /   --   \\")
    img.append("         /  ______  \\")
    img.append("        /  /      \\  \\")
    img.append("        \\  \\______/  /")
    img.append("         \\          /")
    img.append("          \\________/")

    # Cuello y cuerpo
    img.append("            |  |  |")
    img.append("            |  |  |")
    img.append("           /   |   \\")
    img.append("          /    |    \\")

    return "\n".join(img)


if __name__ == "__main__":
    print("=" * 55)
    print("  VERSIÓN A: Gorra en medio del pelo")
    print("  (El pelo rodea la gorra)")
    print("=" * 55)
    print()
    print(bart_pelo_gorra())
    print()
    print("=" * 55)
    print("  VERSIÓN B: Gorra arriba, pelo debajo")
    print("  (El pelo explota desde abajo)")
    print("=" * 55)
    print()
    print(bart_gorra_simple())
