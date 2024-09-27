'''
Default 
'''
import board
import players
from PIL import Image, ImageDraw, ImageFont
import os, sys

def draw_board(pos, pov=1):
    '''
    Generate an output image of the current board status
    pos - FEN Notation Board status
    PoV parameter shows the Board in:
        0: White Perspective
        1: Black Perspective
        2: Neutral/Normal Perspective
    '''
    print("FEN of the position is :", pos)
    bk = Image.open('assets/bK.png')
    bq = Image.open('assets/bQ.png')
    br = Image.open('assets/bR.png')
    bn = Image.open('assets/bN.png')
    bb = Image.open('assets/bB.png')
    bp = Image.open('assets/bP.png')

    wk = Image.open('assets/wK.png')
    wq = Image.open('assets/wQ.png')
    wr = Image.open('assets/wR.png')
    wn = Image.open('assets/wN.png')
    wb = Image.open('assets/wB.png')
    wp = Image.open('assets/wP.png')

    img  = Image.open('assets/ChessBoard.png')
    draw = ImageDraw.Draw(img)

    fontname = ImageFont.truetype('assets/font.ttf', 20)
    if pov == 1:
        draw.rectangle(xy=(225, 12, 240, 27), fill=(0,0,0), outline=(128,0,0), width=2)
        draw.text((250, 10), 'TO MOVE', font=fontname, fill=(128,0,0))
    else:
        draw.rectangle(xy=(225, 12, 240, 27), fill=(255,255,255), outline=(128,0,0), width=2)
        draw.text((250, 10), 'TO MOVE', font=fontname, fill=(128,0,0))


    x=0
    y=0
    count = 0
    fen_piece_loc = pos.split()[0]
    for char in pos:
        y = count // 8
        x = count % 8
        match char:
            case 'p':
                img.paste(bp, (35+60*x, 35+60*y), bp.convert('RGBA'))
            case 'n':
                img.paste(bn, (35+60*x, 35+60*y), bn.convert('RGBA'))
            case 'b':
                img.paste(bb, (35+60*x, 35+60*y), bb.convert('RGBA'))
            case 'r':
                img.paste(br, (35+60*x, 35+60*y), br.convert('RGBA'))
            case 'q':
                img.paste(bq, (35+60*x, 35+60*y), bq.convert('RGBA'))
            case 'k':
                img.paste(bk, (35+60*x, 35+60*y), bk.convert('RGBA'))

            case 'P':
                img.paste(wp, (35+60*x, 35+60*y), wp.convert('RGBA'))
            case 'N':
                img.paste(wn, (35+60*x, 35+60*y), wn.convert('RGBA'))
            case 'B':
                img.paste(wb, (35+60*x, 35+60*y), wb.convert('RGBA'))
            case 'R':
                img.paste(wr, (35+60*x, 35+60*y), wr.convert('RGBA'))
            case 'Q':
                img.paste(wq, (35+60*x, 35+60*y), wq.convert('RGBA'))
            case 'K':
                img.paste(wk, (35+60*x, 35+60*y), wk.convert('RGBA'))

            case '/':
                count -= 1
        if char.isnumeric():
            count += int(char)-1
        count += 1
    img.resize((224,224))
    img.save('board.png')
    print("Done")

os.chdir(sys.path[0])

board = board.Board()

white = players.Player(0, None)
black = players.Player(1, None)

draw_board('8/2R1Q1pk/3N1r1p/3P4/8/6P1/2R3KP/5q2')
