import sys
import math
import numpy as np 

def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
compteur = 0
hasShield= True
hasBoost = True
dist_opponent_x, dist_opponent_y, dist_opponent, dist_enn_checkpoint, angle_from_opponent = 0, 0, 0, 0, 0
#last_position_x_me, last_position_y_me, last_position_x_opponent, last_position_y_opponent = x, y, opponent_x, opponent_y
coord_me = []
vector_me = []

coord_opponent = []
vector_opponent = []
thrust = 100

accurate_angle = 0

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
    
    coord_me.append(x)
    coord_me.append(y)
    
    coord_opponent.append(x)
    coord_opponent.append(y)
    
    #me = np.array([coord_me[0], coord_me[1],coord_me[2],coord_me[3], dtype=int])
    
    
    
    if(len(coord_me) == 6):
        del coord_me[0]
        del coord_me[0]
        
    if(len(coord_opponent) == 6):
        del coord_opponent[0]
        del coord_opponent[0]
        
        
    if (compteur > 4):
        xB_me = coord_me[2]
        xA_me = coord_me[0]
        yB_me = coord_me[3]
        yA_me = coord_me[1]
        
        xB_opponent = coord_opponent[2]
        xA_opponent = coord_opponent[0]
        yB_opponent = coord_opponent[3] #_opponent
        yA_opponent = coord_opponent[1]
    
        vector_me.append((xB_me-xA_me))
        vector_me.append((yB_me-yA_me))  
        
        vector_opponent.append((xB_opponent-xA_opponent))
        vector_opponent.append((yB_opponent-yA_opponent))  
        
        if(len(vector_me) == 4):
            del vector_me[0]
            del vector_me[0]
        if(len(vector_opponent) == 4):
            del vector_opponent[0]
            del vector_opponent[0]
    #angle=arccos( math.pr (AB),AC) / (norm(AB)*norm(BC)) )
    
    next_checkpoint_angle_norm = math.sqrt(next_checkpoint_angle ** 2)
    
    #calculate opponent distance from our pod and from the next checkpoint
    destination_x = next_checkpoint_x
    destination_y = next_checkpoint_y
    dist_enn_checkpoint = math.sqrt(((next_checkpoint_x - opponent_x)**2) + ((next_checkpoint_y - opponent_y)**2))
    
    dist_opponent_x = x - opponent_x
    dist_opponent_y = y - opponent_y
    dist_opponent = math.sqrt(dist_opponent_x**2+dist_opponent_y**2)
    
    #use the booster if we can boost and if we are alignated with checkpoint
    if (next_checkpoint_dist >= 4500 and hasBoost == True and -1<=next_checkpoint_angle <=1 and compteur >=20): #and compteur >=30
        thrust = "BOOST"
        hasBoost = False

    #different power according to angle or distance between our pod and checkpoint
    
    elif (next_checkpoint_dist > 5000 and -110<next_checkpoint_angle<110 and hasBoost == False):
        thrust = 100
        
    elif (next_checkpoint_angle < 5 and thrust > 20 or -5 < next_checkpoint_angle and thrust > 20):
        thrust = int(100 - (next_checkpoint_angle_norm//1.8))
        

    # kick opponent if we are close of it and next checkpoint with using boost, shield, or just power 
    if(dist_enn_checkpoint <=  next_checkpoint_dist and dist_opponent <= 1800 and next_checkpoint_dist <= 2000):
        destination_x = opponent_x
        destination_y = opponent_y
        thrust = 100
        
        #mise en place de la visée, essayer de calculer l'angle entre le pod et l'adversaire
        # il faut empecher l'activation des capacités si mon pod est parallèle à l'adversaire
        if(dist_enn_checkpoint < next_checkpoint_dist and hasBoost == True):
            thrust = "BOOST" 
            
            hasBoost = False
            
    if(hasShield == True and dist_opponent <= 850):
        thrust = "SHIELD" 
        hasShield = False
        
    
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    #print("Debug messages: "+ str(dist_opponent_x)+" "+str(dist_opponent_x))

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
    print(str(destination_x) + " " + str(destination_y) + " " + str(thrust))
    thrust=100
