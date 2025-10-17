# Dungeons & Dragons 5E SRD Domain Model

## Scope and Context
- **System Reference Document (SRD)** content centers on running tabletop role-playing sessions that mix social interaction, exploration, and combat.
- The domain focuses on the data and rules needed to describe player characters, the world they explore, and the mechanics that resolve actions.
- Primary stakeholders are **Players** (control characters) and the **Game Master (GM)** (presents scenes, adjudicates rules, controls nonplayer characters and monsters).

## Core Aggregates
### Character
- Represents an adventurer with identity, narrative background, and mechanical statistics recorded on a character sheet.
- Key attributes: name, level, class, subclass, background, species, alignment, experience points, size, speed, initiative, armor class, hit points, conditions, and wealth.
- Holds six **Ability Scores** (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) and derived **Ability Modifiers**.
- Tracks **Proficiency Bonus** (level-based), **Saving Throws**, **Skills**, **Tool Proficiencies**, **Languages**, **Feats**, **Features**, **Equipment**, **Spells**, and **Spell Slots**.
- Lifecycle (from character creation rules): choose class → determine origin (background, species, languages) → determine ability scores → choose alignment → fill in derived details (attack bonuses, spell save DC, passive scores, etc.).
- Relationships:
  - Linked to exactly one **Class** at level 1 and a class-specific **Subclass** once unlocked.
  - Gains a **Background** and **Species** defining story hooks and mechanical traits.
  - Owns zero or more **Feats**, **Equipment Items**, and known/prepared **Spells**.
  - Interacts with **Conditions**, **Actions**, **Rest states**, and **Encounters** during play.

### Ability Score
- Value from 1–20 for characters (monsters can exceed 20).
- Each score maps to an ability modifier (−5 to +10) used in d20 Tests, damage, spell save DCs, and derived statistics.
- Ability score improvements arise from Backgrounds, Species traits, Class features, and Feats.

### Proficiency and Skills
- **Proficiency Bonus** scales with character level and applies to trained skills, tools, weapons, and saving throws.
- **Skills** are named specializations tied to abilities (e.g., Athletics, Stealth) and come from classes, backgrounds, or feats.
- **Tool Proficiencies** represent familiarity with equipment sets (artisan’s tools, vehicles, gaming sets, etc.).

### Class
- Defines combat role, hit dice, class features per level, proficiencies, spellcasting progression, and subclass access.
- Provides starting equipment packages and determines armor/weapons/tools training.
- Each class exposes a **Class Table** describing feature progression, spell slot advancement (if applicable), and subclass unlock level.
- Includes **Subclass** options (e.g., Berserker Barbarian, Life Domain Cleric) that extend class abilities.

### Background
- Bundles narrative backstory with mechanical benefits: ability score increases, a fixed **Origin Feat**, two skill proficiencies, one tool proficiency, and equipment (or 50 gp alternative).
- Suggests roleplaying hooks (bonds, ideals) and forms part of a character’s origin profile.

### Species
- Determines creature type (humanoid in SRD), size, base speed, life span guidance, and species-specific traits (darkvision, resistances, innate abilities).
- May offer choice-driven traits (e.g., damage ancestry, spell-like features).

### Feat
- Represents discrete special abilities, often with prerequisites (ability scores, level, class membership, species, or other features).
- Origin feats come from backgrounds; other feats are selected during advancement.
- Grant modifiers, proficiencies, spells, actions, or conditional bonuses.

### Equipment
- Catalog of physical items grouped into armor, weapons, adventuring gear, tools, mounts/vehicles, and treasure (coins, gems).
- Items have properties: cost, weight, category, traits (e.g., armor type, weapon properties like finesse, heavy).
- Armor defines Armor Class calculations and minimum Strength/training requirements; shields modify AC.
- Weapons specify damage dice, damage types, handedness, ammunition, and special qualities.
- Tools support skill checks, downtime activities, or class features.

### Magic Items
- Special equipment providing magical effects, charges, or spell access; often require attunement and can replicate spells or grant bonuses.

### Spellcasting
- **Spells** defined by name, school of magic, level, casting time, range, components (verbal, somatic, material), duration, and effect text.
- Spell lists tagged by class; characters prepare or know spells based on class rules.
- **Spell Slots** represent expendable magical resources; higher-level slots intensify effects. Ritual casting and always-prepared spells create exceptions to slot usage.
- Many spells scale with slot level, apply conditions, or deal damage typed to the schools of magic.

### Combat & Action Economy
- Core loop uses **d20 Tests** (ability checks, attack rolls, saving throws) resolved against DC or AC.
- **Actions** include Attack, Cast a Spell, Dash, Disengage, Dodge, Help, Hide, Search, Use an Object, and class- or spell-specific actions.
- **Bonus Actions** and **Reactions** provide additional timing windows; limitations include one leveled spell per turn with slots.
- Turn structure occurs within **Combat Encounters** organized into rounds, initiative order, and movement rules.
- **Conditions** (blinded, charmed, prone, etc.) alter capabilities; tracked on character sheets and monster stat blocks.
- **Rest Mechanics** (Short Rest, Long Rest) manage resource recovery, including hit points, class features, and spell slots.

### Monsters and NPCs
- **Monsters** use stat blocks with ability scores, proficiency bonus, saving throws, skills, senses, damage types, and action options (attacks, spells, recharge abilities).
- Categorized in lists (standard and alphabetical) with challenge ratings, size, creature type, alignment tendencies, and XP rewards.
- Provide adversaries, allies, or environmental hazards controlled by the GM.

### Encounter Toolbox
- The SRD toolbox supplies guidance on building encounters, hazards, traps, environmental effects, and alternative gameplay procedures (initiative variants, chase rules).
- Includes tables for random events, travel pace, downtime, and exploration challenges that interact with character abilities and resources.

## Supporting Concepts
- **Rules Glossary** defines key terms (attack roll, condition, damage type, spell save DC) ensuring consistent interpretation across rules modules.
- **Legal and Licensing** context clarifies SRD usage but does not affect in-game mechanics.
- **Animals** provide mundane creature stat blocks for mounts, companions, and familiars.

## Relationships Summary
- Characters aggregate data from Class, Background, Species, Equipment, Spells, and Feats to form a complete sheet.
- Classes dictate advancement, available spells, and combat roles; subclasses refine specialization.
- Backgrounds and Species supply origin story, ability adjustments, and proficiencies, which interact with skill and tool mechanics.
- Equipment and Magic Items modify statistics, grant abilities, or provide resources; many require proficiency for optimal use.
- Spells and Spell Slots integrate with class features, actions, and conditions to create tactical choices.
- Monsters and Encounter rules provide opposition that triggers d20 Tests, resource expenditure, and narrative outcomes.
