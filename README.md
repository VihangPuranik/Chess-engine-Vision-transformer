# Chess Engine Using Vision transformer
Chess Position Evaluation Using Vision transformer from Scratch

Uses a pretrained Vision Transformer model to analyze the given chess board.
Can take as input a chess board image with white side at bottom and black at the top (as a standard board image)
and evaluate the two results from the given position, one being if the immediate move is for white, and the other
for if the next move is to be from black.

Trains the model against known evaluation for the same positions generated from StockFish Engine.
Higher value (i.e. a positive number) of Evaluation means White has higher chances of a win.
Lower value (i.e. a negative number) of Evaluation means Black has a higher chance of a win.
Evaluation of 0 means a somewhat equal position, very high chances of a draw if both players play ideally.

An example output uses the board.png as a legal chess position in this case.

![board](https://github.com/user-attachments/assets/782f135c-67f7-4ced-a68e-7401be74c6cf)


The StockFish Engine at a depth of 30, gives the evaluation of the position as
1. White to play
  Favoring black in this position.
  The StockFish puts black ahead with an evaluation of -1.63.
3. Black to play
  Favoring black once again, but this time, the position is overwhelmingly in black's favor.
  The Engine evaluation is an overwhelming -6.73 for black over white.

On the other hand, the model has predicted the following evaluation for the same position.
![download](https://github.com/user-attachments/assets/b541abe6-69e9-4a60-acda-340c19e5040d)
