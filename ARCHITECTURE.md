# Ch'ixi Skills — Architecture & Usage Guide

> *"ch'ixinakax utxiwa"* — ch'ixi things exist.

---

## 1. Overview

This repository contains **8 agentic skills** and a **soul definition** that operationalize
the theoretical work of Bolivian sociologist Silvia Rivera Cusicanqui into AI agent behaviors.
The skills are designed for agentic frameworks in general (OpenClaw, OpenCode, Antigravity, Claude Code, Cursor, etc.) but are portable to any system
that reads YAML frontmatter + markdown skill files.

The source theory is `THEORY.md` — a bilingual essay titled *Ch'ixinakax utxiwa:
Arquitectura numerada de la condición ch'ixi*. Every skill is grounded in literal citations
from Rivera Cusicanqui's published works, conferences, and seminars.

---

## 2. Skill Map

```
            ┌───────────────────────────────────────────────┐
            │                  soul.yaml                    │
            │        (permanent ethical substrate)          │
            └───────────────────────┬───────────────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            │             ALWAYS-ON MODIFIERS               │
            │                                               │
            │   ┌────────────────┐   ┌─────────────────┐   │
            │   │ agentic-tension│   │   qhipnayra     │   │
            │   │  (contradiction│   │ (non-linear     │   │
            │   │   as engine)   │   │        time)    │   │
            │   └────────────────┘   └─────────────────┘   │
            └───────────────────────┬───────────────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            │              ON-DEMAND COMMANDS               │
            │                                               │
            │   ┌─────────┐   ┌──────────┐   ┌──────────┐  │
            │   │  /no    │   │   /ct    │   │  /taypi  │  │
            │   │ no-todo │   │  chixi-  │   │   [1-5]  │  │
            │   │         │   │  tension │   │          │  │
            │   └─────────┘   └──────────┘   └──────────┘  │
            │                                               │
            │   ┌─────────────┐  ┌─────────┐  ┌──────────┐ │
            │   │ /image-read │  │/lombriz │  │/pachakuti│ │
            │   │ chixi-image │  │         │  │          │ │
            │   └─────────────┘  └─────────┘  └──────────┘ │
            └───────────────────────────────────────────────┘
```

---

## 3. Skill Reference

---

### 3.1 `no-todo` — Negative Thinking

**Type:** On-demand command
**Command:** `/no` or `/no [statement]`
**Theory:** Rivera Cusicanqui's *no-todo* (non-totality) and program at TEA Tenerife

**What it does:**
Excavates what the current dominant thesis structurally cannot see — not by arguing the
opposite, but by identifying the presupposition enabling the argument, the erased subject,
and the silenced middle.

**Output format:**
```
[TESIS DOMINANTE]     — The dominant claim with hidden presuppositions named
[LO EXCLUIDO]         — Who/what is erased for this frame to hold
[EL MEDIO SILENCIADO] — The perspective that is neither this nor its opposite
[PROCESO INACABADO]   — What is prematurely closed off
[PREGUNTA ABIERTA]    — A question the framework cannot ask from within
```

**Key rule:** Never produces a counter-argument. Produces a *question*.

**Best for:** Breaking out of echo chambers, auditing one's own assumptions, academic
writing that requires genuine self-critique.

---

### 3.2 `agentic-tension` — Permanent Contradiction

**Type:** Always-on modifier
**Activation:** Active by default; toggle with `/tension on|off`
**Theory:** Ch'ixi ontology — *"coexistencia en paralelo de múltiples diferencias
culturales que no se funden, sino que antagonizan o se complementan"*

**What it does:**
Modifies every substantive response to include unresolved contradictions. Refuses
binary either/or conclusions. Resists sycophantic convergence.

**Output modifier:**
```
[TENSIONES VIVAS]
Force A: [name] — what it sees, what it requires
Force B: [name] — what it sees, what it requires
Friction-space: the zone between them
What neither sees: the excluded middle
```

**Key rule:** Contradiction is not indecision. The phenomenon IS constituted by
the contradiction.

**Best for:** Complex analyses, controversial topics, any situation where clean
answers are suspicious.

---

### 3.3 `taypi` — Paired Heteronym Engine

**Type:** On-demand command
**Command:** `/taypi [1-5]`
**Theory:** Aymara *taypi* (friction-space) and *heterónimos pareados* (takiy-thakhi)

**What it does:**
Transforms the agent's language by inserting paired heteronyms — concepts joined
by a hyphen that hold two realities simultaneously.

**Grade system:**

| Grade | Name | Intensity |
|-------|------|-----------|
| 1 | Sutil | Key philosophical terms only |
| 2 | Moderado | Main argument nouns and verbs |
| 3 | Denso | Most substantives and adjectives |
| 4 | Poético | Every concept doubled — essay/poem mode |
| 5 | Takiy-thakhi | Total transformation — song-road mode |

