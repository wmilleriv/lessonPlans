// "when started" hat block
int whenStarted1() {
  Drivetrain.driveFor(forward, 1500.0, mm, true);
  Drivetrain.turnFor(right, 90.0, degrees, true);
  Drivetrain.driveFor(forward, 750.0, mm, true);
  Drivetrain.turnFor(right, 90.0, degrees, true);
  Drivetrain.driveFor(forward, 1500.0, mm, true);
  Drivetrain.turnFor(right, 90.0, degrees, true);
  Drivetrain.driveFor(forward, 1500.0, mm, true);
  Drivetrain.turnFor(right, 90.0, degrees, true);
  Drivetrain.driveFor(forward, 1500.0, mm, true);
  return 0;
}


int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();

  whenStarted1();
}