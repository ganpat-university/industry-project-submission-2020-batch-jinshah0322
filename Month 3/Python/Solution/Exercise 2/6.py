set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference (Set 1 - Set 2):", set1.difference(set2))
print("Difference (Set 2 - Set 1):", set2.difference(set1))

print("Symmetric Difference:", set1.symmetric_difference(set2))

print("Is Set 1 subset of Set 2:", set1.issubset(set2))
print("Is Set 2 subset of Set 1:", set2.issubset(set1))
print("Is Set 1 superset of Set 2:", set1.issuperset(set2))
print("Is Set 2 superset of Set 1:", set2.issuperset(set1))