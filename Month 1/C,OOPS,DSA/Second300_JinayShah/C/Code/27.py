def build_suffix_array(text):
    n = len(text)
    suffixes = []
    for i in range(n):
        suffix = text[i:]  
        suffixes.append((suffix, i))  
    
    suffixes.sort()  

    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

text = "banana"
suffix_array = build_suffix_array(text)

print("Suffix Array:", suffix_array)