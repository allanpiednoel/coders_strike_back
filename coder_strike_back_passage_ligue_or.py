import sys
import math
import numpy as np 

def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

compteur = 0
counter_shield = 4

#bool's for permission to use capacities
hasShield= True
hasBoost = True
canBoost = True

accurate_angle,prodscal_me_opponent, angle_diretion_checkpoint, norm_vector_direction = 0, 0, 0, 0
dist_opponent_x, dist_opponent_y, dist_opponent, dist_enn_checkpoint,norm_vector_opponent,norm_vector_me = 0, 0, 0, 0, 0, 0

speed =0 #est en unité/tours

coord_me = []
vector_me = []
approaching_checkpoint_list = []
checkpoint_list_x = []
checkpoint_list_y = []
checkpoint_number_x,checkpoint_number_y, numero_checkpoint = 0, 0, -1
coord_opponent = []
vector_opponent = []
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
    


    #saving informations
    
    coord_me.append(x)
    coord_me.append(y)
    
    coord_opponent.append(opponent_x)
    coord_opponent.append(opponent_y)
    
    
    
    #have 4 parts in lists
    if(len(coord_me) == 6):
        del coord_me[0]
        del coord_me[0]
        
    #if(len(checkpoint_list_x) < 7):
    #    del checkpoint_list_x[6]
        
    if(len(coord_opponent) == 6):
        del coord_opponent[0]
        del coord_opponent[0]

    #calculations begins after 5 rounds for erase "division by 0" error or index out of range

    if (compteur > 5):
        
        
        if (checkpoint_number_x != 6):
            checkpoint_list_x.append(next_checkpoint_x)
        if (checkpoint_number_y != 6):
            checkpoint_list_y.append(next_checkpoint_y)
        
            #deleting useless coordination
            
        
        if(compteur >=7 and checkpoint_number_x !=6 and checkpoint_list_x[checkpoint_number_x] == checkpoint_list_x[checkpoint_number_x +1]):
            del checkpoint_list_x[checkpoint_number_x + 1]
        elif(checkpoint_number_x !=6 and compteur >=7):
            checkpoint_number_x += 1
        
        if(compteur >=7 and checkpoint_number_x !=6 and checkpoint_list_y[checkpoint_number_y] == checkpoint_list_y[checkpoint_number_y +1]):
            del checkpoint_list_y[checkpoint_number_y + 1]
        elif(checkpoint_number_y !=6 and compteur >=7):
            checkpoint_number_y += 1
            
            
        #try to recognize checkpoint (first one is chekpoint nb 1)
            
        if (checkpoint_number_y >=3 and checkpoint_number_x >= 3):
            if (next_checkpoint_x == checkpoint_list_x[0]):
                numero_checkpoint = 0
                
        #increasing visibility of operations
        xB_me = coord_me[2]
        xA_me = coord_me[0]
        yB_me = coord_me[3]
        yA_me = coord_me[1]
        
        xB_opponent = coord_opponent[2]
        xA_opponent = coord_opponent[0]
        yB_opponent = coord_opponent[3] 
        yA_opponent = coord_opponent[1]
    



        #create a list which is vector parameters (Delta_x, Delta_y)
        vector_me.append((xB_me-xA_me))
        vector_me.append((yB_me-yA_me)) 
        
        vector_opponent.append((xB_opponent-xA_opponent))
        vector_opponent.append((yB_opponent-yA_opponent))  
        
        approaching_checkpoint_list.append(int(math.hypot((x-next_checkpoint_x),(y-next_checkpoint_y)))) 
        if(compteur > 7):
            speed = approaching_checkpoint_list[1]-approaching_checkpoint_list[2]
            speed = math.sqrt((speed)**2)
            
            
        #erase unusable data's


        if(len(vector_me) == 4):
            del vector_me[0]
            del vector_me[0]
        if(len(vector_opponent) == 4):
            del vector_opponent[0]
            del vector_opponent[0]
        if(len(approaching_checkpoint_list)==3):
            del approaching_checkpoint_list[0]

        
        #beginning of vectorial calculations
            
        prodscal_me_opponent = (vector_me[0]*vector_opponent[0]) + (vector_me[1]*vector_opponent[1])
        
        norm_vector_opponent = math.hypot(vector_opponent[0],vector_opponent[1])
        
        norm_vector_me = math.hypot(vector_me[0],vector_me[1])
        
        norm_vector_direction = math.hypot((next_checkpoint_x - x), (next_checkpoint_y - y))
        
        accurate_angle = math.degrees(math.acos(prodscal_me_opponent/(norm_vector_me*norm_vector_opponent)))
        
        angle_diretion_checkpoint = math.degrees(math.acos(((vector_me[0]*(x-next_checkpoint_x)) + (vector_me[1]*(y-next_checkpoint_y)))/(norm_vector_me*norm_vector_direction)))
            
        angle_diretion_checkpoint = 180-angle_diretion_checkpoint
        
        angle_diretion_checkpoint = math.sqrt((angle_diretion_checkpoint)**2)
    
    destination_x = next_checkpoint_x
    destination_y = next_checkpoint_y

    #calculate opponent distance from our pod and from the next checkpoint
    
    
    dist_enn_checkpoint = math.sqrt(((next_checkpoint_x - opponent_x)**2) + ((next_checkpoint_y - opponent_y)**2))
    
    dist_opponent_x = x - opponent_x
    dist_opponent_y = y - opponent_y
    dist_opponent = math.hypot(dist_opponent_x,dist_opponent_y)


    #use the booster if we can boost and if we are alignated with checkpoint

    if (next_checkpoint_dist >= 4500 and hasBoost == True and -1<=next_checkpoint_angle <=1 and canBoost == True and compteur >=20):
        thrust = "BOOST"
        hasBoost = False



    #different power according to angle or distance between our pod and checkpoint
    
    elif (next_checkpoint_dist > 5000 and -110<next_checkpoint_angle<110 and hasBoost == False):
        thrust = 100
        


    #optimization of trajectory
            
    elif (angle_diretion_checkpoint > 3): 
        thrust = 100
        destination_x = next_checkpoint_x + (-vector_me[0]*4)
        destination_y = next_checkpoint_y + (-vector_me[1]*4)
        
    #reduce speed approaching checkpoint
    
    if(speed > 250 and next_checkpoint_dist<2000):
        thrust = 10
        
        
    #anticipation of turn
    
    if (numero_checkpoint >=0):
        if(next_checkpoint_x == checkpoint_list_x[checkpoint_list_x.index(next_checkpoint_x)] and next_checkpoint_dist < 800):
            destination_x = checkpoint_list_x[checkpoint_list_x.index(next_checkpoint_x)+1]
            destination_y = checkpoint_list_y[checkpoint_list_y.index(next_checkpoint_y)+1]
        
        
            
    # kick opponent if we are close of it and next checkpoint with using boost, shield, or just power 

    if(accurate_angle >30 and dist_enn_checkpoint <= next_checkpoint_dist and dist_opponent <= 1800 and next_checkpoint_dist <= 2000 and compteur > 15):
        destination_x = opponent_x
        destination_y = opponent_y
        thrust = 100
            
        if(dist_enn_checkpoint < next_checkpoint_dist and hasBoost == True and canBoost == True):
            thrust = "BOOST" 
            hasBoost = False
            
    if(accurate_angle >20 and hasShield == True and dist_opponent <= 900 and compteur > 15):
        thrust = "SHIELD" 
        hasShield = False
        canBoost = False
        
    if (canBoost == False):
        counter_shield -=1
        
        if (counter_shield == 0):
            counter_shield = 0
            canBoost = True
            
    
            
    
    
    print(str(destination_x) + " " + str(destination_y) + " " + str(thrust))
    thrust=100
