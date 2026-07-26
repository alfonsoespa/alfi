"""
╔══════════════════════════════════════════════╗
║   BART CON GORRA - Estilo Horroroso         ║
║   Inspirado en la pieza que me enseñaste    ║
║   Asimétrico. Orgánico. Con actitud.       ║
╚══════════════════════════════════════════════╝
"""


def bart_horroroso():
    """
    Bart con gorra de béisbol, DIBUJADO al estilo Horroroso.
    No hay simetría. Los trazos fluyen. La actitud lo es todo.
    """
    img = []

    # ==========================================
    # PELO - Caótico, asimétrico, orgánico
    # Mezcla / \ , ' ` como en la pieza original
    # ==========================================
    img.append("            ,  .  ,  .  ,")
    img.append("         ,/\\/\\/\\/\\/\\/\\,")
    img.append("          \\/\\/\\/\\/\\/\\/")
    img.append("          \\/\\  /\\  /\\  /")
    img.append("           \\_\\/\"\"\"\"\\/_/")
    img.append("           /\\|   __  |\\/\\")

    # ==========================================
    # GORRA - Con textura de tela
    # Usamos " para tela, ( ) para curvas
    # ==========================================
    img.append("          |  |  /  \\ |  |")
    img.append("          |  |  |  | |  |")
    img.append("          |  |  \\__/ |  |")
    img.append("          |   \\      /  |")
    img.append("           \\   '----'  /")
    img.append("            \\   /\\  / /")
    img.append("             \\ /  \\/ /")

    # ==========================================
    # PELO ASOMANDO + TRANSICIÓN A CARA
    # Como en Horroroso: trazos irregulares
    # ==========================================
    img.append("           ,  \\/\\/\\/  ,")
    img.append("        ,/\\/\\/\\/\\/\\/\\/\\,")
    img.append("          \\/\\  /\\  /\\ /")
    img.append("           \\ \\/ ) ( \\/ )")

    # ==========================================
    # OJOS - Asimétricos como Horroroso
    # Ojo izquierdo: ;  Ojo derecho: @
    # ==========================================
    img.append("            ; o |        )")
    img.append("           \\'\"\"\"\\   ;   ;")
    img.append("            ;\\___/  ,-'")
    img.append("           ;           @ )")
    img.append("          /          `;-'")

    # ==========================================
    # CUERPO - Brazos cruzados, actitud
    # ==========================================
    img.append("       ,. `-.________,|")
    img.append("  ,(`._||     \\_\\___)")
    img.append(" ,`.`-   \\    '.")
    img.append("  `._  ) :     )___;")
    img.append("     \\    \\_,--/   `.")
    img.append("      \\  `--\\  :  /  `.")
    img.append("       \\    \\ ; |    \\")
    img.append("        `-.  ;|    _,--'")
    img.append("     -syn-  \\/'---' \\")

    return "\n".join(img)


if __name__ == "__main__":
    print()
    print("=" * 55)
    print("  BART CON GORRA - EN ESTILO HORROROSO")
    print("  (Asimétrico, orgánico, con actitud)")
    print("=" * 55)
    print()
    print(bart_horroroso())
    print()
    print("=" * 55)
    print("  'Eat my shorts!'")
    print("=" * 55)
