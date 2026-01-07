from typing import Dict
import random

def tool(func):
    return func

game_state = {
    "round": 0,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "game_over": False
}

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]


@tool
def validate_move(move: str, is_user: bool) -> bool:
    if move not in VALID_MOVES:
        return False

    if move == "bomb":
        if is_user and game_state["user_bomb_used"]:
            return False
        if not is_user and game_state["bot_bomb_used"]:
            return False

    return True


@tool
def resolve_round(user_move: str, bot_move: str) -> str:
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb" and bot_move == "bomb":
        return "draw"
    if user_move == "bomb":
        return "user"
    if bot_move == "bomb":
        return "bot"

    if (
        (user_move == "rock" and bot_move == "scissors") or
        (user_move == "paper" and bot_move == "rock") or
        (user_move == "scissors" and bot_move == "paper")
    ):
        return "user"

    return "bot"


@tool
def update_game_state(result: str, user_move: str, bot_move: str):
    game_state["round"] += 1

    if user_move == "bomb":
        game_state["user_bomb_used"] = True
    if bot_move == "bomb":
        game_state["bot_bomb_used"] = True

    if result == "user":
        game_state["user_score"] += 1
    elif result == "bot":
        game_state["bot_score"] += 1

    if game_state["round"] >= 3:
        game_state["game_over"] = True


def explain_rules():
    print(
        "Rules:\n"
        "• Best of 3 rounds\n"
        "• Moves: rock, paper, scissors, bomb\n"
        "• Bomb can be used once and beats all\n"
        "• Invalid input wastes the round\n"
    )


def bot_choose_move() -> str:
    if not game_state["bot_bomb_used"]:
        return random.choice(VALID_MOVES)
    return random.choice(["rock", "paper", "scissors"])


def play_game():
    explain_rules()

    while not game_state["game_over"]:
        print(f"\nRound {game_state['round'] + 1}")
        user_move = input("Enter your move: ").strip().lower()

        if not validate_move(user_move, is_user=True):
            print("Invalid move! Round wasted.")
            game_state["round"] += 1
            continue

        bot_move = bot_choose_move()

        result = resolve_round(user_move, bot_move)
        update_game_state(result, user_move, bot_move)

        print(f"You played: {user_move}")
        print(f"Bot played: {bot_move}")

        if result == "draw":
            print("Result: Draw")
        elif result == "user":
            print("Result: You win the round")
        else:
            print("Result: Bot wins the round")

    print("\n--- GAME OVER ---")
    print(f"Final Score -> You: {game_state['user_score']} | Bot: {game_state['bot_score']}")

    if game_state["user_score"] > game_state["bot_score"]:
        print("Final Result: USER WINS")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("Final Result: BOT WINS")
    else:
        print("Final Result: DRAW")


if __name__ == "__main__":
    play_game()
