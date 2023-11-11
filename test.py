class Field:
    def __init__(self, hid=False, size):
        self.size = size
        self.hid = hid
        self.field = [[" "] * 6 for _ in range(6)]

    def add_ship (self, )
        print()
        print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
        print("  --------------------------- ")
        for i, row in enumerate(field):
            row_str = f"  {i + 1} | {' | '.join(row)} | "
            print(row_str)
            print("  --------------------------- ")
