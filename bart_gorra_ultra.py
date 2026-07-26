"""
╔══════════════════════════════════════════════╗
║   BART SIMPSON - GORRA DE BÉISBOL ULTRA     ║
║   Versión más limpia y precisa               ║
╚══════════════════════════════════════════════╝
"""


def bart():
    """Bart con gorra de béisbol. Versión ultra limpia."""
    img = []

    # Gorra de béisbol
    img.append("          .-\"\"\"\"-.")
    img.append("         /        \\")
    img.append("        |    __    |")
    img.append("        |   /  \\   |")
    img.append("        |   |  |   |")
    img.append("        |   \\__/   |")
    img.append("         \\        /")
    img.append("          \\      /")
    img.append("           '----'")
    # Pelo conecta DIRECTAMENTE debajo (sin espacio)
    img.append("        ,  ,  ,  ,  ,")
    img.append("      ,/\\/\\/\\/\\/\\/\\,")
    img.append("      \\/\\/\\/\\/\\/\\/")
    img.append("      \\/\\  /\\  /\\  /")
    img.append("       \\ \\/ ) ( \\/ /")
    # Ojos
    img.append("        \\(@)  (@)/")
    # Boca simple
    img.append("        /   --   \\")
    img.append("        \\   __   /")
    img.append("         \\______/")
    # Cuello corto
    img.append("           |  |")
    img.append("           |  |")
    # Brazos más naturales
    img.append("          /    \\")
    img.append("         /      \\")

    return "\n".join(img)


if __name__ == "__main__":
    print()
    print(bart())
    print()
    print("=" * 40)
    print("  'Eat my shorts!'")
    print("=" * 40)
