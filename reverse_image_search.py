def solve(image):
    matches = [{} for _ in range(len(image))]
    # [{2: 49, 3: 56},{ 1: 49, 3: 34 },{}]

    def search(image1, image2):
        return abs(image1 - image2)

    for i in range(image):
        for j in range(image[i]):
            if not matches[i][j]:
                match = search(image[i], image[j])
                matches[i][j] = match
                matches[j][i] = match
    return matches
