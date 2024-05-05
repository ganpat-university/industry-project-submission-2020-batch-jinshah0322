def bwt(text):
  """Performs the Burrows-Wheeler Transform on the given text."""

  rotations = sorted([text[i:] + text[:i] for i in range(len(text))])
  print(rotations)
  bwt = "".join(row[-1] for row in rotations)
  return bwt

text = "banana$"  
bwt_text = bwt(text)
print("BWT:", bwt_text)