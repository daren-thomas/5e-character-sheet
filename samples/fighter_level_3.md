---
title: "Level 3 Fighter Sample"
template: markdown
bind:
  ability_scores: character.ability_scores
  saves: character.saves
  senses: character.senses
  attacks: character.actions.attacks
  actions: character.actions
  equipment: character.inventory
  features: character.features
  resources: character.resources
  proficiencies: character.proficiencies
  spellcasting: character.spellcasting
  notes: character.notes
---

# {{ character.name }}

**Heritage** {{ character.origin.ancestry.name }} | **Background** {{ character.origin.background.name }} | **Class** {{ character.classes.primary.name }} {{ character.classes.primary.level }} ({{ character.subclasses.primary.name }})

## Snapshot
- **Proficiency Bonus:** {{ signals.proficiency_bonus }}
- **Initiative:** {{ signals.initiative.total }}
- **Armor Class:** {{ character.defenses.armor_class.total }}
- **Speed:** {{ character.movement.speed.total }} ft.
- **Hit Points:** {{ character.hit_points.current }} / {{ character.hit_points.maximum }} (Hit Dice: {{ character.hit_dice.pool }})
- **Passive Perception:** {{ senses.passive_perception }}

## Ability Scores
| Ability | Score | Modifier | Save | Save Proficient |
|---------|-------|----------|------|-----------------|
| Strength | {{ ability_scores.strength.total }} | {{ ability_scores.strength.modifier }} | {{ saves.strength.total }} | {{ saves.strength.proficient }} |
| Dexterity | {{ ability_scores.dexterity.total }} | {{ ability_scores.dexterity.modifier }} | {{ saves.dexterity.total }} | {{ saves.dexterity.proficient }} |
| Constitution | {{ ability_scores.constitution.total }} | {{ ability_scores.constitution.modifier }} | {{ saves.constitution.total }} | {{ saves.constitution.proficient }} |
| Intelligence | {{ ability_scores.intelligence.total }} | {{ ability_scores.intelligence.modifier }} | {{ saves.intelligence.total }} | {{ saves.intelligence.proficient }} |
| Wisdom | {{ ability_scores.wisdom.total }} | {{ ability_scores.wisdom.modifier }} | {{ saves.wisdom.total }} | {{ saves.wisdom.proficient }} |
| Charisma | {{ ability_scores.charisma.total }} | {{ ability_scores.charisma.modifier }} | {{ saves.charisma.total }} | {{ saves.charisma.proficient }} |

## Combat Actions
### Attacks
{{#attacks.primary}}
- **{{ name }}** — Attack Bonus {{ attack_bonus.total }}, Damage {{ damage.formula }} {{ damage.type }}
{{/attacks.primary}}
{{^attacks.primary}}
_No primary attacks configured._
{{/attacks.primary}}

### Bonus Actions
{{#actions.bonus_actions}}
- {{ name }} — {{ summary }}
{{/actions.bonus_actions}}
{{^actions.bonus_actions}}
_No bonus actions available._
{{/actions.bonus_actions}}

### Reactions
{{#actions.reactions}}
- {{ name }} — {{ summary }}
{{/actions.reactions}}
{{^actions.reactions}}
_No reactions available._
{{/actions.reactions}}

## Class Features (Fighter 3)
{{#features.class}}
- **{{ name }} ({{ source.level }})** — {{ summary }}
{{/features.class}}
{{^features.class}}
_No class features detected._
{{/features.class}}

### Maneuvers (Battle Master)
{{#resources.superiority_dice}}
- Superiority Dice: {{ current }}d{{ die_size }} (max {{ maximum }})
{{/resources.superiority_dice}}
{{#resources.maneuvers.list}}
  - {{ name }} — {{ summary }}
{{/resources.maneuvers.list}}
{{^resources.maneuvers.list}}
_No maneuvers selected._
{{/resources.maneuvers.list}}

## Equipment
{{#equipment.carried}}
- {{ item.name }} ×{{ quantity }} ({{ weight.total }} lb.) — Equipped: {{ equipped }}
{{/equipment.carried}}
{{^equipment.carried}}
_No equipment listed._
{{/equipment.carried}}

## Proficiencies
### Armor
{{#proficiencies.armor}}
- {{.}}
{{/proficiencies.armor}}
{{^proficiencies.armor}}
- None
{{/proficiencies.armor}}

### Weapons
{{#proficiencies.weapons}}
- {{.}}
{{/proficiencies.weapons}}
{{^proficiencies.weapons}}
- None
{{/proficiencies.weapons}}

### Tools
{{#proficiencies.tools}}
- {{.}}
{{/proficiencies.tools}}
{{^proficiencies.tools}}
- None
{{/proficiencies.tools}}

### Saving Throws
{{#proficiencies.saving_throws}}
- {{.}}
{{/proficiencies.saving_throws}}
{{^proficiencies.saving_throws}}
- None
{{/proficiencies.saving_throws}}

### Skills
{{#proficiencies.skills}}
- {{ name }} ({{ total }})
{{/proficiencies.skills}}
{{^proficiencies.skills}}
- None
{{/proficiencies.skills}}

## Notes
{{#notes.journal}}
- {{.}}
{{/notes.journal}}
{{^notes.journal}}
_No personal notes._
{{/notes.journal}}

## Spellcasting Summary
{{#spellcasting.classes}}
### {{ class_name }} Spellcasting
- Spell Save DC: {{ spell_save_dc }}
- Spell Attack Bonus: {{ spell_attack_bonus }}
- Spell Slots:
{{#slots}}
  - Level {{ level }}: {{ count }}
{{/slots}}
{{^slots}}
  - None
{{/slots}}
- Prepared Spells:
{{#prepared_spells}}
  - {{ name }}
{{/prepared_spells}}
{{^prepared_spells}}
  - None
{{/prepared_spells}}
{{/spellcasting.classes}}
{{^spellcasting.classes}}
_No spellcasting available._
{{/spellcasting.classes}}
