# Ch'ixi Skills — A Stained Agentic Repository

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

| Agent | Project path | Global path |
|-------|--------------|-------------|
| Antigravity | `.agent/skills/` | `~/.gemini/antigravity/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenCode | `.agents/skills/` | `~/.opencode/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |

### Antigravity example

```bash
mkdir -p ~/.gemini/antigravity/skills
cp -r skills/no-todo ~/.gemini/antigravity/skills/no-todo
cp -r skills/taypi ~/.gemini/antigravity/skills/taypi
# ... etc.
```

### Claude Code example

```bash
mkdir -p .claude/skills
cp -r skills/no-todo .claude/skills/no-todo
cp -r skills/chixi-tension .claude/skills/chixi-tension
```

### OpenCode example

```bash
mkdir -p ~/.opencode/skills
cp -r skills/no-todo ~/.opencode/skills/no-todo
cp -r skills/lombriz ~/.opencode/skills/lombriz
```

### Cursor example

```bash
mkdir -p .cursor/skills
cp -r skills/no-todo .cursor/skills/no-todo
cp -r skills/chixi-image .cursor/skills/chixi-image
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

This repository is licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International** (`CC BY-NC-SA 4.0`).

- You can use, study, fork, remix, and share this work for research, education, and other non-commercial contexts.
- You must provide attribution and keep derivatives under the same license.
- Commercial use is not permitted without a separate written agreement.

See `LICENSE` and `LICENSE-NOTES.md`.

---

## Credits

Theoretical foundation: **Silvia Rivera Cusicanqui** (1944-present)
Assembled by: **eme / aleph::ch'ixi**
More at: https://habitatmd.net/en/lab

---

*This repository does not conclude. Ch'ixi does not conclude. It operates.*
