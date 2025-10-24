import random
import sys

PEG_COUNT = 4
COLORS = {
    "1": ("Rouge", (200, 30, 30)),
    "2": ("Vert", (30, 180, 30)),
    "3": ("Bleu", (40, 80, 200)),
    "4": ("Jaune", (230, 220, 60)),
    "5": ("Rose", (200, 40, 160)),
    "6": ("Blanc", (40, 200, 200)),
}
MAX_ATTEMPTS = 10


def generate_secret():
    return [random.choice(list(COLORS.keys())) for _ in range(PEG_COUNT)]


def evaluate_guess(secret, guess):
    exact = 0
    secret_remaining = []
    guess_remaining = []
    for s, g in zip(secret, guess):
        if s == g:
            exact += 1
        else:
            secret_remaining.append(s)
            guess_remaining.append(g)
    misplaced = 0
    secret_counts = {}
    for s in secret_remaining:
        secret_counts[s] = secret_counts.get(s, 0) + 1
    for g in guess_remaining:
        if secret_counts.get(g, 0) > 0:
            misplaced += 1
            secret_counts[g] -= 1
    return exact, misplaced


def parse_guess_input(s):
    s = s.strip()
    if " " in s:
        parts = s.split()
    elif "," in s:
        parts = [p.strip() for p in s.split(",")]
    else:
        parts = list(s)
    parts = [p for p in parts if p != ""]
    return parts


def terminal_game():
    secret = generate_secret()
    print("\nBienvenue dans le jeu Mastermind (Version Terminal) !\n")
    print("Règles : Devinez la combinaison secrète de 4 chiffres entre 1 et 6.")
    print("Vous avez 10 tentatives pour deviner la combinaison.")
    print("Indices : '*' = bien placé, '-' = mal placé.")
    print(f"Couleurs possibles (tapez les chiffres, ex: 1234 ou 1 2 3 4) :")
    for k, (name, _) in COLORS.items():
        print(f"  {k} = {name}")
    print(f"Devinez la combinaison secrète des {PEG_COUNT} chiffres générés aléatoirement. Vous avez {MAX_ATTEMPTS} tentatives.")
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        attempt += 1
        while True:
            raw = input(f"Tentative {attempt}/{MAX_ATTEMPTS} > ").strip()
            guess = parse_guess_input(raw)
            if len(guess) != PEG_COUNT:
                print(f"Entrée invalide : il faut {PEG_COUNT} valeurs.")
                continue
            if not all(g in COLORS for g in guess):
                print("Entrée invalide : valeurs valides = " + ", ".join(COLORS.keys()))
                continue
            break
        exact, misplaced = evaluate_guess(secret, guess)
        indicators = "*" * exact + "-" * misplaced
        print(f"Indices: {indicators}  (exact={exact}, misplaced={misplaced})")
        if exact == PEG_COUNT:
            print(f"Bravo ! Vous avez trouvé la combinaison en {attempt} tentatives.")
            return
    print("Dommage, vous avez épuisé vos tentatives.")
    print("La combinaison était :", " ".join(secret))
    print("Correspondance couleurs :",
          ", ".join(f"{k}={v[0]}" for k, v in COLORS.items()))

def main():
    print("\nMastermind - Choisissez la version:")
    print("  1) Terminal")
    print("  2) Interface graphique (Pygame)")
    choice = input("Votre choix (1/2) > ").strip()
    if choice == "2":
            print("\nLa Version sur Pygame est en cours de développement.\n")
            terminal_game()
    else:
        terminal_game()

if __name__ == "__main__":
    main()