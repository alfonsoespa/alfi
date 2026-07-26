"""
╔══════════════════════════════════════════════╗
║   ANALISIS DIDACTICO - BART SIMPSON         ║
║   Entendiendo la estructura paso a paso     ║
╚══════════════════════════════════════════════╝
"""

# =============================================
# PIEZA ORIGINAL (usando listas para análisis)
# =============================================
BART = [
    "  |\\/\\/\\/\\/\\/|",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |    __  __|",
    "  |   /  \\/  \\",
    "  |  (o   )o  )",
    " /C   \\__/ --.",
    " \\_   ,     -'",
    "  |  '\\_______)",
    "  |      _)",
    "  |     |",
    " /`-----'\\",
    "/         \\",
]

print("=" * 70)
print("  ANALISIS DE LA ESTRUCTURA")
print("=" * 70)
print()

# =============================================
# MOSTRAR PIEZA ORIGINAL
# =============================================
print("PIEZA ORIGINAL:")
print()
for line in BART:
    print("  " + line)
print()

# =============================================
# PASO 1: COLUMNA VERTEBRAL
# =============================================
print("=" * 70)
print("  PASO 1: Los | son el ESQUELETO")
print("  Definen el ancho de la cabeza (14 caracteres)")
print("=" * 70)
print()

for i, fila in enumerate(BART):
    # Resaltar solo los |
    resaltada = ""
    for c in fila:
        if c == "|":
            resaltada += "#"
        elif c == " ":
            resaltada += " "
        else:
            resaltada += "."
    print("  " + resaltada + "  <- linea " + str(i+1))

print()
print("  Los # son los bordes |")
print("  Los . son los detalles (pelo, ojos, boca)")
print("  Los espacios son la piel de la cara")
print()

# =============================================
# PASO 2: EL PELO
# =============================================
print("=" * 70)
print("  PASO 2: El pelo - serpenteo de / y \\")
print("=" * 70)
print()

print("  Linea 1:  |\\/\\/\\/\\/\\/|")
print()
print("  |          -> borde izquierdo")
print("  \\/\\/\\/\\/\\/  -> 5 picos alternando \\ y /")
print("            |  -> borde derecho")
print()
print("  Cada dos caracteres \\/ = un pico:")
print("  |\\/\\/\\/\\/\\/|")
print("   ^^ ^^ ^^ ^^ ^^")
print("   1  2  3  4  5  spikes")
print()

# =============================================
# PASO 3: LA CARA
# =============================================
print("=" * 70)
print("  PASO 3: La cara - espacio VACIO como piel")
print("=" * 70)
print()

print("  Los espacios entre | | son la PIEL.")
print("  El cerebro del que ve rellena los blancos.")
print()
print("  Lineas 2-4: Solo |           |")
print("  Eso es la CARA de Bart.")
print()

# =============================================
# PASO 4: OJOS
# =============================================
print("=" * 70)
print("  PASO 4: Los ojos - anatomia")
print("=" * 70)
print()

print("  L5:  |    __  __|")
print("  L6:  |   /  \\/  \\")
print("  L7:  |  (o   )o  )")
print()
print("  Desglose del ojo IZQUIERDO:")
print("    __    -> parpado superior")
print("   /  \\   -> apertura del ojo")
print("  (o      -> globo ocular (o) con parpado inferior ( )")
print()
print("  Desglose del ojo DERECHO:")
print("  __|    -> parpado superior (toca el borde)")
print("  \\/  \\  -> apertura del ojo")
print("   )o  ) -> pupila )o y parpado inferior )")
print()
print("  CLAVE: Los ojos NO son simetricos!")
print("  Izquierdo: abierto, con ( )")
print("  Derecho: mas cerrado, con ) )")
print("  Eso le da PERSONALIDAD")
print()

# =============================================
# PASO 5: BOCA
# =============================================
print("=" * 70)
print("  PASO 5: Boca y menton")
print("=" * 70)
print()

print("  L8:  /C   \\__/ --.")
print()
print("   /C     -> cuello de la camisa en V")
print("   \\__/   -> la boca")
print("   --.    -> sonrisa burlona")
print()
print("  La C es el CUELLO de la camiseta de Bart")
print("  \\__/ + --. = la sonrisa torcida clasica")
print()

# =============================================
# PASO 6: CUERPO
# =============================================
print("=" * 70)
print("  PASO 6: El cuerpo")
print("=" * 70)
print()

print("  L9:  \\_   ,     -'    -> barbilla + cuello")
print("  L10:  |  '\\_______)   -> torso (camiseta)")
print("  L11:  |      _)        -> cintura")
print("  L12:  |     |          -> piernas")
print("  L13: /`-----'\\         -> pies")
print("  L14:/         \\        -> base / sombra")
print()

# =============================================
# RESUMEN DE LA TECNICA
# =============================================
print("=" * 70)
print("  RESUMEN: La tecnica del TUBO con |")
print("=" * 70)
print()
print("  Tu metodo funciona porque:")
print()
print("  1. COLUMNA VERTEBRAL: | | definen el ancho")
print("     (como los bordes de una hoja de papel)")
print()
print("  2. PIEL = VACIO: Los espacios en blanco")
print("     son la carne de la cara")
print()
print("  3. SOLO DETALLES ESENCIALES: Cada caracter")
print("     tiene un trabajo especifico")
print()
print("  4. ASIMETRIA INTENCIONAL: Los ojos son")
print("     diferentes -> expresion, no simetria")
print()
print("  5. ECONOMIA: ~200 caracteres para un Bart")
print("     totalmente reconocible")
print()
print("  Lo que hace GENIAL a este estilo:")
print("  - Es FACIL de modificar (cambias un | y todo")
print("    se reajusta)")
print("  - Es FACIL de leer (estructura clara)")
print("  - Es FACIL de recordar (logica simple)")
print()
print("  Ahora... aplicare esto para crear uno nuevo.")
print()
