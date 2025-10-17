# Character Language Specification

## 1. Goals

The Character Language (CL) describes tabletop RPG rulesets as structured, queryable models. The language must:

1. Represent rules as data tables, entities, and relationships.
2. Compute derived values from base data, including chained dependencies.
3. Attach modifiers to categories and entities in a composable way.
4. Feed character sheet templates that recompute values reactively when referenced data changes.
5. Support multiple RPG systems without hardcoding 5.2 SRD assumptions.

## 2. Core Concepts

- **Model**: A collection of named declarations that define tables, entities, modifiers, and computed expressions. Models can be composed via imports.
- **Table**: A keyed data structure, similar to a database table. Tables hold rows with typed columns and are used to encode level progressions, spell lists, equipment catalogs, etc.
- **Entity**: A typed record representing a rules element (class, ancestry, item, feature, etc.). Entities may reference tables and modifiers.
- **Selector**: A query expression that extracts values from tables or entities (e.g., `proficiency_bonus[level=2]`).
- **Modifier**: A declarative adjustment applied to one or more **targets** (categories, stats, or entities). Modifiers can be additive, multiplicative, or replace values.
- **Signal**: A reactive expression that caches its value but recomputes when dependencies change. Signals drive character sheet outputs.

## 3. Syntax Overview

CL uses a YAML-like serialization with explicit typing. Top-level documents are dictionaries keyed by declaration name. Each declaration contains a `type` field indicating its kind.

```yaml
proficiency_table:
  type: table
  key: level
  columns:
    level: integer
    proficiency_bonus: integer
  rows:
    - { level: 1, proficiency_bonus: 2 }
    - { level: 2, proficiency_bonus: 2 }
    - { level: 3, proficiency_bonus: 2 }
    - { level: 4, proficiency_bonus: 2 }
    - { level: 5, proficiency_bonus: 3 }
```

Other serializations (JSON, TOML) are allowed if they map 1:1 to this structure. Implementations may provide schema validation.

## 4. Data Types

- `integer`, `number`, `string`, `boolean`
- `enum` with permitted string values
- `ref` referencing another declaration by name
- `list<T>` and `map<K,V>` collections
- `expression` containing a reactive formula written in CL Expression Language (see §7)

## 5. Tables

Tables define structured datasets.

### 5.1 Fields
- `key`: Column name(s) uniquely identifying each row (string or list of strings).
- `columns`: Map of column names to data types.
- `rows`: Array of row dictionaries.
- `indexes` *(optional)*: Additional column indexes for faster lookup.

### 5.2 Access
Selectors read table data:

```yaml
level_two_prof:
  type: selector
  source: proficiency_table
  where:
    level: 2
  project: proficiency_bonus
```

Selectors return a scalar (when key uniquely matches) or a list. `where` accepts equality or comparison operators.

## 6. Entities

Entities model rule elements.

```yaml
ranger:
  type: entity
  entity_type: class
  attributes:
    hit_die: d10
    primary_abilities: [dexterity, wisdom]
    spellcasting: half_caster
  progressions:
    class_table: ref:ranger_table
  modifiers:
    - ref:ranger_weapon_proficiencies
```

Fields:
- `entity_type`: Namespaced string (e.g., `class`, `ancestry`, `item.weapon`).
- `attributes`: Key-value map of primitive or reference values.
- `progressions`: Named references to tables or selectors.
- `modifiers`: List of modifier references applied when the entity is active.
- `signals`: Optional computed expressions tied to the entity.

## 7. Expression Language

Expressions power selectors, modifiers, and signals. The syntax is functional with dotted access and operators.

### 7.1 Literals and Operators
- Supports numeric and string literals, `true`/`false`.
- Arithmetic: `+`, `-`, `*`, `/`, `%`.
- Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Logical: `and`, `or`, `not`.

### 7.2 References
- `@table.column` refers to the current row in a table iteration.
- `model.declaration` references any declaration by name.
- `character.ability_scores.strength` accesses the reactive character context.

