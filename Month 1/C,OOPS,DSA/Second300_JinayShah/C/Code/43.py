def overlap(str1, str2):
  for i in range(min(len(str1), len(str2)), 0, -1):
    if str1[-i:] == str2[:i]:
      return str1[-i:]
  return ""

def shortest_superstring(strings):
  superstring = strings[0]
  while len(strings) > 1:
    best_overlap = ""
    best_pair = None
    for i in range(len(strings)):
      for j in range(len(strings)):
        if i != j:
          overlap_str = overlap(strings[i], strings[j])
          if len(overlap_str) > len(best_overlap):
            best_overlap = overlap_str
            best_pair = (i, j)
    if best_pair is not None:
      s1, s2 = best_pair
      if len(strings[s1]) > len(strings[s2]):
        superstring += strings[s2][len(best_overlap):]
        del strings[s2]
      else:
        superstring += strings[s1][len(best_overlap):]
        del strings[s1]
    else:
      superstring += strings[1]
      del strings[1]
  return superstring

strings = ["ABCD", "BCDE", "CDEFG", "FGHA"]
superstring = shortest_superstring(strings)
print(superstring) 