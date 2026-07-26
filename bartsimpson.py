"""
╔══════════════════════════════════════════════╗
║   BART SIMPSON - ASCII ART GENERATOR        ║
║   Construido con curiosidad, no con copia   ║
║   Cada carácter tiene una razón de ser      ║
╚══════════════════════════════════════════════╝
"""


def construir_bart():
    """
    Construye a Bart capa por capa.
    Cada fila es una línea de la imagen final.
    Aprendemos por qué cada carácter está donde está.
    """
    bart = []

    # ==========================================
    # CAPA 1: El pelo puntiagudo (spikes)
    # ==========================================
    # Usamos comas como puntas lejanas,
    # y / y \ para crear la textura erizada.
    # Es la silueta más icónica de Bart.
    # ==========================================
    bart.append("            ,  ,  ,  ,  ,")            # puntas superiores lejanas
    bart.append("          ,/\\/\\/\\/\\/\\/\\,")        # primera hilera de spikes
    bart.append("          \\/\\/\\/\\/\\/\\/")          # segunda hilera (más densa)
    bart.append("          \\/\\  /\\  /\\  /")          # los spikes empiezan a curvarse

    # ==========================================
    # CAPA 2: La frente y la transición
    # ==========================================
    # Aquí el pelo se encuentra con la cara.
    # Usamos paréntesis para empezar a redondear.
    # ==========================================
    bart.append("           \\ \\/ ) ( \\/ /")           # transición pelo -> cara

    # ==========================================
    # CAPA 3: Los OJOS (el alma de Bart)
    # ==========================================
    # Los ojos de Bart son grandes y separados.
    # Usamos (O)(O) para la expresión clásica
    # de "sabelotodo" que lo caracteriza.
    # ==========================================
    bart.append("            \\(O)  (O)/")              # ojos saltones (O)(O)
    bart.append("            /   --   \\")              # ceño / entrecejo
    bart.append("           /  ______  \\")             # parte superior de la boca

    # ==========================================
    # CAPA 4: La boca burlona
    # ==========================================
    # La boca de Bart siempre tiene un dejo
    # de sarcasmo. Usamos / \ para la sonrisa
    # torcida característica.
    # ==========================================
    bart.append("          /  /      \\  \\")           # apertura de boca
    bart.append("         /  /        \\  \\")          # profundidad de la boca
    bart.append("         \\  \\________/  /")          # mandíbula inferior

    # ==========================================
    # CAPA 5: Barbilla y cuello
    # ==========================================
    bart.append("          \\            /")            # cierre de la barbilla
    bart.append("           \\  ______  /")             # base de la cabeza

    # ==========================================
    # CAPA 6: El cuello y la camiseta
    # ==========================================
    # El cuello son dos palos | |
    # y la camiseta tiene el clásico cuello en V
    # ==========================================
    bart.append("             |  |  |")                 # cuello (3 líneas)
    bart.append("             |  |  |")                 #
    bart.append("            /   |   \\")               # inicio del cuello de la camisa
    bart.append("           /    |    \\")              # V de la camiseta
    bart.append("          /     |     \\")             # profundidad de la V
    bart.append("         /      |      \\")            #

    # ==========================================
    # CAPA 7: El cuerpo y la actitud
    # ==========================================
    # Bart siempre tiene los brazos en jarra
    # o en los bolsillos. Usamos / para brazos.
    # ==========================================
    bart.append("        /       |       \\ ")          # hombros
    bart.append("       /        |        \\")          # brazos comenzando
    bart.append("      /         |         \\")         # brazos en jarra
    bart.append("     /          |          \\")        # antebrazos
    bart.append("    /           |           \\")       # manos en caderas

    return "\n".join(bart)


def construir_bart_con_texto():
    """Versión con el texto clásico de Bart: '¡Cómete mis shorts!'"""
    bart = construir_bart()
    texto = (
        "\n"
        "     ___________________________\n"
        "    /                           \\\n"
        '   |   "EAT MY SHORTS!"         |\n'
        "    \\___________________________/\n"
    )
    return bart + texto


# ==========================================
# EXPLORACIÓN: ¿Por qué estos caracteres?
# ==========================================
#
# Caracteres usados y su propósito:
#
#   /  \  -> Ángulos, picos del pelo, curvas de la cara
#   (  )  -> Curvas suaves (mejillas, ojos, redondez)
#   ,  '  -> Puntas finas del cabello (textura)
#   O  o  -> Pupilas de los ojos (expresión)
#   _     -> Líneas rectas (entrecejo, base de boca)
#   |     -> Líneas verticales (cuello, cuerpo)
#
# La REGLA DE ORO del ASCII art:
#   Los caracteres no son letras, son PÍXELES.
#   Cada uno tiene un peso visual:
#     - Caracteres ligeros: . , ' ` : (poco grosor)
#     - Caracteres medios: - = _ ~ (grosor medio)
#     - Caracteres pesados: # @ M W (macho grosor)
#

if __name__ == "__main__":
    print()
    print("=" * 50)
    print("  BART SIMPSON - NUESTRA CREACIÓN")
    print("=" * 50)
    print()

    print(construir_bart())

    print()
    print("=" * 50)
    print("  Versión con frase clásica:")
    print("=" * 50)
    print()

    print(construir_bart_con_texto())
