"""
╔══════════════════════════════════════════════╗
║   BART SIMPSON - CON GORRA DE BÉISBOL      ║
║   Versión 2.0 - Integración pelo+gorra     ║
╚══════════════════════════════════════════════╝

Estrategia:
  - Gorra de béisbol simple (vista frontal)
  - El pelo de Bart rodea la gorra por los lados
  - La visera es el elemento que conecta gorra con cara
"""


def bart_gorra_v2():
    """Bart con gorra integrada. Intento más limpio."""
    img = []

    # ==========================================
    # CAPA 1: CÚPULA DE LA GORRA (centro arriba)
    # ==========================================
    img.append("              ,-\"\"\"\"-.")
    img.append("             /        \\")
    img.append("            |   ____   |")
    img.append("            |  /    \\  |")
    img.append("            |  |    |  |")
    img.append("            |  \\____/  |")

    # ==========================================
    # CAPA 2: VISERA Y TRANSICIÓN AL PELO
    # ==========================================
    # La visera se curva hacia afuera.
    # El pelo empieza a aparecer a los lados.
    # ==========================================
    img.append("             \\  ,--,  /")
    img.append("              \\/    \\/")
    img.append("               \\    /")
    img.append("                \\  /")

    # ==========================================
    # CAPA 3: PELO EXPLOTANDO A LOS LADOS
    # ==========================================
    img.append("     ,  ,  ,    \\/    ,  ,  ,")
    img.append("   ,/\\/\\/\\/\\  /\\/\\  /\\/\\/\\/\\,")
    img.append("   \\/\\/\\/\\/\\ \\  / \\/\\/\\/\\/\\/")
    img.append("   \\/\\  /\\  / \\/  \\/ \\  /\\  /")

    # ==========================================
    # CAPA 4: OJOS - EL ALMA DE BART
    # ==========================================
    img.append("    \\ \\/ ( @)    (@ ) \\/ /")
    img.append("     \\    \\   --   /    /")
    img.append("      \\    \\_____/    /")

    # ==========================================
    # CAPA 5: BOCA BURLONA
    # ==========================================
    img.append("       \\            /")
    img.append("        \\   ____   /")
    img.append("         \\ /    \\ /")
    img.append("          \\      /")
    img.append("           \\____/")

    # ==========================================
    # CAPA 6: CUELLO
    # ==========================================
    img.append("            |  |  |")
    img.append("            |  |  |")
    img.append("           /   |   \\")
    img.append("          /    |    \\")

    return "\n".join(img)


def bart_gorra_atras():
    """
    Versión alternativa: GORRA HACIA ATRÁS.
    La visera está en la nuca (no se ve).
    Solo vemos la cúpula redondeada detrás del pelo.
    ES MÁS FÁCIL porque el pelo es el protagonista.
    """
    img = []

    # ==========================================
    # CAPA 1: PELO (arriba, como siempre)
    # ==========================================
    img.append("          ,  .  ,  .  ,")
    img.append("        ,/\\/\\/\\/\\/\\/\\,")
    img.append("        \\/\\/\\/\\/\\/\\/")
    img.append("        \\/\\  /\\  /\\  /")

    # ==========================================
    # CAPA 2: GORRA ASOMANDO ENTRE EL PELO
    # ==========================================
    # La gorra está detrás del pelo, pero asoma
    # como una curva suave entre las puntas.
    # ==========================================
    img.append("        /\\ \\/ \"\" \\/ /\\")
    img.append("       /  \\/      \\/  \\")
    img.append("      /   /        \\   \\")
    img.append("     /   /   ____   \\   \\")
    img.append("    /   |   /    \\   |   \\")

    # ==========================================
    # CAPA 3: OJOS
    # ==========================================
    img.append("    \\    \\  (@)(@)  /    /")
    img.append("     \\    \\   --   /    /")
    img.append("      \\    \\_____/    /")

    # ==========================================
    # CAPA 4: BOCA
    # ==========================================
    img.append("       \\            /")
    img.append("        \\   ____   /")
    img.append("         \\ /    \\ /")
    img.append("          \\      /")
    img.append("           \\____/")

    # ==========================================
    # CAPA 5: CUELLO
    # ==========================================
    img.append("            |  |  |")
    img.append("            |  |  |")
    img.append("           /   |   \\")
    img.append("          /    |    \\")

    return "\n".join(img)


if __name__ == "__main__":
    import sys

    print("=" * 55)
    print("  BART - GORRA HACIA ADELANTE (v2)")
    print("=" * 55)
    print()
    print(bart_gorra_v2())
    print()
    print("=" * 55)
    print("  BART - GORRA HACIA ATRÁS")
    print("=" * 55)
    print()
    print(bart_gorra_atras())
