void main() {
  StringBuffer buffer = StringBuffer();
  int asciiValue = 65;
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < i + 1; j++) {
      buffer.write(String.fromCharCode(asciiValue));
    }
    print(buffer);
    buffer.clear();
    asciiValue++;
  }
}
