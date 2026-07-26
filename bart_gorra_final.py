"""
╔══════════════════════════════════════════════╗
║   BART SIMPSON - GORRA DE BÉISBOL FINAL     ║
║   Versión refinada con mejores proporciones ║
╚══════════════════════════════════════════════╝

Lecciones aprendidas en el camino:
  - El pelo de Bart debe ser el protagonista visual
  - La gorra va ARRIBA, el pelo DEBAJO (como en la vida real)
  - Menos es más: cuanto más simple, más legible
  - Las proporciones importan: cabeza grande, cuerpo pequeño
"""


def bart_gorra_final():
    """
    Versión definitiva.
    Gorra arriba. Pelo intacto. Cuerpo proporcionado.
    """
    img = []

    # ==========================================
    # GORRA DE BÉISBOL (arriba)
    # ==========================================
    # Simple, limpia, reconocible.
    # Sin demasiados detalles que compitan con el pelo.
    # ==========================================
    img.append("           .-\"\"\"\"-.")
    img.append("          /        \\")
    img.append("         |    __    |")
    img.append("         |   /  \\   |")
    img.append("         |   |  |   |")
    img.append("         |   \\__/   |")
    img.append("          \\        /")
    img.append("           \\      /")
    img.append("            '----'")

    # ==========================================
    # PELO DE BART (explota desde debajo)
    # ==========================================
    # Usamos la técnica orgánica: mezcla de / \ ,
    # El pelo toca la gorra pero se expande hacia afuera
    # ==========================================
    img.append("         ,  ,  ,  ,  ,")
    img.append("       ,/\\/\\/\\/\\/\\/\\,")
    img.append("       \\/\\/\\/\\/\\/\\/")
    img.append("       \\/\\  /\\  /\\  /")

    # ==========================================
    # TRANSICIÓN PELO -> CARA
    # ==========================================
    img.append("        \\ \\/ ) ( \\/ /")

    # ==========================================
    # OJOS (el alma de Bart)
    # ==========================================
    # @ para la pupila maliciosa
    # Separados pero no demasiado
    # ==========================================
    img.append("         \\(@)  (@)/")
    img.append("         /   --   \\")

    # ==========================================
    # BOCA BURLONA
    # ==========================================
    # La sonrisa torcida que solo Bart tiene
    # ==========================================
    img.append("        /  ______  \\")
    img.append("       /  /      \\  \\")
    img.append("       \\  \\______/  /")
    img.append("        \\          /")
    img.append("         \\________/")

    # ==========================================
    # CUELLO
    # ==========================================
    # Más corto que antes para mejor proporción
    # ==========================================
    img.append("           |  |  |")
    img.append("           |  |  |")

    # ==========================================
    # CUERPO (ahora más proporcionado)
    # ==========================================
    # Hombros y brazos en jarra
    # Usamos / \ para los brazos
    # ==========================================
    img.append("          /   |   \\")
    img.append("         /    |    \\")
    img.append("        /     |     \\")
    img.append("       /      |      \\")

    return "\n".join(img)


if __name__ == "__main__":
    print()
    print("=" * 50)
    print("  BART SIMPSON CON GORRA DE BÉISBOL")
    print("  Versión final - Aprendizaje completado")
    print("=" * 50)
    print()
    print(bart_gorra_final())
    print()
    print("=" * 50)
    print("  Con frase clásica:")
    print("=" * 50)
    print()
    print(bart_gorra_final() + """
     ___________________________
    /                           \\
   |   \"EAT MY SHORTS!\"         |
    \\___________________________/""")
