# Text-Based Adventure Game
# Text Adventure Game - SKILLCITY Learning Project
# Author: samuel

A simple terminal-based adventure game where you explore rooms, interact with characters, collect items, and fight enemies.

## Features
- Explore interconnected rooms with descriptions
- Interact with friendly (Supporter) and enemy (Enemy) characters
- Collect key items to unlock new areas
- Simple combat system with item weaknesses
- Locked doors requiring specific items
- Underlined action hints in descriptions

## How to Play
1. Navigate between rooms using cardinal directions
2. `pet` the cat to get cheese for combat
3. `take` the key to unlock doors
4. `talk` to characters for clues
5. `fight` enemies using collected items

## Game Commands
| Command       | Action                                  |
|---------------|-----------------------------------------|
| north/south/east/west | Move between rooms             |
| talk          | Speak with characters                   |
| pet           | Interact with friendly characters       |
| take          | Collect items                           |
| fight         | Engage in combat                        |

## Classes Overview
### `Room`
- Contains name, description, linked rooms
- Holds characters and items
- Handles movement between rooms

### `Character`
- Base class for all characters
- Has name, description, and conversation
- Methods: `describe()`, `talk()`

### `Enemy` (inherits from Character)
- Has weakness attribute
- Combat system using `fight()` method

### `Supporter` (inherits from Character)
- Provides helpful items when interacted with
- Gives cheese through `pet` command

### `Item`
- Collectible objects with name/description
- Key item unlocks specific doors

## Game Flow
1. Start in kitchen with friendly cat
2. Find key to unlock south door
3. Navigate to dining hall to encounter zombie
4. Get cheese by petting cat
5. Use cheese to defeat zombie

## Example Gameplay
```text
You are in the kitchen. A dank and dirty room buzzing with flies
Whiskers is here! A fluffy white cat with green eyes...

> take
You take the key.

> south
You are in the dining_hall. A large room with ornate golden decorations
Dave is here! A smelly zombie...

> fight
What are you going to fight with?: cheese
You have defeated Dave with the cheese!