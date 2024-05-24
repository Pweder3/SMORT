import array
import gc
import random

Myarray = array.array('f',[0])  
My2array = array.array('f',[0])  
My3array = array.array('f',[0])  
My4array = array.array('f',[0])  

index = 0

while True:
    if len(Myarray) < 2000:
        
        Myarray.append(random.random())
        My2array.append(random.random())
        My3array.append(random.random())
        My4array.append(random.random())
    else:
        Myarray[index] = random.random()
        My2array[index] = random.random()
        My3array[index] = random.random()
        My4array[index] = random.random()
        
        index += 1
        if index > 1999:
            index = 0
    
    print(f"memFree: {gc.mem_free()}, memAlloc: {gc.mem_alloc()}, {len(Myarray)}")