FloatList ants = new FloatList(); //list of coordinates of ants in form [x1, y1, x2, y2,...]
FloatList moves = new FloatList(0,0,
                                1,0,
                                0,1,
                                -1,0,
                                0,-1);
int n = 100000;
int step = 5;
int alpha = 5;

void setup() {
  size(500, 500);
  for (int i = 0; i < n; i++) {
    ants.append(250);
    ants.append(250);
  }
  fill(255, 255, 255, alpha);
  noStroke();
  mouseClicked();
}

void draw() {
}

void mouseClicked() {
  background(0);
  for (int i = 0; i < ants.size(); i += 2){
    circle(ants.get(i), ants.get(i+1), 1);
    float a = random(TWO_PI); //Picks random move index
    ants.add(i, step * cos(a));
    ants.add(i+1, step * sin(a));
  }
}
