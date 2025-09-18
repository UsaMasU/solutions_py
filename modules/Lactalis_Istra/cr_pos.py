import time

crane = "TK2"

with open(f"IniPosTraslo_{crane}.ini") as f_data:
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
                    #place = '1' if pos_log[0] == '901' else pos_log[0]
                    #place = '0' if pos_log[0] == '999' else pos_log[0]
                    #place = pos_log[0]
                  
                    if pos_log[0] == '901': 
                        place = '1'
                    elif pos_log[0] == '999':
                        place = '0'
                    else:
                        place = pos_log[0]
                    
                    x = pos_raw[0]
                    y = pos_raw[1]
                    
                    if side == '1' or side == '2':
                        deep = 1
                    elif side == '3' or side == '4':
                        deep = 2
                    
                    if side == '1':
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].X := {x};", file=f_side_1)
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].Y := {y};", file=f_side_1)
                        
                    if side == '2':                        
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].X := {x};", file=f_side_2)
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].Y := {y};", file=f_side_2)
                                          
                    if side == '3':                   
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].X := {x};", file=f_side_1)
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].Y := {y};", file=f_side_1)
                                           
                    if side == '4':                    
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].X := {x};", file=f_side_2)
                        print(f"Deep[{deep}].Shelf_{shelf}[{place}].Y := {y};", file=f_side_2)                    
                                           
                    print(f"Deep[{deep}].Shelf_{shelf}[{place}].X := {x};")
                    print(f"Deep[{deep}].Shelf_{shelf}[{place}].Y := {y};")

            time.sleep(0.01)
            
        print(f"Deep_Value[1].Z := 0;", file=f_side_1)
        print(f"Deep_Value[2].Z := 0;", file=f_side_1)
        print(f"Deep_Value[1].Z := 0;", file=f_side_2)
        print(f"Deep_Value[2].Z := 0;", file=f_side_2)

        print(f"Deep_Value[1].Z := 0;")
        print(f"Deep_Value[2].Z := 0;")
        print(f"Deep_Value[1].Z := 0;")
        print(f"Deep_Value[2].Z := 0;")
                    
            
