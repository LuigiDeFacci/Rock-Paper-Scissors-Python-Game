<!DOCTYPE html>
<html>
<body>
	<h1>Rock Paper Scissors Game</h1>
	<p>This is a simple rock paper scissors game implemented using Python and the tkinter module. The game allows the user to choose between rock, paper, and scissors and play against the computer. The rules of the game are defined in a dictionary, and the score is kept track of using variables.</p>
less
Copy code
<h2>How to Play</h2>
<ol>
	<li>Clone or download the repository.</li>
	<li>Open the terminal and navigate to the directory where the file is located.</li>
	<li>Run the following command to start the game:</li>
	<pre><code>python rock_paper_scissors.py</code></pre>
	<li>A window will appear with the game interface.</li>
	<li>Click on the "Rock", "Paper", or "Scissors" button to make your choice.</li>
	<li>The computer will randomly choose its option.</li>
	<li>The result of the game will be displayed in the "Result" section and the scores will be updated accordingly in the "User" and "Computer" sections.</li>
</ol>

<h2>Code Explanation</h2>
<p>The game code is implemented in Python and uses the tkinter module to create a GUI. The game logic is implemented in the <code>play()</code> function which takes the user's choice as an argument. The function selects a random choice for the computer and then uses the rules dictionary to determine the result of the game. Depending on the result, the score and the result label are updated.</p>

<p>The GUI is created using the <code>Tk()</code> function from the tkinter module. The labels and buttons are created using the <code>Label()</code> and <code>Button()</code> functions respectively. The buttons are bound to the <code>play()</code> function using the <code>command</code> parameter.</p>

<p>Finally, the <code>mainloop()</code> of the window is started using the function which waits for user input and updates the window accordingly.</p>
</body>
</html>
