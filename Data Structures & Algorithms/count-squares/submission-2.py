class CountSquares:

    def __init__(self):
        self.cods = {}

    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.cods:
            self.cods[tuple(point)] = 0
        self.cods[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.cods:
            if x == px and y == py:
                continue
            print(x, y, px, py, abs(x - px) == abs(y - py))
            if abs(x - px) == abs(y - py):
                print((x, py) in self.cods)
                if (x, py) in self.cods and (px, y) in self.cods:
                    countpoint = 1 if (px, py) not in self.cods else self.cods[(px, py)]
                    res+= self.cods[(x, py)]*self.cods[(px, y)]*self.cods[(x, y)]*(countpoint)
                    print(self.cods[(x, py)], self.cods[(px, y)])
        return res
