"""
Mr. Vincent works in a door mat manufacturing company.

https://www.hackerrank.com/challenges/designer-door-mat/problem

One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""


def draw_mat(ht, wid):
    """Function to draw mat."""
    pattern = '.|.'
    for i in range(ht):
        row_pattern = pattern * ((ht // 2 - abs(i - ht // 2)) * 2 + 1)
        if i == ht // 2:
            row_pattern = 'WELCOME'
        lines = "-" * ((wid - len(row_pattern)) // 2)
        row = "{0}{1}{2}".format(lines, row_pattern, lines)

        print(row)

if __name__ == "__main__":
    height, width = raw_input('Please input height width separated by space\n').split(' ')
    draw_mat(int(height), int(width))
