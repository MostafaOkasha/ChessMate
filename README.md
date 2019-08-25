# ChessMate
A Scara Robot that plays chess! (With a lot of image recognition)

## About:
### How it works:
With a camera attached to a raspberry pi, an image is taken of the board state at the beginning of the game to determine that all pieces are in their designated spots. The exact pieces are not recognized but isntead, whether a piece occupies a square within the board is all the information that is required. The only assumption is that the user begins the game with all pieces in their right positon. With that in mind, whenever a piece is moved from one location to another, one square will be detected as not occupied and another square as occupied. This only works for moves that do not involve attacking and for that we have a solution! By identifying if the piece occupying the square is a white or black piece (blue and red in our case because it was easier to detect with way less errors), we are able to determine all types of moves that occur on the board and also validate the moves using an open source chess library. 

The process is as follows:

* User sets up the board with the correct pieces in place.
* User makes a move, lets say B2 to B3.
* User presses a button to tell the system that they have completed their move.
* An image of the game board is taken.
* Our beautiful neural network crops the image into a perfect square so that each square on the board is identifiable by pixel location. For example, square B2 would have the pixel range for x:(500:1000) and for y:(0:500) since its in the second column first row.
* Using pixel counting and a calibrated pixel threshold value, we can determine if a piece is present within that square and the color of that piece.
* Using a differences table, the exact move can be determined and passed on to the game logic system to determine the validity of the move.
* If the move is invalid, the system mentions this to the user.
* If the move was valid, the game logic will determine a move for the user and send the exact gcode coordinates to move the piece.

### What about everything else?

This entire code was running on an AWS EC2 server and interacting with an AWS S3 database to retrieve images taken from the board. The neural network image crop required a lot of processing power that was simply too slow to have running on the Raspberry Pi. The Pi, connected to a camera, interacts with the user and captures the image when required. It then processes the image and uploads it to the database where the server is alerted. This is where this code comes to play and does all the processing. The gcode is processed and sent to the raspberry pi which sends it to an Arduino. This is where the communication with the robot arm takes place.

