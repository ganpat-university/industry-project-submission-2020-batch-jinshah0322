void main() {
  StringBuffer buffer = StringBuffer();
  for (int i = 0; i < 5; i++) {
    int asciiValue = 65;
    for (int j = 0; j < i + 1; j++) {
      buffer.write(String.fromCharCode(asciiValue));
      asciiValue++;
    }
    print(buffer);
    buffer.clear();
  }
}
