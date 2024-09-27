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
