import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
compteur = 0
debug = 0

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    thrust = 100
    compteur+=1
    dist_opponent_x= x - opponent_x
    dist_opponent_y= y - opponent_y
    dist_opponent = math.sqrt(dist_opponent_x*dist_opponent_x+dist_opponent_y*dist_opponent_y)
    
    if (next_checkpoint_dist >= 2000 and debug != 10 and next_checkpoint_angle == 0 and thrust == 0 and compteur >=50):
        thrust = "BOOST"
        debug += 1
        
    if(next_checkpoint_angle > 90 or next_checkpoint_angle < -90 or next_checkpoint_dist < 600):
        thrust = 0
        
    #elif (next_checkpoint_dist <= 1000):
        #thrust = 50

    if(dist_opponent_x <= 1000 and debug <=1 and compteur >= 50 and next_checkpoint_dist >=3000):
         print(str(opponent_x) + " " + str(opponent_y) + " BOOST")
         debug += 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
   

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust) + " " + str(dist_opponent))