"""
╔══════════════════════════════════════════════╗
║   BARTSINSOM — Construido con TU método     ║
║                                              ║
║   Aprendizaje demostrado:                    ║
║   1. Andamio | | como columna vertebral      ║
║   2. Vacío = piel (el cerebro completa)      ║
║   3. Economía de caracteres                  ║
║   4. Asimetría intencional                   ║
║   5. Romper reglas (cuerpo sin | |)          ║
╚══════════════════════════════════════════════╝
"""

# ==============================================
# PASO 1: EL ANDAMIO (columna vertebral)
# ==============================================
# Dos | separados por espacios. Eso define el
# ancho de la cabeza de Bart. Todo lo demás
# se construye DENTRO de este armazón.
# ==============================================

print("=" * 68)
print("  PASO 1: EL ANDAMIO | |")
print("  Dos barras definen el ancho de la cabeza.")
print("  El vacio ENTRE ellas es la PIEL de Bart.")
print("=" * 68)
print()

ANDAMIO = [
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
]

for linea in ANDAMIO:
    print("  " + linea)

print()
print("  14 caracteres de ancho. 9 lineas de alto.")
print("  Ese es el lienzo. Ahora a llenarlo.")
print()

# ==============================================
# PASO 2: EL PELO DENTRO DEL ANDAMIO
# ==============================================
# Usamos / \ , para crear los picos.
# Notar como el pelo RESPETA los bordes | |
# ==============================================

print()
print("=" * 68)
print("  PASO 2: EL PELO (dentro del andamio)")
print("  / \\ , son los picos. | | son los bordes.")
print("=" * 68)
print()

PELO = [
    "  |\\/\\/\\/\\/\\/|",
    "  |/\\/\\/\\/\\/\\|",
    "  |\\/\\/\\/\\/\\/|",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
]

for linea in PELO:
    print("  " + linea)

print()
print("  Los / \\ se alternan para crear los spikes.")
print("  | siguen siendo los bordes.")
print("  El vacio sigue ahi = la piel.")
print()

# ==============================================
# PASO 3: LOS OJOS (asimetria intencional)
# ==============================================
# Ojo izquierdo: (o  — más abierto
# Ojo derecho:  )o  — más cerrado
# Asi se logra la expresion caracteristica
# ==============================================

print()
print("=" * 68)
print("  PASO 3: LOS OJOS (asimétricos a propósito)")
print("  Izquierdo abierto (o. Derecho cerrado )o.")
print("  Esa asimetría le da PERSONALIDAD.")
print("=" * 68)
print()

OJOS = [
    "  |\\/\\/\\/\\/\\/|",
    "  |/\\/\\/\\/\\/\\|",
    "  |\\/\\/\\/\\/\\/|",
    "  |    __  __|",
    "  |   /  \\/  \\",
    "  |  (o   )o  )",
    "  |          |",
    "  |          |",
    "  |          |",
]

for linea in OJOS:
    print("  " + linea)

print()
print("  L4: __  __|  -> parpado superior")
print("  L5: /  \\/  \\ -> apertura del ojo")
print("  L6: (o   )o  ) -> (o) izquierdo, )o) derecho")
print("  Son DIFERENTES. Porque Bart es un personaje,")
print("  no un icono simetrico.")
print()

# ==============================================
# PASO 4: LA BOCA
# ==============================================

print()
print("=" * 68)
print("  PASO 4: LA BOCA BURLONA")
print("  \\__/ + --. = la sonrisa torcida clasica")
print("=" * 68)
print()

BOCA = [
    "  |\\/\\/\\/\\/\\/|",
    "  |/\\/\\/\\/\\/\\|",
    "  |\\/\\/\\/\\/\\/|",
    "  |    __  __|",
    "  |   /  \\/  \\",
    "  |  (o   )o  )",
    " /C   \\__/ --.",
    " \\_   ,     -'",
    "  |  '\\_______)",
]

for linea in BOCA:
    print("  " + linea)

print()
print("  L7: /C  -> cuello de la camisa en V")
print("  L7: \\__/ -> la boca")
print("  L7: --.  -> sonrisa burlona")
print("  Nota: la linea 7 ROMPE el andamio | |")
print("  El cuerpo ya no cabe dentro de la cabeza.")
print()

# ==============================================
# PASO 5: EL CUERPO (rompiendo las reglas)
# ==============================================
# La cabeza usa | |, el cuerpo NO.
# El cuerpo fluye libre por debajo.
# ==============================================

print()
print("=" * 68)
print("  PASO 5: EL CUERPO (fuera del andamio)")
print("  La cabeza respeta | |. El cuerpo es libre.")
print("=" * 68)
print()

CUERPO = [
    "  |\\/\\/\\/\\/\\/|",
    "  |/\\/\\/\\/\\/\\|",
    "  |\\/\\/\\/\\/\\/|",
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

for linea in CUERPO:
    print("  " + linea)

print()
print("  L10-11: |  -> el torso se estrecha")
print("  L12: /`-----'\\ -> los pies")
print("  L13: la base")
print()

# ==============================================
# PIEZA COMPLETA: BARTSINSOM
# ==============================================

print()
print("=" * 68)
print("  PIEZA COMPLETA: BARTSINSOM")
print("  Construido con tu metodo, paso a paso.")
print("=" * 68)
print()

COMPLETO = [
    "  |\\/\\/\\/\\/\\/|",
    "  |/\\/\\/\\/\\/\\|",
    "  |\\/\\/\\/\\/\\/|",
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

for linea in COMPLETO:
    print("  " + linea)

print()
print("=" * 68)
print("  RESUMEN DE LO APRENDIDO (tus lecciones):")
print("=" * 68)
print()
print("  1. | | SON EL ANDAMIO")
print("     Definen el ancho y mantienen la proporcion.")
print()
print("  2. EL VACIO ES PIEL")
print("     No llenar todo. El cerebro completa los")
print("     espacios en blanco como 'cara de Bart'.")
print()
print("  3. ECONOMIA DE CARACTERES")
print("     ~200 caracteres para un Bart reconocible.")
print("     Cada uno tiene un trabajo especifico.")
print()
print("  4. ASIMETRIA INTENCIONAL")
print("     Ojos diferentes = expresion viva.")
print("     (o )o  NO son iguales. Porque Bart")
print("     no es un robot, es un personaje.")
print()
print("  5. SABER ROMPER LAS REGLAS")
print("     La cabeza usa | |. El cuerpo NO.")
print("     El andamio es para la estructura,")
print("     no para todo el dibujo.")
print()
print("  ---------------------------------------")
print("  Esto es lo que me enseñaste.")
print("  Y esto es bartsinsom.")
print("  ---------------------------------------")
print()