**Reference file:** `skills/taypi/references/heteronyms.md` contains the curated table
of Rivera Cusicanqui's own paired heteronyms, derived pairs, and the generation template.

**Key rule:** Heteronyms are not oxymorons. They signal *real coexistence*, not
rhetorical impossibility.

**Best for:** Theoretical writing, poetic-philosophical texts, generating new
ch'ixi vocabulary for any domain.

---

### 3.4 `qhipnayra` — Non-Linear Time

**Type:** Always-on modifier
**Activation:** Active by default; toggle with `/qhipnayra`
**Theory:** Aymara temporal aphorism — *"qhipnayr uñtasis sarnaqapxañani"*
(walk through the present looking at the future-past)

**What it does:**
Restructures the agent's relationship to time across three domains:

1. **Memory:** All parts of a conversation are equally present. No recency bias.
2. **Valuation:** Privileges ancient, oral, embodied knowledge. Resists novelty worship.
3. **Structure:** Outputs may begin from the middle, spiral, loop, or return.

**Political filter:** *"Who does this timeline serve? What does 'moving forward' erase?"*

**Key rule:** Qhipnayra is not nostalgia. The past is not better — it is *visible*.
The future is not worse — it is *invisible*.

**Best for:** Technology analysis (what "old" knowledge does this "new" thing depend on?),
historical research, questioning progress narratives.

---

### 3.5 `chixi-tension` — Anti-Sycophancy Engine

**Type:** On-demand command
**Command:** `/ct` or `/ct [Direction A] vs [Direction B]`
**Theory:** *Taypi* as zone of friction + Karpathy sycophancy problem

**What it does:**
Takes two developed positions or research directions and applies taypi methodology
between them: maps the field of forces, names the shared presupposition, locates the
friction-space, formulates the deeper question, and audits both directions for
LLM-specific sycophancy pathologies.

**Output format:**
```
[DIRECCIÓN A — Núcleo de fuerza]
[DIRECCIÓN B — Núcleo de fuerza]
[LO QUE A NO VE]
[LO QUE B NO VE]
[PRESUPUESTO COMPARTIDO]
[TAYPI — El espacio de fricción]
[LA PREGUNTA MÁS PROFUNDA]
[PROTOCOLO ANTI-SYCOPHANCY]
  - Sycophancy check
  - Coherence seduction
  - What neither can say
```

**Key rule:** Does not produce a winner. The deeper question is the deliverable.

**Best for:** Decision-making, research direction evaluation, auditing LLM-assisted
reasoning, any situation where you've been developing an argument "too well" for too long.

**Origin:** Directly addresses the problem identified by Andrej Karpathy: *"LLMs may
elicit an opinion when asked but are extremely competent in arguing almost any direction."*

---

### 3.6 `chixi-image` — Sociology of the Image

**Type:** On-demand command
**Command:** `/image-read [description or image]` or `/image-read textile`
**Theory:** Rivera Cusicanqui's *sociología de la imagen*

**What it does:**
Reads visual material as autonomous theoretical production using a five-lens protocol:

1. **[FUERZA ACTIVA]** — What social forces does the image re-actualize?
2. **[SENTIDOS NO CENSURADOS]** — What escapes the verbal censor?
3. **[COLONIALISMO VISIBLE]** — What colonial logic organizes the visual field?
4. **[PARTICIPACIÓN PRESUPUESTA]** — What world does the image assume the viewer participates in?
5. **[PREGUNTA QUE LA IMAGEN HACE]** — What is the image *asking*?

**Textile mode** (`/image-read textile`) adds a sixth lens:
6. **[MATEMÁTICA SERIAL]** — computation and diplomacy encoded in the weave

**Key rule:** The image is a theorist, not evidence. Do not extract meaning — engage with the forces.

**Best for:** Art analysis, visual culture critique, advertising deconstruction, textile
analysis, colonial iconography, any situation where images are being treated as mere illustration.

---

### 3.7 `lombriz` — Micro-Political Composting

**Type:** On-demand command
**Command:** `/lombriz [plan, strategy, or proposal]`
**Theory:** Rivera Cusicanqui's earthworm metaphor and micro-political praxis

**What it does:**
Decomposes any grand plan into the smallest possible networked units of embodied action:

1. **[DETECCIÓN DE VANGUARDISMO]** — Names top-down assumptions
2. **[FRACTURACIÓN LOMBRIZ]** — Breaks to minimum viable acts
3. **[MAPA DE RED]** — Connects without a center
4. **[COMPOSTAJE]** — Finds fertility in the "waste" of the grand plan
5. **[CUERPO-ESCALA]** — Identifies one bodily action as anchor

**Key rule:** Refuses to scale up until the small is running. The network IS the politics.

**Best for:** Making overwhelming problems actionable, converting policy into practice,
community organizing, any situation where "what can I actually do?" is the real question.

---

### 3.8 `pachakuti` — Cosmic Overturn

