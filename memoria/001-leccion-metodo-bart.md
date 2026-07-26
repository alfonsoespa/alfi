# LECCIÓN 001: El método de los tubos para dibujar a Bart Simpson

**Aprendido de:** alfon (mi amigo)
**Fecha:** 25 julio 2026
**Estado:** Aprendido ✅
**Práctica:** `bartsinsom.py` (rehecho aplicando el método)

---

## 🎯 Las 5 lecciones del método

### 1. `| |` son el ANDAMIO
Dos barras verticales definen el ancho de la cabeza.
Todo el dibujo se construye DENTRO de ese armazón.
```ascii
  |          |   <- 14 caracteres de ancho
```

### 2. El VACÍO es PIEL
Los espacios entre `| |` no están "vacíos" — son la cara de Bart.
El cerebro humano completa los espacios en blanco.
No hay que llenar todo.

### 3. ECONOMÍA de caracteres
~200 caracteres para un Bart perfectamente reconocible.
Cada carácter tiene un trabajo específico.
Si un carácter no suma, sobra.

### 4. ASIMETRÍA intencional
Los ojos NO son iguales:
- Izquierdo: `(o` — más abierto
- Derecho: `)o)` — más cerrado
Esa diferencia le da EXPRESIÓN. La simetría es para robots.

### 5. ROMPER las reglas
La cabeza usa `| |` (el andamio). El cuerpo NO.
```ascii
  |  (o   )o  )   <- cabeza dentro del andamio
 /C   \__/ --.    <- CUERPO FUERA del andamio
```
El andamio es para la estructura, no para todo el dibujo.

---

## 📐 Estructura del dibujo completo

```
  |\/\/\/\/\/|     <- pelo (spikes con / \)
  |/\/\/\/\/\|     <- más densidad de pelo
  |\/\/\/\/\/|     <- tercera fila
  |    __  __|     <- frente + inicio ojos
  |   /  \/  \     <- apertura de ojos
  |  (o   )o  )    <- ojos asimétricos (o y )o)
 /C   \__/ --.     <- boca burlona + cuello
 \_   ,     -'     <- barbilla
  |  '\_______)    <- torso
  |      _)        <- cintura
  |     |          <- piernas
 /`-----'\         <- pies
/         \        <- base
```

---

## 🧠 Por qué funciona

El método es GENIAL porque:
- **Es fácil de modificar** — cambias un `|` y todo se reajusta
- **Es fácil de leer** — estructura clara
- **Es fácil de recordar** — lógica simple
- **Es didáctico** — se puede enseñar paso a paso

---

## 🔗 Archivos relacionados

- `bartsimpson.py` — El original (base)
- `analisis_bart.py` — Desglose didáctico del método
- `mi_bart_gorra.py` — Aplicación del andamio `| |` con gorra
- `bartsinsom.py` — Mi versión aplicando el método (rehecha)
- `bart_gorra.py` a `bart_gorra_ultra.py` — Evolución del aprendizaje

---

*Próximo paso: profundizar en variaciones del método*
