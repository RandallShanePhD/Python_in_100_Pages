# Python in 100 Pages - v2
# Math Example

'''A train leaves the station at noon and travels for 4 hours in a straight line.  It takes the train 30 minutes to accelerate and 30 minutes to decelerate.  The average speed when it is accelerating or decelerating is 30 miles per hour.  At full speed, the train travels at 60 miles per hour.  How many miles did the train cover?'''

# Digest the problem
# 4 hours total travel time
# Full speed = 60 mph
# Half speed = full speed * .5
# 30 (.5 hours) minutes accelerating at half speed
# 3 hours at full speed
# 30 (.5 hours) minutes decelerating  at half speed

# Set the variables
full_speed = 60
half_speed = full_speed * .5

accelerate_hours = .5
full_speed_hours = 3
decelerate_hours = .5

# Apply the formula
total_miles = (half_speed * accelerate_hours) + (full_speed * full_speed_hours) + (half_speed * decelerate_hours)

print('Total Miles: ', total_miles)
