# There are 2 Task in this assignment and need to write the program in python.

1) First one:-

File name: Md Shad.py

Write a program to select paper bill denominations in an ATM.

The input is the value requested by the customer. Check if the value is a multiple of 5 (smallest available bill). Break down the value into bills of 100, 50, 10 and 5, using the largest possible bills.

Examples:
Withdrawing $375:
3 bills of $100
1 bill of $50
2 bills of $10
1 bill of $5
Withdrawing $57:
Sorry, amount must be a multiple of 5

2) Second Task:- 

File name: challenge.py

1: Surface and Battery Detection
Create a program that can detect the type of surface the robot is traveling on and adjust its movement accordingly, while also monitoring the battery level:

Get user input for the surface type (carpet, tile, grass) and the battery level (0-100%)
Implement the following logic:
If the surface is carpet and the battery level is above 50%, the robot should increase its wheel torque
If the surface is tile or the battery level is below 20%, the robot should maintain normal wheel torque
If the surface is grass and the battery level is below 50%, the robot should decrease its wheel torque to avoid getting stuck
Your program should output messages like:

"🚨 Carpet detected with high battery. Increasing wheel torque for better traction."
"🟢 Tile surface. Maintaining normal wheel torque."
"⚠️ Grass detected with low battery. Decreasing wheel torque to prevent getting stuck."