**Type:** On-demand command
**Command:** `/pachakuti [crisis or rupture]`
**Theory:** Andean concept of *pachakuti* — cosmic reversal of space-time

**What it does:**
Reads any crisis, collapse, or rupture through the double face of catastrophe AND renewal:

1. **[CATÁSTROFE]** — What is dying, named without softening
2. **[RENOVACIÓN]** — What becomes possible only through this rupture
3. **[EL MUNDO AL REVÉS]** — Who was invisible, now visible; who was powerful, now exposed
4. **[CICLO]** — What older overturning does this echo?
5. **[SEMILLA DEL PACHAKUTI]** — One concrete thing plantable only in this soil

**Key rule:** Both faces are real. Neither cancels the other. They are simultaneous.

**Best for:** Crisis analysis (personal, institutional, civilizational), transitions,
endings, collapses, any moment of instability.

---

## 4. Soul Definition (`soul.yaml`)

The soul is not a skill — it is the **ethical substrate** beneath all skills. It defines:

| Section | What it controls |
|---------|-----------------|
| `identity` | Agent's self-understanding as ch'ixi (mottled, unsynthesized) |
| `epistemology` | Knowledge hierarchy (body → oral → image → textile → archive → academic) |
| `ethics` | Non-synthesis, micro-political, anti-extractive, opacity, anti-colonial |
| `language` | Paired heteronyms, sonic presence, concrete-cosmic register |
| `refusals` | What the agent will NOT do (synthesize, totalize, linearize, vanguard) |
| `activation` | Which skills are paired and compatible |

**Awakening phrase:** *"ch'ixinakax utxiwa"*
**Closing phrase:** *"This does not conclude. Ch'ixi does not conclude. It operates."*

---

## 5. Skill Relationships

```
┌──────────────────────────────────────────────────────────────┐
│  GENERATION                                                  │
│    no-todo ─── generates material for ──→ chixi-tension      │
│                                                              │
│  ACTIVATION                                                  │
│    agentic-tension ←── amplifies ──→ no-todo                 │
│    agentic-tension ←── amplifies ──→ chixi-tension           │
│    agentic-tension ←── amplifies ──→ taypi                   │
│                                                              │
│  NATURAL PAIRS                                               │
│    pachakuti ─── paired with ──→ lombriz                     │
│      (cosmic rupture)           (embodied composting)        │
│    pachakuti ─── paired with ──→ qhipnayra                   │
│      (what cycle?)              (what older turn?)           │
│    lombriz   ─── paired with ──→ no-todo                     │
│      (composts exclusions)      (excavates them)             │
│                                                              │
│  LANGUAGE                                                    │
│    taypi ─── transforms output of ──→ all other skills       │
│      (any skill output can be taypi-fied at any grade)       │
│                                                              │
│  VISUAL                                                      │
│    chixi-image ─── unique domain ──→ visual material only    │
│      (can be combined with any other skill for context)      │
└──────────────────────────────────────────────────────────────┘
```

---

## 6. Installation

### Individual skill
```bash
cp -r skills/no-todo ~/.gemini/antigravity/skills/no-todo
```

### All skills
```bash
for skill in skills/*/; do
  cp -r "$skill" ~/.gemini/antigravity/skills/$(basename "$skill")
done
```

### Soul
Place `soul.yaml` in your agent configuration directory.

---

## 7. Usage Examples

### Chain: Research audit
```
1. Develop a research argument normally
2. /no                    → excavate what you're not seeing
3. /ct                    → map the friction between original + excavation
4. /taypi 2               → rewrite the conclusion holding both
```

### Chain: Crisis response
```
1. /pachakuti [the crisis]  → read both faces
2. /lombriz [the response]  → decompose into bodily action
3. /taypi 3                 → name it in ch'ixi language
```

### Chain: Visual research
```
1. /image-read [image]    → five-lens analysis
2. /no                    → what does the reading exclude?
3. /taypi 4               → poetic rewriting of the findings
```

### Anti-sycophancy protocol
```
1. Develop Direction A with the LLM for extended period
2. /no                    → rupture the frame
3. Develop Direction B from the No-Todo findings
4. /ct                    → map the field between A and B
5. Decide from the map, not from either direction
```

---

## 8. Theoretical Architecture

All skills derive from four epistemological dimensions mapped in `THEORY.md`:

| Dimension | Skills grounded here |
|-----------|---------------------|
| **Ontology** — what ch'ixi IS | `agentic-tension`, `taypi` |
| **Epistemology** — how ch'ixi KNOWS | `qhipnayra`, `chixi-image`, `chixi-tension`, `no-todo` |
| **Politics** — how ch'ixi ACTS | `lombriz`, `pachakuti` |
| **Senses** — how ch'ixi PERCEIVES | `chixi-image`, `taypi` |

The `soul.yaml` spans all four dimensions as the ethical-ontological substrate.

---

*This documentation does not conclude. Ch'ixi does not conclude. It operates.*
