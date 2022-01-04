def findRotateSteps(ring, key):
    # dist = min(abs(i-j), n-abs(i-j))

    def bfs(start):
        queue = [start, 0]
        for x in queue:
            char, steps = x
            if key == "":
                return steps
            if char == 1:
