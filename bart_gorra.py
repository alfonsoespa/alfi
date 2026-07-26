"""
╔══════════════════════════════════════════════╗
║   BART SIMPSON - CON GORRA DE BÉISBOL      ║
║   Versión 1.0 - Aprendiendo haciendo       ║
╚══════════════════════════════════════════════╝

Estructura (de arriba abajo):
  1. Cúpula de la gorra (redondeada)
  2. Visera al frente
  3. Pelo puntiagudo escapando de la gorra
  4. Cara con ojos saltones
  5. Cuello y camiseta
"""


def bart_con_gorra():
    """Bart Simpson luciendo una gorra de béisbol hacia adelante."""
    img = []

    # ==========================================
    # CAPA 1: CÚPULA DE LA GORRA
    # ==========================================
    # La gorra tiene una forma redondeada arriba.
    # Usamos . - " para dar la textura de tela.
    # ==========================================
    img.append("               .--\"\"--.")
    img.append("              /        \\")
    img.append("             /   ____   \\")
    img.append("            |   /    \\   |")
    img.append("            |  |      |  |")
    img.append("            |   \\____/   |")

    # ==========================================
    # CAPA 2: VISERA
    # ==========================================
    # La visera sobresale al frente.
    # Usamos / \ para darle volumen curvo.
    # ==========================================
    img.append("             \\          /")
    img.append("              \\   /\\   /")
    img.append("               \\ /  \\ /")
    img.append("                '    '")

    # ==========================================
    # CAPA 3: PELO ESCAPANDO
    # ==========================================
    # El pelo de Bart es indomable.
    # Se escapa por los lados de la gorra.
    # Usamos la técnica orgánica: / \ , mezclados
    # ==========================================
    img.append("           ,  ,  ,  ,  ,")
    img.append("         ,/\\/\\/\\/\\/\\/\\,")
    img.append("         \\/\\/\\/\\/\\/\\/")
    img.append("         \\/\\  /\\  /\\  /")

    # ==========================================
    # CAPA 4: TRANSICIÓN PELO -> CARA
    # ==========================================
    img.append("          \\ \\/ ) ( \\/ /")

    # ==========================================
    # CAPA 5: OJOS SALTONES
    # ==========================================
    # (O)(O) con @ para pupila maliciosa
    # ==========================================
    img.append("           \\(@)  (@)/")

    # ==========================================
    # CAPA 6: ENTROCEJO Y NARIZ
    # ==========================================
    img.append("           /   --   \\")

    # ==========================================
    # CAPA 7: BOCA BURLONA
    # ==========================================
    img.append("          /  ______  \\")
    img.append("         /  /      \\  \\")
    img.append("         \\  \\______/  /")

    # ==========================================
    # CAPA 8: BARBILLA
    # ==========================================
    img.append("          \\          /")
    img.append("           \\  ____ /")

    # ==========================================
    # CAPA 9: CUELLO Y CAMISETA
    # ==========================================
    img.append("             |  |  |")
    img.append("             |  |  |")
    img.append("            /   |   \\")
    img.append("           /    |    \\")
    img.append("          /     |     \\")

    # ==========================================
    # CAPA 10: HOMBROS / ACTITUD
    # ==========================================
    img.append("         /      |      \\")
    img.append("        /       |       \\")
    img.append("       /        |        \\")

    return "\n".join(img)


def bart_con_gorra_v2():
    """
    Versión 2: Gorra más integrada con el pelo.
    Aquí el pelo rodea la gorra en lugar de estar debajo.
    """
    img = []

    # Pelo rodeando la gorra por ARRIBA y los lados
    img.append("         ,  .  ,  .  ,")
    img.append("       ,/\\/\\/\\/\\/\\/\\,")
    img.append("       \\/\\/\\/\\/\\/\\/")
    img.append("       \\/\\/ .--\"\"--. /\\/")
    img.append("        \\/ /        \\/ /")
    img.append("        | |   ____  |  |")
    img.append("        | |  /    \\ |  |")
    img.append("        | | |      ||  |")
    img.append("        | |  \\____/ |  |")
    img.append("        /  \\        /  \\")
    img.append("       /    \\  /\\  /    \\")
    img.append("      /      \\/  \\/      \\")
    img.append("     /       /    \\       \\")
    img.append("    /       /      \\       \\")
    img.append("    \\   (@)\\  --  /(@)   /")
    img.append("     \\       \\____/      /")
    img.append("      \\                /")
    img.append("       \\              /")
    img.append("        \\            /")
    img.append("          |    |    |")
    img.append("          |    |    |")
    img.append("         /     |    \\")
    img.append("        /      |     \\")

    return "\n".join(img)


if __name__ == "__main__":
    print("=" * 55)
    print("  BART CON GORRA DE BÉISBOL - Versión 1")
    print("=" * 55)
    print()
    print(bart_con_gorra())
    print()
    print("=" * 55)
    print("  BART CON GORRA - Versión 2 (pelo integrado)")
    print("=" * 55)
    print()
    print(bart_con_gorra_v2())
