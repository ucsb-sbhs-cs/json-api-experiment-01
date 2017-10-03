import json
import json

with open('car_dimensions.json') as data_file:    
    data = json.load(data_file)

print("The width of the car is: ",data["Width"]," cm")
print("The height of the car is: ",data["Height"]," cm")
print("The length of the car is: ",data["Length"]," cm")

