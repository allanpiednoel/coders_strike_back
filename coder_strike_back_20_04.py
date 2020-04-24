import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
checkpoint_list_x = []
checkpoint_list_y = []
laps = int(input())
vector_1 = []
x_both = []
y_both = []
hasBoost = True
HasShield= True
canBoost = True
vector_2 = []
checkpoint_count = int(input())
destination_x_1, destination_y_1, thrust_1, compteur = 8000, 4500, 100, 0
destination_x_2, destination_y_2, thrust_2= 8000, 4500, 100
speed_1, speed_2 = 0, 0
norm_vector_1, norm_vector_direction_1, angle_diretion_checkpoint_1 = 0, 0, 0
norm_vector_2, norm_vector_direction_2, angle_diretion_checkpoint_2 = 0, 0, 0
next_checkpoint_dist_1, next_checkpoint_dist_2 = 5000, 5000

for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoint_list_x.append(checkpoint_x)
    checkpoint_list_y.append(checkpoint_y)

def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
    
# game loop
while True:
    compteur += 1
    for i in range(2):
        # x: x position of your pod
        # y: y position of your pod
        # vx: x speed of your pod
        # vy: y speed of your pod
        # angle: angle of your pod
        # next_check_point_id: next check point id of your pod
        x, y, vx, vy, angle, next_check_point_id = [int(j) for j in input().split()]
        if(i == 0):
            vector_1.append(vx)
            vector_1.append(vy)

        if(i==1):
            vector_2.append(vx)
            vector_2.append(vy)
            
        x_both.append(x)
        y_both.append(y)
    for i in range(2):
        # x_2: x position of the opponent's pod
        # y_2: y position of the opponent's pod
        # vx_2: x speed of the opponent's pod
        # vy_2: y speed of the opponent's pod
        # angle_2: angle of the opponent's pod
        # next_check_point_id_2: next check point id of the opponent's pod
        x_2, y_2, vx_2, vy_2, angle_2, next_check_point_id_2 = [int(j) for j in input().split()]
        
    destination_x = checkpoint_list_x[next_check_point_id]
    destination_y = checkpoint_list_y[next_check_point_id]
        
    if(compteur > 2):    
        norm_vector_1 = math.hypot(vector_1[0],vector_1[1])
        
        norm_vector_direction_1 = math.hypot((checkpoint_list_x[next_check_point_id] - x), (checkpoint_list_y[next_check_point_id] - y))
        
        angle_diretion_checkpoint_1 = math.degrees(math.acos(((vector_1[0]*(x-checkpoint_list_x[next_check_point_id])) + (vector_1[1]*(y-checkpoint_list_y[next_check_point_id])))/(norm_vector_1*norm_vector_direction_1)))
            
        angle_diretion_checkpoint_1 = int(180-angle_diretion_checkpoint_1)
        
        norm_vector_2 = math.hypot(vector_2[0],vector_2[1])
        
        norm_vector_direction_2 = math.hypot((checkpoint_list_x[next_check_point_id] - x), (checkpoint_list_y[next_check_point_id] - y))
        
        angle_diretion_checkpoint_2 = math.degrees(math.acos(((vector_2[0]*(x-checkpoint_list_x[next_check_point_id])) + (vector_2[1]*(y-checkpoint_list_y[next_check_point_id])))/(norm_vector_2*norm_vector_direction_2)))
            
        angle_diretion_checkpoint_2 = int(180-angle_diretion_checkpoint_2)
        
        speed_1 = math.hypot(vector_1[0],vector_1[1])
        
        speed_2 = math.hypot(vector_2[0],vector_2[1])
        
        
    if(len(vector_1) >= 4):
        del vector_1[0]
        del vector_1[0]

    if(len(vector_2) >= 4):
        del vector_2[0]
        del vector_2[0]
    if(len(x_both)>=4):
        for m in range(2):
            del x_both[0]
            del y_both[0]
            
            
    if (next_checkpoint_dist_1 >= 4500 and angle_diretion_checkpoint_1 < 2 and hasBoost == True and compteur >=20):
        thrust_2 = "BOOST"
        hasBoost = False
        
    elif (next_checkpoint_dist_2 >= 4500 and angle_diretion_checkpoint_2 < 2 and hasBoost == True and compteur >=20):
        thrust_2 = "BOOST"
        hasBoost = False
        


        
    if (angle_diretion_checkpoint_1 > 2): 
       
        thrust_1 = 100
        destination_x_1 = checkpoint_list_x[next_check_point_id] + (-vector_1[0]*4)
        destination_y_1 = checkpoint_list_y[next_check_point_id] + (-vector_1[1]*4)
    
    if (angle_diretion_checkpoint_2 > 2): 
       
        thrust_2 = 100
        destination_x_2 = checkpoint_list_x[next_check_point_id] + (-vector_2[0]*4)
        destination_y_2 = checkpoint_list_y[next_check_point_id] + (-vector_2[1]*4)
        
        

    next_checkpoint_dist_1 = math.hypot((x_both[0]-checkpoint_list_x[next_check_point_id]),(y_both[0]-checkpoint_list_y[next_check_point_id]))
    next_checkpoint_dist_2 = math.hypot((x_both[1]-checkpoint_list_x[next_check_point_id]),(y_both[1]-checkpoint_list_y[next_check_point_id]))
    
    
    if(speed_1 > 250 and next_checkpoint_dist_1<2000):
        thrust_1 = 10
        
    
    if (next_checkpoint_dist_1<800 and next_check_point_id < checkpoint_count -1 ):
        destination_x_1 = checkpoint_list_x[next_check_point_id +1] + (-vector_1[0]*4)
        destination_y_1 = checkpoint_list_y[next_check_point_id +1] + (-vector_1[1]*4)
        
    if (next_checkpoint_dist_2<800 and next_check_point_id < checkpoint_count - 1):
        destination_x_2 = checkpoint_list_x[next_check_point_id +1] + (-vector_2[0]*4)
        destination_y_2 = checkpoint_list_y[next_check_point_id +1] + (-vector_2[1]*4)
    
    print(str(destination_x_1)+" "+ str(destination_y_1)+" "+str(thrust_1))
    print(str(destination_x_2)+" "+ str(destination_y_2)+" "+str(thrust_2))