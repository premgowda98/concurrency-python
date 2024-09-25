## Multiprocessing

1. When ever the process is created it runs from top to bottom
2. So Creating process should be inside `if __name__=="__main__`
3. This will make sure it runs only on the main process


The below code runs infinitely where each process calls other process

```python
import os
from multiprocessing import Process, current_process, Pool
import time


def square(num):
    s=0
    for i in range(num):
        s+=i*i
    return s 

with Pool(4) as pool:
    # Submit tasks using map
    numbers = [1, 2, 3, 4, 5]
    results = pool.map(square, numbers)
    print(results)
```