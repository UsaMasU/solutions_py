import time

crane = "CR2"

with open(f"{crane}_IniPosTraslo1.ini") as f_data:
    content = list(filter(None, f_data.read().split('\n')))

    with open(f"{crane}_side_1_xy.txt", "w") as f_side_1, open(f"{crane}_side_2_xy.txt", "w") as f_side_2 :
        
        for item in content:         
            start_pos_log = item.find('(')
            end_pos_log = item.rfind(')') + 1 
            pos_log = item[start_pos_log:end_pos_log].replace("(", "").replace(")", "")
            if len(pos_log) > 0:
                eq_symb = item.find('=') + 1
                pos_raw = item[eq_symb:]
                pos_log = ' '.join(pos_log.split())        
                pos_raw = ' '.join(pos_raw.split())
                if len(pos_raw) > 1:
                    pos_log = pos_log.split(':')
                    pos_raw = pos_raw.split(':')
                    
                    side = pos_log[2]
                    shelf = pos_log[1]
                    place = '1' if pos_log[0] == '901' else pos_log[0]
                    x = pos_raw[0]
                    y = pos_raw[1]
                    
                    if side == '1':
                        print(f"Shelf_{shelf}[{place}].X := {x};", file=f_side_1)
                        print(f"Shelf_{shelf}[{place}].Y := {y};", file=f_side_1)
                    if side == '2':
                        print(f"Shelf_{shelf}[{place}].X := {x};", file=f_side_2)
                        print(f"Shelf_{shelf}[{place}].Y := {y};", file=f_side_2)
                    
                        print(f"Shelf_{shelf}[{place}].X := {x};")
                        print(f"Shelf_{shelf}[{place}].Y := {y};")
                
            time.sleep(0.01)
            
