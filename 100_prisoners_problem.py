def prisoner_problem():
    import random

    prisoners = list(range(1, 101))
    picked_prisoners = set()

    for i in range(1, 100):
        random.shuffle(prisoners)
        if i in prisoners[0:50]:
            picked_prisoners.add(i)
    return picked_prisoners
print(len(prisoner_problem()))
