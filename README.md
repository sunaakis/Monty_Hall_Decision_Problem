## Monty Hall Decision Problem

The Monty Hall Problem is a decision problem where a player has to decide which of the three doors to chose to find the car which was hidden behind one the three doors given. The design of the game is that once the player choose a door without knowing what is behind the door, the host of the game opens one of the remaining doors. It is important to understand that the host does not choose which door to open randomly. Instead, the choice of the host depends on the player’s choice. So, the choices does not satisfy the condition on independence.<br/>

One of the most accepted solutions is that the assumption of ”the host’s choice of the door does not improve the information set of the player’s choice of door i.e. player still cannot know what is behind the door he picked”. This assumption then help us to conclude that the probability of choosing the door with a car (1/3) remains the same after the host opens a door without the car. The opened door without the car has the probability of 0/3 to have the car. However since the initial probability of the player’s door have the car did not change and remains 1/3; then the probability of the other unopened door has the car (except the player’s) becomes 2/3 (1- 1/3). Therefore, the player is advised to switch to the other unopened door.<br/>

We will try to find alternative solutions with the assumptions that, the player will be asked ’after’ Monty Hall open one of the unchosen doors and that Monty Hall knows where the car is.<br/>

The result of 10.000 trials given the decision of switch after Monty opens a door where a ’goat’ is located behind it, is approximately 67% where the choice of switch is False i.e. the player does not switch to the other closed door; the result of 10.000 trials becomes 33%. The probability of winning the car when not switching after Monty opens a door with a goat is clearly smaller than switching.<br/>

if we extend this game to be formed with 10 doors or n doors we can see that switching is always a better decision. However, the most important part of the multiple door game is that the assumption of Monty Hall will ask the player whether switch or not only 2 doors remain in the game. It does not matter whether Monty Hall opens the doors consecutively, or all n − 2 doors at once. Since Monty cannot open the door that the player chose and the door with a car, he has to leave the player with two doors.<br/>

The code is extended to multiple doors game with door number 10 and the game is repeated 10.000 times. As can be seen the probability of winning the car when deciding to switch become 0.9 contrary to probability of winning the car when not switching 0.1.<br/>

<br/>
Code inspiration. <br/>
https://betterprogramming.pub/solving-the-monty-hall-problem-with-python-46d3f63eadc3
