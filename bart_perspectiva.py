"""
BART CON GORRA - CON PERSPECTIVA 3/4
Aplicando las lecciones de tu original
"""

import sys

def p(s=""):
    print(s)

def sep(titulo):
    p()
    p("=" * 70)
    p("  " + titulo)
    p("=" * 70)
    p()

# =============================================
# ANALISIS DE LA PERSPECTIVA
# =============================================
sep("ANALISIS DE PERSPECTIVA EN TU ORIGINAL")

p("  Esquema de posiciones (0-13):")
p()
p("  0 1 2 3 4 5 6 7 8 9 0 1 2 3")
p("  -----------------------------")
p("  |   |   | o |   | o |   |    <- ojos")
p("  C   |   |   |   | --.        <- cuello + boca")
p()
p("  Cuello (C) en pos 2 = IZQUIERDA")
p("  Boca (--.) en pos 11 = DERECHA")
p("  -> Cabeza gira hacia la IZQUIERDA")
p("  -> Lado IZQUIERDO esta MAS CERCA")
p()

# =============================================
# INTENTO 1: Gorra suelta (desconectada)
# =============================================
sep("INTENTO 1: Gorra SIN conectar a | |")

GORRA_SUELTA = [
    "   ,-\"\"-.    ",
    "  /   __  \\   ",
    "  |  /  \\  )  ",
    "  |  \\__/ (   ",
    "   \\     /    ",
    "    '---'     ",
]

p("  La gorra sola, sin los | |:")
p()
for linea in GORRA_SUELTA:
    p("  " + linea)
p()

CABEZA_CUERPO = [
    "  |\\/\\/\\/\\/\\/|",
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

p("  Cabeza + cuerpo (tu original):")
p()
for linea in CABEZA_CUERPO:
    p("  " + linea)
p()

p("  PROBLEMA: La gorra flota sobre la cabeza.")
p("  No comparte el mismo sistema de | |.")
p()

# =============================================
# INTENTO 2: Gorra DENTRO de los | | con perspectiva
# =============================================
sep("INTENTO 2: Gorra DENTRO de | | con perspectiva")

p("  Ahora la gorra respeta los | |")
p("  pero tiene perspectiva INTERNA:")
p()

COMPLETO = [
    "  | .-\"\"-..  |",
    "  |/  __  \\  |",
    "  || /  \\ )  |",
    "  || \\__/ (  |",
    "  | \\    /   |",
    "  |  '--'    |",
    "  |\\/\\/\\/\\/\\/|",
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

for linea in COMPLETO:
    p("  " + linea)

p()
p("  DIFERENCIAS con mi version anterior:")
p()
p("  Linea 1:  '..' en vez de espacios a la derecha")
p("            -> la cupula se extiende (perspectiva)")
p()
p("  Linea 3:  ')' en vez de '|' en el borde derecho")
p("            -> el lado der se curva hacia adentro")
p()
p("  Linea 4:  '(' en vez de '|' en el borde derecho")
p("            -> la curva se cierra en perspectiva")
p()

# =============================================
# INTENTO 3: GORRA INTEGRADA
# =============================================
sep("INTENTO 3: Gorra CON pelo asomando por los lados")

p("  La gorra deberia ser mas angosta que la cabeza")
p("  para que el pelo de Bart asome por los LADOS:")
p()

COMPLETO3 = [
    "  |  .-\"\"-.   |",    # Gorra mas chica, centrada
    "  | /  __  \\  |",    # 
    "  || /  \\  \\ |",    # \ extra del lado der
    "  || \\__/  / |",    # / del lado der
    "  |  \\    /   |",    # Visera
    "  |   '--'    |",    # Borde
    "  |\\/\\/\\/\\/\\/|",    # Pelo OCUPA todo el ancho
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

for linea in COMPLETO3:
    p("  " + linea)

p()
p("  Este intento tiene:")
p("  - Gorra mas angosta (8 chars) que la cabeza (10 chars)")
p("  - Pelo OCUPANDO los 10 chars (asoma por los lados)")
p("  - Un '\\' extra en L3 que sugiere profundidad")
p()

# =============================================
# LECCION FINAL
# =============================================
sep("LO QUE APRENDI SOBRE PERSPECTIVA")

p("""
  La perspectiva en ASCII art se logra con:

  1. ASIMETRIA INTENCIONAL
     El lado izquierdo y derecho NO son iguales.
     El lado mas cercano tiene mas detalle.

  2. DESPLAZAMIENTO DE EJE
     Los elementos no estan centrados.
     Cuello a la izq, boca a la der.

  3. CURVAS CON ( y )
     ( abre una curva hacia la derecha.
     ) cierra una curva hacia la izquierda.
     Juntos sugieren volumen.

  4. ESCALA
     La gorra es mas angosta que la cabeza.
     El pelo asoma por los lados de la gorra.

  5. SUPERPOSICION
     La gorra esta DELANTE del pelo.
     El pelo esta DETRAS de la gorra.
     
  La clave: cada elemento debe existir en un
  espacio tridimensional, no en un plano 2D.
""")
