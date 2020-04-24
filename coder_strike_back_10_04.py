import sys
import math


def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
compteur = 0
hasBoost = True
dist_opponent_x, dist_opponent_y, dist_opponent, dist_enn_checkpoint = 0, 0, 0, 0
thrust = 100

# game loop
while True:
    #counter for increasing a sort of time
    compteur+=1
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    next_checkpoint_angle_norm = math.sqrt(next_checkpoint_angle ** 2)
    
    #calculate opponent distance from our pod and from the next checkpoint
    destination_x = next_checkpoint_x
    destination_y = next_checkpoint_y
    dist_enn_checkpoint = math.sqrt(((next_checkpoint_x - opponent_x)**2) + ((next_checkpoint_y - opponent_y)**2))
    
    dist_opponent_x = x - opponent_x
    dist_opponent_y = y - opponent_y
    dist_opponent = math.sqrt(dist_opponent_x**2+dist_opponent_y**2)
    
    
 
    #use the booster if we can boost and if we are alignated with checkpoint
    if (next_checkpoint_dist >= 4500 and hasBoost == True and -1<=next_checkpoint_angle <=1 and compteur >=10): #and compteur >=30
        thrust = "BOOST"
        hasBoost = False

    #different power according to angle or distance between our pod and checkpoint
    
    elif (next_checkpoint_dist > 5000 and -110<next_checkpoint_angle<110 and hasBoost == False):
        thrust = 100
        
    elif (next_checkpoint_angle < 5 and thrust > 20 or -5 < next_checkpoint_angle and thrust > 20):
        thrust = int(100 - (next_checkpoint_angle_norm//1.8))
        
        #if (next_checkpoint_dist < 2500):
        #     thrust = int((100 - (next_checkpoint_angle_norm//1.8))//1.2)
    
        
            
   
     
     
    # kick opponent if we are close of it and next checkpoint with using boost or not 
    if(dist_enn_checkpoint <=  next_checkpoint_dist and dist_opponent <= 1000 and next_checkpoint_dist <= 2000):   
        destination_x = opponent_x
        destination_y = opponent_y
        thrust = 100
        if(dist_enn_checkpoint < next_checkpoint_dist and hasBoost == True):
            thrust = "BOOST"   
            hasBoost = False
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    #print("Debug messages: "+ str(dist_opponent_x)+" "+str(dist_opponent_x))

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
    print(str(destination_x) + " " + str(destination_y) + " " + str(thrust))
    thrust=100
    debug(hasBoost)
    debug(next_checkpoint_angle)
    debug(next_checkpoint_dist)
    #+ " " + str(hasBoost)+" "+str(next_checkpoint_angle))
    
    