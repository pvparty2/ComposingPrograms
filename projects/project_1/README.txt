This project was obtained from: https://inst.eecs.berkeley.edu//~cs61a/fa13/proj/hog/hog.html

This project is used to showcase higher-order functions.

I only made changes to the hog.py and README.txt. The 3 other files and 1 folder were obtained online. (scrap.py is scrap paper)

The following quote is copied from the website:

"In this project, you will develop a simulator and multiple strategies for the dice game Hog. You will need to use control and higher-order functions together, from Sections 1.1 through 1.6 of the Composing Programs online text.

In Hog, two players alternate turns trying to reach 100 points first. On each turn, the current player chooses some number of dice to roll, up to 10. Her turn score is the sum of the dice outcomes, unless any of the dice come up a 1, in which case the score for her turn is only 1 point (the Pig out rule).

To spice up the game, we will play with some special rules:

Free bacon. If a player chooses to roll zero dice, she scores one more than the largest digit in her opponent's score. For example, if Player 1 has 42 points, Player 0 gains 1 + max(4, 2) = 5 points by rolling zero dice. If Player 1 has 48 points, Player 0 gains 1 + max(4, 8) = 9 points.
Hog wild. If the sum of both players' total scores is a multiple of seven (e.g., 14, 21, 35), then the current player rolls four-sided dice instead of the usual six-sided dice.
Swine swap. If at the end of a turn one of the player's total score is exactly double the other's, then the players swap total scores. Example 1: Player 0 has 20 points and Player 1 has 5; it is Player 1's turn. She scores 5 more, bringing her total to 10. The players swap scores: Player 0 now has 10 points and Player 1 has 20. It is now Player 0's turn. Example 2: Player 0 has 90 points and Player 1 has 50; it is Player 0's turn. She scores 10 more, bringing her total to 100. The players swap scores, and Player 1 wins the game 100 to 50."

hog.py:
	Apart from _digits_ and _can_swap_ global functions, I written my code in all the sections with the following label: "*** YOUR CODE HERE ***".
	I had no hog_grader.py to test my code, so I had to make do with hog_gui.py and the python terminal.

images:
	Images of dice sides. Used by hog_gui.py.





