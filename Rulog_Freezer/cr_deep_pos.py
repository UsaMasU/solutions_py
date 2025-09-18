
import time

crane = "CR2"

with open(f"{crane}_IniPosMuliIzq1.ini") as f_z_left, open(f"{crane}_IniPosMuliDer1.ini") as f_z_right:
    content_z_left = list(filter(None, f_z_left.read().split('\n')))
    content_z_right = list(filter(None, f_z_right.read().split('\n')))
    
    with open(f"{crane}_side_1_z.txt", "w") as f_side_1, open(f"{crane}_side_2_z.txt", "w") as f_side_2 :
        
        for i_left in content_z_left:
        
            eq_symb_left = i_left.find('/')
            pos_z_left = i_left[:eq_symb_left]
            pos_z_left = ''.join(pos_z_left.split())

            if len(pos_z_left) > 1:
                pos_z_left = pos_z_left.split('=')  
                
                z_left_log = pos_z_left[0]
                z_left = pos_z_left[1]
                
                print(f"Deep[{z_left_log}].Z := {z_left};", file=f_side_1)
                print(f"Deep[{z_left_log}].Z := {z_left};")
           
            time.sleep(0.01)
        
        for i_right in content_z_right:
        
            eq_symb_right = i_right.find('/')
            pos_z_right = i_right[:eq_symb_right]
            pos_z_right = ''.join(pos_z_right.split())

            if len(pos_z_right) > 1:
                pos_z_right = pos_z_right.split('=')  
                
                z_right_log = pos_z_right[0]
                z_right = pos_z_right[1]
                
                print(f"Deep[{z_right_log}].Z := {z_right};", file=f_side_2)
                print(f"Deep[{z_right_log}].Z := {z_right};")
           
            time.sleep(0.01)
            
