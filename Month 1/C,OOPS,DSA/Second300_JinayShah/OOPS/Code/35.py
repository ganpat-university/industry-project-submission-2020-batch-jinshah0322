import re

def compile_and_match(pattern_str, text):
    compiled_pattern = re.compile(pattern_str)

    match = compiled_pattern.match(text)

    if match:
        print(f"Pattern '{pattern_str}' matched the text '{text}'.")
    else:
        print(f"Pattern '{pattern_str}' did not match the text '{text}'.")

pattern_str = r'^[a-zA-Z]+ \d+$'
text1 = 'John 123'
text2 = '123 John'

compile_and_match(pattern_str, text1)
compile_and_match(pattern_str, text2)
