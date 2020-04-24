import sys
import math


def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
compteur = 0
hasBoost = True
dist_opponent_x, dist_opponent_y, dist_opponent, dist_enn_checkpoint = 0, 0, 0, 0
thrust = 0

# game loop
while True:
    #counter for increasing sort of time
    compteur+=1
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    destination_x = next_checkpoint_x
    destination_y = next_checkpoint_y

    dist_enn_checkpoint = math.sqrt(((next_checkpoint_x - opponent_x)**2) + ((next_checkpoint_y - opponent_y)**2))
    
    dist_opponent_x = x - opponent_x
    dist_opponent_y = y - opponent_y
    dist_opponent = math.sqrt(dist_opponent_x**2+dist_opponent_y**2)
    
    #booster si le prochain ckeckpoint est loin, qu'on est aligné avec ce dernier
    if (next_checkpoint_dist >= 5000 and hasBoost == True and -1<=next_checkpoint_angle <=1 and compteur >=30): #and compteur >=30
        thrust = "BOOST"
        hasBoost = False
    elif(next_checkpoint_dist < 3500 and thrust > 10):   
        if (not -5 < next_checkpoint_angle < 5):
            thrust -=10                                            #(next_checkpoint_dist//25) 

    elif (next_checkpoint_dist > 4000):
        if(next_checkpoint_angle < -100 or next_checkpoint_angle > 100):
            thrust = 20
        
        elif (next_checkpoint_angle > 70 or next_checkpoint_angle < -70):
            thrust = 60
            
        elif (next_checkpoint_angle > 45 or next_checkpoint_angle < -45):
            thrust = 70
        
        elif (next_checkpoint_angle < 30 or next_checkpoint_angle > -30):
            thrust = 99
        
    else:
        if(next_checkpoint_angle < -100 or next_checkpoint_angle > 100):
            thrust = 20
        
        elif (next_checkpoint_angle > 70 or next_checkpoint_angle < -70):
            thrust = 50
            
        elif (next_checkpoint_angle > 45 or next_checkpoint_angle < -45):
            thrust = 80
        
        elif (next_checkpoint_angle < 30 or next_checkpoint_angle > -30):
            thrust = 99
            
    #if(next_checkpoint_dist<1000 and thrust > 20):
     #   thrust -=20

    if(dist_enn_checkpoint <=  next_checkpoint_dist and dist_opponent <= 1000 and next_checkpoint_dist <= 2000):   
        destination_x = opponent_x
        destination_y = opponent_y
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
    thrust = 0
    debug(hasBoost)
    debug(next_checkpoint_angle)
    #+ " " + str(hasBoost)+" "+str(next_checkpoint_angle))