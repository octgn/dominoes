dominoes
========

a legally-distributable game definition for OCTGN.

The Dominoes game definition supports Double-Six and Double-Nine games.  This game definition is uniquely programmed to run without having to load a deck.  It does so by generating the domino draw pile through the Python scripts and stores into a shared global variable.  Manual shuffling of the draw pile is not required or provided.

When in a game, any player can initiate the deck by selecting "Start a Double-Six Game" or "Start a Double-Nine Game", which generates the Draw Pile and deals a chosen number of dominoes to each player.  The "Draw a Domino" function is hotkeyed to ctrl+shift+D.

An invisible snap-to grid is utilized to help players place their dominoes correctly.  To further aid the player in correct placements, the conventional W/A/S/D keys in combination with CTRL will move the domino one space in the given direction.  CTRL+E will rotate the domino clockwise, CTRL+Q will rotate counterclockwise.

Some simple locking and error-proofing mechanisms are in place to prevent accidental erroring of the Draw Pile system.
1) Players MUST restart the game with the restart button in order to generate a new Draw Pile.  This is verified by the New Game functions by counting the number of dominoes on the table, in the discard pile, and in the local player's hand.
2) Once the New Game script has been commenced, the Draw Pile becomes locked.  This is to prevent other players from simultaneously starting another new game, or drawing cards.  The pile becomes unlocked after the script finishes.
3) The New Game function will not let the script proceed if the number of cards dealt to each player exceeds the number of cards in the Draw Pile.
4) Players cannot draw cards from an empty Draw Pile.