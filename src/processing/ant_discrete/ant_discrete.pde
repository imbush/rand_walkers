FloatList ants = new FloatList(); //list of coordinates of ants in form [x1, y1, x2, y2,...]
FloatList moves = new FloatList(0,0,
                                1,0,
                                0,1,
                                -1,0,
                                0,-1);
int n = 10;
int step = 10;
int alpha = 255;

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
    circle(ants.get(i), ants.get(i+1), 10);
    int a = floor(random(moves.size()/2)); //Picks random move index
    ants.add(i, step * moves.get(2 * a));
    ants.add(i+1, step * moves.get(2 * a+1));
  }
}
