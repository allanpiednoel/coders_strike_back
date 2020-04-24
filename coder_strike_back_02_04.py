import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
compteur = 0
duree =0
hasBoost = True
pouet_X_opponent, pouet_Y_opponent, dist_opponent_x, dist_opponent_y, dist_opponent, New_X_opponent, New_Y_opponent, dist_enn_checkpoint = 0, 0, 0, 0, 0, 0, 0, 0
thrust = 100
#getter_pos_x_opponent
# game loop
while True:
    
    compteur+=1
    
    ModuloCounter = compteur % 2
    #modulo permettant de récupérer les données ennemis avec 1 tour de différence
    
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint

    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    
    if(ModuloCounter == 1):
        New_X_opponent = opponent_x
        New_Y_opponent = opponent_y
    elif (ModuloCounter == 0):

        pouet_X_opponent = opponent_x - New_X_opponent
         
        pouet_Y_opponent = opponent_y - New_Y_opponent

    dist_enn_checkpoint = math.sqrt(((next_checkpoint_x - opponent_x)**2) + ((next_checkpoint_y - opponent_y)**2))
    
    dist_opponent_x = x - opponent_x
    dist_opponent_y = y - opponent_y
    dist_opponent = math.sqrt(dist_opponent_x**2+dist_opponent_y**2)
    
    #booster si le prochain ckeckpoint est loin, qu'on est aligné avec ce dernier
    if (next_checkpoint_dist >= 5000 and hasBoost == True and next_checkpoint_angle <= 10 and next_checkpoint_angle >= -10 and compteur >=30):
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " BOOST" + " " + str(hasBoost)+" "+str(next_checkpoint_angle))
        duree+=1
        if (duree ==3):
            hasBoost = False
        
    if(next_checkpoint_angle < -10 or next_checkpoint_angle > 10):
        thrust = int(100 - ( math.sqrt (next_checkpoint_angle**2)*(5/9)))
        
    elif(next_checkpoint_dist<1800):
        thrust = int(100-(math.sqrt(next_checkpoint_dist)))
        
    else:
        thrust = 100
        
    #elif (next_checkpoint_dist <= 1000):
        #thrust = 50

    if(dist_opponent <= 800 and compteur >= 10 and next_checkpoint_dist >= dist_enn_checkpoint):
        print(str(opponent_x) + " " + str(opponent_y) +" 100")
        if (hasBoost == True):
            print(str(opponent_x) + " " + str(opponent_y) + " BOOST")
            duree+=1
            if (duree ==3):
                hasBoost = False
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    #print("Debug messages: "+ str(dist_opponent_x)+" "+str(dist_opponent_x))

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust) + " " + str(hasBoost)+" "+str(next_checkpoint_angle))