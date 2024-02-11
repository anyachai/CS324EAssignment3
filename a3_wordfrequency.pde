int x = 70;
int hue = 93;
int sat = 92;
int bri = 30;
int bri_stroke = 30;
int freq_count = 1;
int bottomMargin = 50;

void setup() {
  size(745, 900);
  background(255);
  colorMode(HSB, 360, 100, 100);
  String[] lines = loadStrings("wordFrequency.txt");
  
  fill(0);
  
  // Drawing x & y axis labels
  textSize(14);
  text("0", 50, 870);
  text("4018", 700, 870);
  text("1589", 35, 40);
  text("Frequencies", width / 2 - 20, height - 20);
  text("Count", 15, height / 2);
  
  // Iterates through each line and assigns variables frequency and count
  for (String line : lines) {
    String[] data = splitTokens(line, " :");
    int frequency = Integer.parseInt(data[0]);
    int count = Integer.parseInt(data[1]) / 2;
    int y = height - count;
    
    // Draws bar with word count
    if (freq_count == frequency) {
      fill(constrain(hue, 0, 360), sat, constrain(bri, 0, 100));
      stroke(constrain(hue, 0, 360), sat, bri_stroke);
      rect(x, y - bottomMargin, 10, count);
      x += 10;
    }
    
    // Draws "axis breaks" to fit all data on screen
    if (frequency > 800 && count >= 0) {
      line(x, y - bottomMargin + 5, x + 10, y - bottomMargin - 5);
      x += 10;
      rect(x, y - bottomMargin, 10, count);
      x += 10; 
    }
    
    // Update changed variables
    freq_count += 1;
    hue -= 5;
    bri += 8;
  }
}
