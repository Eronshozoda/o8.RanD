from datetime import datetime, timedelta
import random
print("Generate a random integer between 0 and 6:")
print(random.randrange(5))
print("Generate random integer between 5 and 10, excluding 10:")
print(random.randrange(start=5,stop=10))
print("Generate random integer between 0 and 10, with a step of 3:")
print(random.randrange(start=0,stop=10,step=3))
print("Random date between two dates:")
first_data = datetime.date(2019,9,1)
second_data = datetime.date(2024,5,9)