### 475. Heaters
The concept is to find the cloest heater for each house. So we can search in the heaters for each house.
1. Using bisect : Binary search to find the position of each house in the heaters.
2. Sort then compare : Sort houses and heaters first, then each time compare the house and the `(heaters[i] + heaters[i+1])//2`. If house is bigger, then `i+=1`. Else compare the current max radius and `abs(house - heaters[i])`.
