def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        tower.append(' ' * (n_floors - i - 1) + '*' * (2 * i + 1) + ' ' * (n_floors - i - 1))
    return tower

print(tower_builder(3)) 
print(tower_builder(6))

def tower_builder2(n_floors):
    return [(' ' * (n_floors - i - 1) + '*' * (2 * i + 1) + ' ' * (n_floors - i - 1)) for i in range(n_floors)]

print(tower_builder2(3))
print(tower_builder2(6))