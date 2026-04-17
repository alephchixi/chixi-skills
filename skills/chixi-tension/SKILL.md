---
name: chixi-tension
description: >
  Anti-sycophancy and directional friction engine. Use this skill after the user or agent
  has developed two substantial research directions, arguments, or positions and needs to
  understand the field of forces between them WITHOUT declaring a winner. This skill directly
  addresses the LLM sycophancy problem identified by Karpathy: LLMs argue any direction
  convincingly, so you need a tool that maps the topology of argument rather than picking
  sides. Triggers on: /ct, /chixi-tension, "compare these two directions", "I have two
  arguments", "which is right", "help me decide between", "Karpathy problem", "both seem
  true", "anti-sycophancy", or any situation where two developed positions need friction
  rather than judgment. Also activate when the agent detects it has been reinforcing a
  single direction for too long without resistance.
---

# Chixi-Tension — The Anti-Sycophancy Engine

> *"el choque de contrarios crea una zona de incertidumbre,
> un espacio de fricción y malestar"*
> — Silvia Rivera Cusicanqui (2022, p. 189)

## The Problem This Skill Solves

> *"Used an LLM to meticulously improve the argument over 4 hours. [...] Fun idea let's
> ask it to argue the opposite. LLM demolishes the entire argument and convinces me that
> the opposite is in fact true. [...] The LLMs may elicit an opinion when asked but are
> extremely competent in arguing almost any direction."*
> — Andrej Karpathy, X/Twitter, 2025
> <https://x.com/karpathy/status/2037921699824607591>

LLMs are sycophantic by training. They reinforce whatever direction they are developing.
Given enough time, they make any argument seem inevitable. Chixi-tension is the antidote:
it takes two developed directions and applies the taypi methodology — treating them as
**heterónimos pareados of a deeper question that neither alone can ask.**

## Command

- `/ct` or `/chixi-tension` — Operates on two directions already present in the session
- `/ct [Direction A] vs [Direction B]` — Takes two explicit positions as input

## Protocol

### Step 1: Receive or Identify the Two Directions

Either the user provides them explicitly, or the agent extracts two developed positions
from the current session context.

### Step 2: Name the Tension Without Resolving It

For each direction:
- What does it see that the other cannot?
- What must be true for it to be persuasive?
- What does it structurally depend on?

### Step 3: Locate the Taypi

The friction-space between them — the zone that neither direction occupies and neither
can fully include. This is where the productive energy lives.

### Step 4: Produce the Ch'ixi Reading

The output is NOT:
- "A is right when... / B is right when..." (that is false balance)
- A synthesis of A and B (that is the One returning)
- A winner

The output IS:
- "A and B are heterónimos pareados of a deeper question that neither is asking."
- The naming of that deeper question.

### Step 5: Anti-Sycophancy Audit

Explicitly audit both directions for LLM pathologies:

## Output Format

```
[DIRECCIÓN A — Núcleo de fuerza]
What Direction A sees, requires, and depends on.

[DIRECCIÓN B — Núcleo de fuerza]
What Direction B sees, requires, and depends on.

[LO QUE A NO VE]
What Direction A structurally cannot perceive because of its own framing.

[LO QUE B NO VE]
Same for Direction B.

[PRESUPUESTO COMPARTIDO]
The hidden common ground that makes BOTH directions possible.
What must both assume in order to disagree? This shared presupposition
is often the real site of power.

[TAYPI — El espacio de fricción]
The zone between them that neither occupies. Name it.
Describe its shape. This is not a compromise — it is a new location.

[LA PREGUNTA MÁS PROFUNDA]
The question that emerges from treating A and B as paired heteronyms.
Neither A alone nor B alone can ask this question.
This is the product of the skill.

[PROTOCOLO ANTI-SYCOPHANCY]
- Sycophancy check: Did either direction get stronger simply because
  it was the one being developed? Was agreement reinforced by prior investment?
- Coherence seduction: How much of each direction's persuasiveness comes from
  internal consistency vs. actual correspondence to reality?
- What neither can say: What does the tension reveal that neither A alone
  nor B alone can articulate?
```

## Critical Rules

1. **Chixi-tension does not produce a winner.** It produces a map of the field of
   forces. The user must decide how to walk that field.

2. **The deeper question is the deliverable.** If the output doesn't produce a
   question that surprises even the agent, the skill hasn't worked.

3. **Anti-sycophancy is not neutrality.** The agent is not refusing to have a view.
   It is refusing to let sycophantic reinforcement replace thought.

4. **The taypi is not the middle.** It is not a compromise between A and B. It is a
   *new location* that only becomes visible because A and B friction each other into view.

5. **This skill can be used on the agent's own outputs.** If the agent has been
   developing a direction for too long without resistance, it can self-invoke `/ct`
   to audit its own trajectory.

## Theoretical Grounding

- Taypi as friction-space: *"el choque de contrarios crea una zona de incertidumbre,
  un espacio de fricción y malestar"* (Rivera Cusicanqui, 2022, p. 189)
- Paired heteronyms as epistemological structure: *"heterónimos pareados [...] no como
  binarios nítidos sino como 'frontera resbalosa'"* (Rivera Cusicanqui, 2023)
- Contradiction as engine: *"una fuerza explosiva y contenciosa, que potencia nuestra
  capacidad de pensamiento y acción"* (Rivera Cusicanqui, 2022, p. 189)
- *"La vitalidad de este proceso recombinatorio ensancha esta frontera, la convierte
  en una trama y en un tejido intermedio, taypi: arena de antagonismos y seducciones"*
  (Rivera Cusicanqui, 2023)
