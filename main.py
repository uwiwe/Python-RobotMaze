# Challenge here: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world.json&url=user_world%3Aproblem_world.json

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn_around():
  turn_left()
  turn_left()

while front_is_clear():
  move()

while not at_goal():
  if wall_on_right() and front_is_clear():
      move()
  elif right_is_clear():
      turn_right()
      move()
  elif wall_in_front():
      turn_left()