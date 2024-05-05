void main() {
  for (int i=0;i<5;i++){
    var star='';
    for (int j = 9-2*i;j>1;j--){
      star+=' ';
    }
    for (int j=0;j<(i*2+1);j++){
      star+='* ';
    }
    print(star);
  }
}
