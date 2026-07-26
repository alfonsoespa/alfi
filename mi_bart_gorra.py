"""
APRENDIZAJE: BART CON GORRA
Aplicando el metodo de los |
como columna vertebral
"""

import sys

def p(s=""):
    print(s)

def sep(titulo):
    p()
    p("=" * 68)
    p("  " + titulo)
    p("=" * 68)
    p()

# =============================================
# PASO 1: El esqueleto
# =============================================
sep("PASO 1: EL ESQUELETO")

ESQUELETO = [
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
    "  |          |",
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

p("  El esqueleto vacio:")
p()
for linea in ESQUELETO:
    p("  " + linea)
p()

# =============================================
# PASO 2: La gorra
# =============================================
sep("PASO 2: LA GORRA DENTRO DE LOS | |")

GORRA = [
    "  | .-\"\"-.   |",
    "  |/  __  \\  |",
    "  || /  \\ |  |",
    "  || \\__/ |  |",
    "  | \\    /   |",
    "  |  '--'    |",
]

p("  Gorra dentro del armazon | |:")
p()
for linea in GORRA:
    p("  " + linea)
p()

# =============================================
# PASO 3: Pelo + cara
# =============================================
sep("PASO 3: PELO ASOMANDO DEBAJO")

PELO_Y_CARA = [
    "  |\\/\\/\\/\\/\\/|",
    "  |          |",
    "  |          |",
    "  |    __  __|",
    "  |   /  \\/  \\",
    "  |  (o   )o  )",
]

p("  Misma tecnica que tu original, pero debajo de la gorra:")
p()
for linea in PELO_Y_CARA:
    p("  " + linea)
p()

# =============================================
# PASO 4: Cuerpo
# =============================================
sep("PASO 4: CUERPO (rompiendo los | |)")

CUERPO = [
    " /C   \\__/ --.",
    " \\_   ,     -'",
    "  |  '\\_______)",
    "  |      _)",
    "  |     |",
    " /`-----'\\",
    "/         \\",
]

p("  El cuerpo sale de los | |:")
p()
for linea in CUERPO:
    p("  " + linea)
p()

# =============================================
# PIEZA COMPLETA
# =============================================
sep("RESULTADO: BART CON GORRA DE BEISBOL")
p("  Construido con tu metodo")
p()

COMPLETO = GORRA + PELO_Y_CARA + CUERPO
for linea in COMPLETO:
    p("  " + linea)

p()
sep("LO QUE APRENDI")
p("""
  1. LOS | | SON EL ANDAMIO:
     Definen el ancho y mantienen la proporcion.

  2. EL VACIO ES PIEL:
     No llenar todo, dejar que el cerebro complete.

  3. ECONOMIA:
     Cada caracter tiene un trabajo.

  4. ASIMETRIA:
     Ojos diferentes = expresion viva.

  5. SABER ROMPER REGLAS:
     La cabeza usa | |, el cuerpo no.
""")
