with open("data.txt", "r") as file:
    l1, l2 = zip(*(map(int, x.split()) for x in file))
    l1, l2 = sorted(l1), sorted(l2)
    total_distance = sum(abs(x-y) for x,y in zip(l1,l2))
    similarity_score = sum(x * l2.count(x) for x in l1)
    print(f"result part1: {total_distance}")
    print(f"result part2: {similarity_score}")
