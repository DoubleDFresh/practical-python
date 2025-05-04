# bounce.py
#
# Exercise 1.5
# ball dropped from 100m
# it bounces back 3/5 as high
# write a prog that shows the first 10 bounces - round to 4 digits

ball_height = 100
ball_bounce = 0.60

for bounce in range(1, 11):
    ball_height *= ball_bounce
    print(f"{bounce}  {ball_height:.4f}")
