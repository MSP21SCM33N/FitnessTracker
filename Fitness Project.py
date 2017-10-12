#Fitness Tracker
miles = int(input("Welcome to the calorie calculator!\nHow far did you travel today? (Miles)"))
weight = int(input("How much do you weigh?(lbs)"))
travel = input("Finally, did you run or walk?")

if travel == 'walk':
    caloriesBurnt = .53 *weight * miles
    print("You burnt ", caloriesBurnt, " calories while walking today!")
elif travel == 'run':
    caloriesBurnt = .75 * weight * miles
    print("You burnt ", caloriesBurnt, " calories while running today!")

