import sys
import rewards
from rewards import get_new_skin

def main():
    counts = {'common': 0, 'rare': 0, 'epic': 0, 'legendary': 0}

    for _ in range(5):
        skin = get_new_skin()
        counts[skin] += 1

    for rarity, count in counts.items():
        print(f"{count}x {rarity}")

if __name__ == "__main__":
    main()
