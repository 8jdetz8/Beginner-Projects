#! python3
# dietCalorieCalculator - Tells you how to adjust your calories depending on
# what you ate earlier in the week.

goal = int(input('Enter your goal calories per day: '))
burnedDaily = int(input('Enter how many calories you burn per day: '))
burnedWeekly = burnedDaily*7
weeklyGoal = goal*7
sinceSunday = int(input('How many days has it been since Sunday? '))
caloriesEaten = []
for i in range(1, sinceSunday + 1):
    caloriesEaten.append(int(input('How many calories did you eat on day ' + str(i)+ '?')))
totalCalories = sum(caloriesEaten)
doggo = ((((burnedDaily*sinceSunday)-totalCalories)*(7/sinceSunday))/3500)
print('You have %d calories and %d days left in the week' % (weeklyGoal - totalCalories, 7 - sinceSunday))
print('That amounts to an average of %d calories per day.' % ((weeklyGoal - totalCalories)/(7 - sinceSunday)))
print('If you stick to your goal calorie count, you\'ll lose %d pound(s) per week.' % ((burnedWeekly - weeklyGoal)/3500))
print('However, if you continue at your current rate of eating for the week, you\'ll \nlose %.1f pound(s) per week.' % (doggo))
