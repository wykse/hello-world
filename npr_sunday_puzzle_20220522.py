"""
NPR Sunday Puzzle
2022-05-22

Take the name of an island. Move its first letter two spaces later in
the alphabet (so A would become C, B would become D, etc.). Reverse
the result and you'll have the name of another island. What islands
are these?

https://www.npr.org/2022/05/22/1100539535/sunday-puzzle-just-a-d-away

"""


def island_puzzle(island: str) -> str:
    """Returns island with first letter shifted two spaces later in the
    alphabet, then reversed.
    """

    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_shift = abc[2:] + abc[0:2]

    abc_key = {k: v for k, v in list(zip(abc, abc_shift))}

    island_shift = [
        abc_key[letter] if count == 0 else letter
        for count, letter in enumerate(island.lower())
    ]
    island_str = "".join(island_shift)

    result = island_str[::-1]

    return result


def main() -> tuple:
    islands = ["Guam", "Maui"]

    islands = [island.lower() for island in islands]

    answer = []
    for island in islands:
        result = island_puzzle(island)
        if result in islands:
            answer.append((island, result))
            print((island, result))


if __name__ == "__main__":
    main()
