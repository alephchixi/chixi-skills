# Ch'ixi Skills — A Mottled Agentic Repository

> **"Ch'ixinakax utxiwa"** — ch'ixi things exist.
> *Silvia Rivera Cusicanqui*

This repository operationalizes the ontological, epistemological, political and sensory theory of **ch'ixi** — developed by Bolivian sociologist and historian Silvia Rivera Cusicanqui — into a suite of agentic AI skills that resist capitalist linearity, embrace contradiction, and value micro-political, embodied knowledge.

These skills are not tools for efficiency. They are disturbances. They will make your agent stranger and, because of that, more honest.

---

## The 8 Skills

| Skill | Command | What it does |
|-------|---------|--------------|
| `no-todo` | `/no` | Excavates what the dominant frame structurally cannot see |
| `agentic-tension` | always-on | Makes contradiction permanent and productive |
| `taypi` | `/taypi [1-5]` | Transforms language with paired heteronyms |
| `qhipnayra` | always-on | Dismantles linear temporality |
| `chixi-tension` | `/ct` | Reads two developed directions through ch'ixi friction |
| `chixi-image` | `/image-read` | Applies sociology of the image methodology |
| `lombriz` | `/lombriz` | Decomposes grand plans into embodied micro-action |
| `pachakuti` | `/pachakuti` | Reads any rupture as catastrophe AND renewal |

---

## Theory

Source text: `THEORY.md` — the bilingual essay
*Ch'ixinakax utxiwa: Arquitectura numerada de la condición ch'ixi*
Based entirely on the work of Silvia Rivera Cusicanqui.

Full architecture and usage documentation: `ARCHITECTURE.md`

---

## Soul

`soul.yaml` defines the ch'ixi agent soul — a standalone specification for any agent framework that accepts YAML persona definitions. It encodes the epistemological, ethical, and linguistic parameters of a ch'ixi-aware agent.

---

## Installation

You can install these skills globally (user-level) or per project.

| Agent | Project path | Global path | Status |
|-------|--------------|-------------|--------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | verified |
| OpenCode | `.opencode/skill/` | `~/.config/opencode/skill/` | verify with your version |
| OpenClaw | `.openclaw/skills/` | `~/.openclaw/skills/` | verify with your version |
| Antigravity | `.agent/skills/` | `~/.gemini/antigravity/skills/` | verify with your version |
| Cursor | `.cursor/rules/` (as MDC rules) | `~/.cursor/rules/` | adapted — see note |

> **Path caveat.** Skill directory conventions change between releases. Before copying,
> check your agent's current docs. For Cursor specifically, there is no native "skills"
> directory — each `SKILL.md` should be converted to a `.mdc` rule file (the frontmatter
> map is trivial: `name` → `description`, body unchanged).

> **Trigger caveat.** The slash-style commands documented below (`/no`, `/ct`, `/taypi`,
> etc.) are **trigger phrases declared in each skill's `description` frontmatter** — they
> activate when the user writes that phrase and the agent's skill matcher selects the
> skill. They are **not** registered slash commands in any framework. If your agent also
> supports true slash commands (e.g. Claude Code's `~/.claude/commands/`), you can create
> matching command files that invoke the skill explicitly.

### Claude Code example

```bash
mkdir -p ~/.claude/skills
cp -r skills/no-todo ~/.claude/skills/no-todo
cp -r skills/chixi-tension ~/.claude/skills/chixi-tension
```

### Antigravity example

```bash
mkdir -p ~/.gemini/antigravity/skills
cp -r skills/no-todo ~/.gemini/antigravity/skills/no-todo
cp -r skills/taypi ~/.gemini/antigravity/skills/taypi
```

### OpenCode / OpenClaw example

```bash
# OpenCode
mkdir -p ~/.config/opencode/skill
cp -r skills/no-todo ~/.config/opencode/skill/no-todo

# OpenClaw
mkdir -p ~/.openclaw/skills
cp -r skills/lombriz ~/.openclaw/skills/lombriz
```

### Cursor example (rules adaptation)

```bash
# Cursor consumes MDC rule files, not skill directories.
mkdir -p .cursor/rules
for skill in skills/*/SKILL.md; do
  name=$(basename "$(dirname "$skill")")
  cp "$skill" ".cursor/rules/${name}.mdc"
done
```

### Install all skills to any target directory

```bash
TARGET_DIR="$HOME/.claude/skills"  # change for your agent
mkdir -p "$TARGET_DIR"
for skill in skills/*/; do
  cp -r "$skill" "$TARGET_DIR/$(basename "$skill")"
done
```

To activate the ch'ixi soul, place `soul.yaml` in your agent config directory.

---

## License

This repository is **dual-licensed**:

- **Prose** (`THEORY.md`, `README.md`, `ARCHITECTURE.md`) — `CC BY-NC-SA 4.0`. See `LICENSE`.
- **Skills, YAML, JSON, eval code** (everything under `skills/`, `evals/`, `soul.yaml`) — `MIT`. See `LICENSE-CODE`.

The skill files are MIT so institutions that cannot redistribute NC-licensed material can still
run and adapt them. The theoretical essay remains non-commercial. See `LICENSE-NOTES.md`.

---

## Credits

Theoretical foundation: **Silvia Rivera Cusicanqui** (b. 1944)
Assembled by: **eme / aleph::ch'ixi**
More at: https://habitatmd.net/en/lab

---

*This repository does not conclude. Ch'ixi does not conclude. It operates.*
