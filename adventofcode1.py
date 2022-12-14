# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 16:32:14 2022

@author: Nicklas Branding
"""


"""
first part of day 1
"""
x = 100; 
biggestvalue = []

while(x>0):
    listWeights = list(map(int, input("Enter multiple weights: ").split()))
    print("List of weights: ", listWeights)
    
    sum = 0
    
    for element in listWeights:
        sum+=element
    
    print(sum)
    biggestvalue.append(sum);
    print(biggestvalue)
    --x
    
    print("Biggest value is: ",max(biggestvalue))    


"""
Second part of day 1
"""
element_list = [25759, 44128, 56961, 50807, 51524, 10514, 63977, 61723, 49769, 56986, 41092, 44974, 42190, 53067, 56628, 29980, 37985, 45758, 38483, 34670, 41766, 28185, 49828, 41320, 47791, 52837, 35533, 39760, 51496, 40057, 55805, 60499, 44045, 52358, 54859, 39747, 48276, 61078, 53141, 44925, 60353, 54648, 39964, 64086, 50420, 50559, 51855, 58275, 51668, 45212, 48327, 23053, 35349, 37969, 30062, 50189, 49697, 46367, 54330, 60500, 54383, 46653, 61562, 44323, 47106, 47413, 53689, 53151, 36180, 58303, 48809, 60281, 58717, 48045, 50021, 41780, 38825, 40656, 38961, 34569, 53659, 31620, 42838, 45210, 49788, 49936, 57277, 40210, 52679, 42426, 35716, 57814, 52189, 53599, 40982, 50406, 42584, 61827, 56206, 50606, 52086, 50685, 3854, 44030, 39841, 50666, 43150, 54681, 50848, 16099, 43187, 44029, 47706, 60513, 57517, 36271, 53563, 44461, 41725, 58991, 51654, 49381, 22640, 56853, 52788, 42731, 60036, 50054, 46973, 45513, 50769, 60801, 45402, 55345, 54701, 36737, 49151, 50248, 38063, 55237, 63781, 56380, 43782, 17434, 46587, 50227, 51191, 44695, 33594, 56391, 52893, 37649, 36344, 62413, 58140, 52437, 35023, 40027, 51800, 48068, 52017, 57529, 67344, 51674, 37529, 39416, 41701, 59561, 57455, 43576, 47622, 51221, 45155, 40721, 45875, 59917, 26357, 41801, 36493, 34510, 45800, 41766, 41217, 53383, 46674, 51860, 60655, 41691, 40352, 59030, 60157, 47316, 50321, 45949, 44456, 37734, 42150, 51933, 60975, 45276, 60157, 44945, 64611, 53086, 20761, 53928, 64983, 51648, 36240, 45413, 45916, 51746, 48843, 41341, 39205, 67658, 50704, 49608, 48663, 48243, 65156, 40085, 44272, 39614, 62622, 51112, 26533, 39147, 53403, 40512, 29854, 21588, 58123, 60746, 43126, 51879, 49435, 57760, 54838, 45193, 50092]


largest = 0
second_largest = 0
third_largest = 0
summa = 0
for element in element_list:
    if element >= largest:
        largest, second_largest, third_largest = element, largest, second_largest
    elif element >= second_largest:
        second_largest, third_largest = element, second_largest
    elif element > third_largest:
        third_largest = element
print(largest)
print(second_largest)
print(third_largest)
summa = largest + second_largest + third_largest
print(summa) 
    
