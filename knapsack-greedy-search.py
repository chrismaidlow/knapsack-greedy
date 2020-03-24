def value(item):
    
    total_value = item[0] / item[1]
    
    return total_value


def greedy(max_weight, objects):
    
    ordered_objects = []
    
    for current_item in objects:
        
        tv = value(current_item)
        
        if not ordered_objects:
            
            ordered_objects.append(current_item)
            
        else:
        
            for item in ordered_objects:
            
                tv2 = value(item)
            
                if tv >= tv2:
                    
                    if ordered_objects.index(item) == 0:
                        
                        ordered_objects.insert(0, current_item)
                        break
                        
                
                    else:
                        
                        ordered_objects.insert(ordered_objects.index(item), current_item)
                        break
                    
                elif len(ordered_objects) == (ordered_objects.index(item)+1):
                    
                    ordered_objects.append(current_item)
                    break
                        
                else:
                    
                    continue
    order2 = [] 
    max_cap = max_weight
    capacity = 0
                
    for item in ordered_objects:
        
        if (capacity + item[1]) < max_cap:
            
          order2.append(item)  
          capacity = capacity + item[1]
    
    return order2
    