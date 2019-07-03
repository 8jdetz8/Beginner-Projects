#! python3
# dietCalorieCalculator - Tells you how to adjust your calories depending on
# what you ate earlier in the week.

goal = int(input('Enter your goal calories per day: '))
weeklyGoal = goal*7
sinceSunday = int(input('How many days has it been since Sunday? '))
caloriesEaten = []
for i in range(1, sinceSunday + 1):
    caloriesEaten.append(int(input('How many calories did you eat on day ' + str(i)+ '?')))
totalCalories = sum(caloriesEaten)
print('You have %d calories and %d days left in the week' % (weeklyGoal - totalCalories, 7 - sinceSunday))
print('That amounts to an average of %d calories per day.' % ((weeklyGoal - totalCalories)/(7 - sinceSunday)))
