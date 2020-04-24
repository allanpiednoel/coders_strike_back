import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
compteur = 0
hasBoost = True
dist_opponent_x, dist_opponent_y, dist_opponent, dist_enn_checkpoint = 0, 0, 0, 0
thrust = 0
#getter_pos_x_opponent
# game loop
while True:
    
    compteur+=1
    
    #modulo permettant de récupérer les données ennemis avec 1 tour de différence
    
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint

    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    dist_enn_checkpoint = math.sqrt(((next_checkpoint_x - opponent_x)**2) + ((next_checkpoint_y - opponent_y)**2))
    
    dist_opponent_x = x - opponent_x
    dist_opponent_y = y - opponent_y
    dist_opponent = math.sqrt(dist_opponent_x**2+dist_opponent_y**2)
    
    #booster si le prochain ckeckpoint est loin, qu'on est aligné avec ce dernier
    if (next_checkpoint_dist >= 6000 and hasBoost == True and next_checkpoint_angle <= 5 and compteur >=30 or next_checkpoint_angle >= -5 and next_checkpoint_dist >= 6000 and hasBoost == True and compteur >=30):
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " BOOST")
        hasBoost = False
        
    if(next_checkpoint_angle < -120 or next_checkpoint_angle > 120):
        thrust = 10
        
    elif (next_checkpoint_angle > 60 or next_checkpoint_angle < -60):
        thrust = 40
        
    elif (next_checkpoint_angle > 30 or next_checkpoint_angle < -30):
        thrust = 70
    
    elif (next_checkpoint_angle < 15 or next_checkpoint_angle > -15):
        thrust = 100
        
    elif(next_checkpoint_dist<2000 and thrust > 20):
        thrust -=20
        
    #else:
    #    thrust = 50
        
    #elif (next_checkpoint_dist <= 1000):
        #thrust = 50

    if(next_checkpoint_dist >= 6000 and hasBoost == True):        
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_x) +" BOOST")        
        hasBoost = False
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    #print("Debug messages: "+ str(dist_opponent_x)+" "+str(dist_opponent_x))

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust)+" "+str(next_checkpoint_angle))
    #+ " " + str(hasBoost)+" "+str(next_checkpoint_angle))
    