from collections import deque
from data_loader import cargar_set_datos
import os


def precompute_dp(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    # Base case: when there's only one element, the player will take it
    for i in range(n):
        dp[i][i] = arr[i]
    
    # Fill the dp table for all subarrays of size 2 or more
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1  # j is the end of the subarray
            # The player can choose the first or the last coin
            pick_first = arr[i] + (dp[i + 1][j] if i + 1 <= j else 0)
            pick_last = arr[j] + (dp[i][j - 1] if i <= j - 1 else 0)
            dp[i][j] = max(pick_first, pick_last)
    
    return dp

def juego_monedas_dinamico(arr):
    blue_score = 0  # Sophia's score
    red_score = 0   # Mateo's score
    choices = []

    dp = precompute_dp(arr)

    dq = deque(arr)
    i, j = 0, len(arr) - 1
    turn = 'Sophia'

    while dq:
        if turn == 'Sophia':
            # Sophia's turn, she chooses optimally based on DP
            if dp[i + 1][j] > dp[i][j - 1]:
                choices.append(f"Sophia debe agarrar la primera ({dq[0]})")
                blue_score += dq.popleft()
                i += 1
            else:
                choices.append(f"Sophia debe agarrar la ultima ({dq[-1]})")
                blue_score += dq.pop()
                j -= 1
            turn = 'Mateo'  # Switch turn to Mateo
        else:
            # Mateo's greedy turn: he takes the larger of the two available options
            if dq[0] > dq[-1]:
                choices.append(f"Mateo agarra la primera ({dq[0]})")
                red_score += dq.popleft()
                i += 1
            else:
                choices.append(f"Mateo agarra la ultima ({dq[-1]})")
                red_score += dq.pop()
                j -= 1
            turn = 'Sophia'  # Switch turn to Sophia

    return blue_score, red_score, choices


# Main function
def main():
    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../segunda-parte-set-datos/25.txt'))
    monedas = cargar_set_datos(dir)

    # Simulate the game
    ganancia_sophia, ganancia_mateo, choices = juego_monedas_dinamico(monedas)

    print("Recuento:")
    print(f"Ganancia Sophia: {ganancia_sophia}")
    print(f"Ganancia Mateo: {ganancia_mateo}")

    # Print the choices made during the game
    print("\nChoices made during the game:")
    print("; ".join(choices))

# Entry point for the program
if __name__ == "__main__":
    main()