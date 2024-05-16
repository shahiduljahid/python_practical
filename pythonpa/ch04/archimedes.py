import math
def archimedes(numSides):
    halfAngleA = 180.0 / numSides
    archi_pi = numSides * math.sin(math.radians(halfAngleA))
    return archi_pi
if __name__ == "__main__":
    for sides in range(8, 100, 8):
        print("{0:>4}  {1}".format(sides, archimedes(sides)))