### 7.3 Functions
Standard library functions include `sum(list)`, `max(a,b)`, `min`, `floor`, `ceil`, `lookup(table, criteria)`, and `if(condition, then, else)`.

### 7.4 Signals
Any expression can be promoted to a signal by wrapping it in a `signal` declaration:

```yaml
strength_modifier:
  type: signal
  inputs:
    - character.ability_scores.strength
  expression: "floor((inputs[0] - 10) / 2)"
```

`inputs` specify dependencies. When any input changes, the expression re-evaluates.

## 8. Modifiers

Modifiers encapsulate adjustments to character state.

```yaml
sword_bonus:
  type: modifier
  targets:
    - category: attack.melee
      operation: add
      value: 2
    - category: damage.slashing
      operation: add
      value: 2
  conditions:
    wielding: ref:sword_item
```

- `targets`: Array of objects describing where the modifier applies.
  - `category`: Namespaced string describing the stat bucket.
  - `path` *(optional)*: Specific attribute path within the character model.
  - `operation`: `add`, `multiply`, `set`, or custom operations defined by the system.
  - `value`: Literal or expression.
- `conditions`: Key-value map or expressions gating the modifier.
- `duration`: Optional scope (`permanent`, `temporary`, `encounter`, etc.).

Modifiers are composable; the engine aggregates all applicable modifiers for a target and resolves them in precedence order (e.g., `set` > `multiply` > `add`).

## 9. Templates

Templates connect models to output formats.

```yaml
simple_sheet:
  type: template
  format: markdown
  source: |
    # {{ character.name }}
    ## Abilities
    - Strength: {{ ability_scores.strength }} ({{ signals.str_mod }})
    ## Saves
    - Strength Save: {{ saves.strength.total }}
  bindings:
    ability_scores: character.ability_scores
    signals.str_mod: ref:strength_modifier
    saves.strength.total: signal:"character.saves.strength.total"
```

Template engines (Handlebars, Jinja, JSX, etc.) are pluggable. `bindings` map template variables to selectors or signals. When underlying data changes, bound expressions recompute and the rendered output updates like an Angular signal graph.

## 10. Character Instances

A character document selects entities and provides user choices:

```yaml
my_ranger:
  type: character
  model:
    imports: [ref:core_srd]
  choices:
    class: ref:ranger
    ancestry: ref:wood_elf
    background: ref:outlander
    ability_scores:
      strength: 14
      dexterity: 16
      constitution: 13
      intelligence: 10
      wisdom: 15
      charisma: 8
  equipment:
    - ref:longsword
  applied_modifiers:
    - ref:sword_bonus
  outputs:
    - template: ref:simple_sheet
```

The runtime constructs a dependency graph from the character's selections, resolves tables and modifiers, and updates all signals. Templates subscribed to those signals receive the latest values.

## 11. Extensibility

- **Imports** allow models to extend or override prior declarations.
- **Namespaces** prevent collisions across different games.
- **Custom operations** and **functions** can be registered per system.
- **Metadata** fields (e.g., licensing, versioning, source references) support SRD compliance.

## 12. Validation

Implementations should validate:
- Data type conformity in tables and entities.
- Selector correctness (references resolve, where clauses match columns).
- Modifier target/category existence.
- Signal dependency acyclicity.
- Template bindings referencing valid selectors/signals.

## 13. Cross-System Modeling

To support other RPGs:
- Use abstract categories (`attack.melee`, `resource.stamina`) rather than SRD-specific names.
- Define game-specific namespaces (e.g., `shadowdark.*`).
- Allow multiple progression tables per entity (e.g., class level tables vs. spell traditions).
- Use metadata to record source SRD/ORC license info.

By adhering to these principles, CL can encode the 5.2 SRD while remaining flexible enough to capture other rulesets and power dynamic, template-driven character sheets.
