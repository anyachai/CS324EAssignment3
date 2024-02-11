String[] uniqueWords;
PFont timesNewRoman;
int randInt, strLen = 0, row = 1, col = 10;
String word;

void setup() {
  // Required window size
  size(700,600);
  
  // List of words that appear only once in the academic text about birds
  uniqueWords = loadStrings("uniquewords.txt");
  
  // I chose Times New Roman since it is a common font in academic texts
  timesNewRoman = createFont("Times New Roman.ttf", 27);
  textFont(timesNewRoman);
}

void draw() {
  // The loop keeps going until it hits the break point in the middle
  while (true) {
    
    // Select a random word
    randInt = int(random(uniqueWords.length));
    word = uniqueWords[randInt] + ' ';
    
    // strLen keeps track of the length of a row of words
    strLen += word.length();
    
    // If length of the row is too long, we move to the next row,
    // starting at the left side of the window
    if (strLen > 40) {
      strLen = 0; 
      col = 10;
      row += 1;
    }
    
    // This break stops the infinite loop
    if (row > 21) {
      break;
    }
    
    // I chose red, green, and blue as my three colors since 
    // they are very special colors among birds. Most birds are
    // typically brown, gray, white, and black.
    if (word.length() < 8) {
      // Short words are blue, sort of like how 
      // blue has a small wavelength of light
      fill(#005493);
    } else if (word.length() > 10) {
      // Long words are red, sort of like how 
      // red has a long wavelength of light
      fill(#941100);
    } else {
      fill(#008f00);
    }
    
    // This prints out a new word
    text(word, col, 28*row);
    // The distance from the left border is updated
    col += word.length()*13;
  }
  noLoop();
}
