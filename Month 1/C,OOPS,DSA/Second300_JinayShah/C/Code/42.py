def edit_distance(string1, string2):
   len1 = len(string1)
   len2 = len(string2)

   if len1 == 0 and len2 == 0:
       return 0

   if len1 == 0 or len2 == 0:
       return abs(len1 - len2)

   if string1[-1] == string2[-1]:
       return edit_distance(string1[:-1], string2[:-1])

   else:
       return 1 + min(edit_distance(string1, string2[:-1]),
                     edit_distance(string1[:-1], string2),
                     edit_distance(string1[:-1], string2[:-1]))
print("Edit Distance is", edit_distance("kitten", "sitting"))