# Ch’ixi Skills

Eight ways of reading and making with contradiction, developed by **eme / aleph::ch’ixi** in conversation with Silvia Rivera Cusicanqui. Rivera credits the Aymara sculptor Víctor Zapana for teaching her the word ch’ixi (*Canibalizar la modernidad*, 2022, pp. 190–191). The project’s essay also works alongside Glissant, Dussel, Quijano and Zalamea.

| Skill | Choose it for | Text alias |
|---|---|---|
| [no-todo](skills/no-todo/SKILL.md) | One thesis and what its premise leaves out | `/no` |
| [agentic-tension](skills/agentic-tension/SKILL.md) | A live decision with a disagreement worth carrying | By name |
| [taypi](skills/taypi/SKILL.md) | A rewrite using paired terms, degree 1–5 | `/taypi` |
| [qhipnayra](skills/qhipnayra/SKILL.md) | A trace through past practice, present evidence and an open future | By name |
| [chixi-tension](skills/chixi-tension/SKILL.md) | Two developed directions and the evidence for both | `/ct` |
| [chixi-image](skills/chixi-image/SKILL.md) | A situated reading of an image, textile or description | `/image-read` |
| [lombriz](skills/lombriz/SKILL.md) | An accountable gesture people can carry out together | `/lombriz` |
| [pachakuti](skills/pachakuti/SKILL.md) | A reading of a rupture and who can shape what follows | `/pachakuti` |

[Read the bilingual essay](THEORY.md), [the design and worked examples](ARCHITECTURE.md), or [the evaluation guide](evals/README.md). The [soul profile](soul.yaml) is a project-specific YAML. Load it through a mechanism supported by the host or read it as agreed session guidance.

## Installation

The table gives paths documented by each host. Use the installed version’s documentation for alternate editions and older releases. See the [evaluation guide](evals/README.md) for how to check installed behavior.

| Host | Project or workspace directory | User directory | Invocation |
|---|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/` | `~/.claude/skills/` | Skill name, e.g. `/no-todo` |
| [OpenCode](https://opencode.ai/docs/skills/) | `.opencode/skills/` | `~/.config/opencode/skills/` | Ask the agent to load the skill by name |
| [OpenClaw](https://docs.openclaw.ai/help/faq/skills-and-automation) | `<workspace>/skills/` | `~/.openclaw/skills/` | Installed command if exposed by the client, or ask by name |
| [Cursor](https://cursor.com/docs/skills) | `.cursor/skills/` or `.agents/skills/` | `~/.cursor/skills/` | Pick the skill by name or ask the agent to use it |
| [Google Antigravity App](https://antigravity.google/docs/skills) | `.agents/skills/` | `~/.gemini/config/skills/` | Ask by name and check discovery. Confirm CLI or IDE variants separately |

From your project directory, give the install helper the appropriate target. Each whole folder travels with its resources. Running the same command twice leaves one folder per skill at the same path. An existing local edit or an unrecognized file marks a conflict before the helper copies anything.

```sh
python3 /path/to/chixi-skills/install_skills.py .claude/skills
python3 /path/to/chixi-skills/install_skills.py .opencode/skills taypi
```

The textual aliases in the skill table express intent. Explicit slash-command availability depends on the host. `agentic-tension` and `qhipnayra` can be invoked for one task or chosen for an ongoing session. Ask to end the mode when you want regular behavior again.

## License

This repository is **dual-licensed**:

- **Prose** (`THEORY.md`, `README.md`, `ARCHITECTURE.md`) — `CC BY-NC-SA 4.0`. See `LICENSE`.
- **Skills, YAML, JSON, eval code** (everything under `skills/`, `evals/`, `soul.yaml` and `install_skills.py`) — `MIT`. See `LICENSE-CODE`.

The skill files are MIT so institutions that cannot redistribute NC-licensed material can still
run and adapt them. The theoretical essay remains non-commercial. See `LICENSE-NOTES.md`.

---

## Credits

Silvia Rivera Cusicanqui is the principal theoretical source. eme / [aleph::ch’ixi](https://alephchixi.org/) makes the transpositions into agent practice. The essay identifies the sources of its other concepts.
