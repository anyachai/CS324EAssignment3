int y = 10;
int freq_count = 1;
void setup(){
  size(900, 800);
  String[] lines = loadStrings("wordFrequency.txt");
  for (String line : lines){
    String[] data = splitTokens(line, " :");
    int frequency = Integer.parseInt(data[0]);
    int count = Integer.parseInt(data[1]);
    if(freq_count == frequency){
      rect(10, y, count/2, 10);
      y += 10;
    }
    if (frequency > 800 && count >= 0){
      line(5, y+10, 15, y);
      rect(10, y, count/2, 10);
      y += 10;
    }
    freq_count += 1;
  }

}
