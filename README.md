# Rock–Paper–Scissors–Plus Game Referee Bot

## Overview
This project implements a **minimal conversational game referee** for the Rock–Paper–Scissors–Plus game.  
The system runs as a CLI-based chatbot that enforces game rules, tracks state across turns, and provides clear, round-by-round feedback to the user.

The implementation focuses on **logical correctness, state management, and agent-style design**, rather than UI polish or external AI services.

---

## Game Rules
- Best of **3 rounds**
- Valid moves:
  - rock
  - paper
  - scissors
  - bomb (can be used **once per player**)
- Bomb beats all other moves
- Bomb vs Bomb → Draw
- Invalid input wastes the round
- Game ends automatically after 3 rounds

---

## State Model
The game state is stored in an explicit in-memory structure that persists across turns:

- `round`: current round number
- `user_score`: number of rounds won by the user
- `bot_score`: number of rounds won by the bot
- `user_bomb_used`: tracks whether the user has used bomb
- `bot_bomb_used`: tracks whether the bot has used bomb
- `game_over`: signals when the game ends

This ensures the system does **not rely on prompts for memory** and behaves deterministically.

---

## Agent & Tool Design
The solution follows an **agent-style architecture inspired by Google ADK concepts**, while remaining fully deterministic and rule-based.

### Tools
Each core responsibility is implemented as a separate tool-like function:
- `validate_move`  
  Validates user and bot moves and enforces bomb usage constraints.
- `resolve_round`  
  Determines the winner of a round using defined game rules.
- `update_game_state`  
  Updates round count, scores, and bomb usage while maintaining persistent state.

### Separation of Concerns
- **Intent Understanding:** Interpreting user input as a valid game move
- **Game Logic:** Rule enforcement, validation, and outcome resolution
- **Response Generation:** Clear, conversational feedback for each round

This separation improves clarity, maintainability, and ease of extension.

---

## Sample Output
