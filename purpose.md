# Purpose

This repository aims to describe tabletop role-playing game rulesets in a machine-readable, reactive format that can power automated character sheet generation.

Our immediate target is the 5.2 System Reference Document (SRD) for the world's most popular fantasy RPG. We want a language that can capture the SRD's classes, ancestry options, equipment, spells, and derived mechanics (e.g., proficiency bonus tables, class features, ability score modifiers). By modeling these rules as structured data and relationships, we can evaluate character builds programmatically, surface validation errors, and drive templated sheet outputs.

The same language should also be flexible enough to model other games (e.g., Shadowdark) without modification. That means supporting:

- Declarative rule tables (class progressions, spell lists, equipment catalogs, etc.).
- Derived values that reference other data ("proficiency bonus at level 2", "hit points = hit die + Constitution modifier").
- Contextual modifiers that apply to categories ("a sword grants +2 melee attack and +2 slashing damage").
- Character sheet templates (Markdown, HTML, JSON, etc.) that reference model data and computed values, updating reactively when inputs change—similar to signal-based systems.

Ultimately, the purpose is to:

1. Encode SRD mechanics in a reusable, versioned model.
2. Offer a language for defining and querying those mechanics.
3. Support template-based rendering of character sheets that stays synchronized with the underlying rules.
4. Generalize to other RPG rulesets without embedding system-specific assumptions into the language.

The remainder of this repository will introduce the **Character Language** specification that realizes this purpose and demonstrate how SRD data is represented within it.
