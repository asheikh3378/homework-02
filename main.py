# Alissa Sheikh 1623952
# Numerous engineering and scientific applications require finding solutions to a set of equations.
# Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2. Given integer coefficients of two linear
# equations with variables x and y, use brute force to find an integer solution for x and y in the range -10 to 10.
# reference chegg.com/homework-help/questions-and-answers/520-lab-brute-force-equation-solver-numerous-engineering
# -scientific-applications-require-f-q107719203?trackid=a96d70f57f32&strackid=07f8a932848a and
# chegg.com/homework-help/questions-and-answers/518-lab-brute-force-equation-solver-python-numerous-engineering
# -scientific-applications-re-q84882601?trackid=7e1a2680ef22&strackid=07f8a932848a
# Use this brute force approach:
# For every value of x from -10 to 10
# For every value of y from -10 to 10
# Check if the current x and y satisfy both equations. If so, output the solution, and finish.


# inputs
One = int(input())
Two = int(input())
Three = int(input())
Four = int(input())
Five = int(input())
Six = int(input())
possible_solution = False

# Loop to go through the -10 to 11
for x in range(-10, 11):
    # Loop to -10 and 11
    for y in range(-10, 11):
        # Brute Force Approach
        if One * x + Two * y == Three and Four * x + Five * y == Six:
            # Solution
            print('{}'.format(x), '{}'.format(y))
            # Update if the solution is found
            possible_solution = True
            break

# Checking if no solution or not
if not possible_solution:
    print('No solution')
