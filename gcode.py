import chess

UP = "G1 Z400"
DOWN = "G1 Z0"

HOME = "G28"
GRIP_CLOSE = "M340 P0 S500"
GRIP_OPEN = "M340 P0 S500 R3"

MAP = {
    "GY": "-500000000",
    "a1": "X100 Y100",
    "a2": "X200 Y200",
    "a3": "",
    "a4": "",
    "a5": "",
    "a6": "",
    "a7": "",
    "a8": "X88 Y5",
    "b1": "",
    "b2": "",
    "b3": "",
    "b4": "",
    "b5": "",
    "b6": "",
    "b7": "",
    "b8": "X100 Y-5",
    "c1": "",
    "c2": "",
    "c3": "",
    "c4": "double blah",
    "c5": "",
    "c6": "",
    "c7": "",
    "c8": "X115 Y-12",
    "d1": "",
    "d2": "",
    "d3": "",
    "d4": "",
    "d5": "blah",
    "d6": "",
    "d7": "",
    "d8": "X135 Y-17",
    "e1": "",
    "e2": "",
    "e3": "",
    "e4": "",
    "e5": "",
    "e6": "",
    "e7": "",
    "e8": "X42 Y298",
    "f1": "",
    "f2": "",
    "f3": "",
    "f4": "",
    "f5": "",
    "f6": "",
    "f7": "",
    "f8": "X63 Y291",
    "g1": "",
    "g2": "",
    "g3": "",
    "g4": "",
    "g5": "",
    "g6": "",
    "g7": "",
    "g8": "X80 Y285",
    "h1": "",
    "h2": "",
    "h3": "",
    "h4": "",
    "h5": "",
    "h6": "",
    "h7": "",
    "h8": ""
}


def generate_gcode_move(move):
    """
    G5 X## Y##: Move to Direction (Angle)
    G1 Z###: Move Up or Down
    G28: Home
    M340 P0 S#### (500 - 2500): Grip Close
    M340 P0 S500 R3: Grip Open

    M84: Disable all stepper motors
    M112: Safety Kill Everything

    - Move to direction (angle)
    - Move down
    - Grip
    - Up
    - Home
    - Move direction
    - Down
    - Ungrip
    - Up
    - Home
    """

    from_square = move[:2]
    to_square = move[2:]

    gcode = []
    gcode.append(HOME)
    gcode.append("G5 " + MAP[from_square])
    gcode.append(DOWN)
    gcode.append(GRIP_CLOSE)
    gcode.append(UP)
    gcode.append(HOME)
    gcode.append("G5 " + MAP[to_square])
    gcode.append(DOWN)
    gcode.append(GRIP_OPEN)
    gcode.append(UP)
    gcode.append(HOME)

    return gcode

def generate_gcode(board, move):
    if board.is_capture(chess.Move.from_uci(move)):
        from_square = move[:2]
        to_square = move[2:]

        first_move = generate_gcode_move(to_square + "GY")
        second_move = generate_gcode_move(move)

        return "\n".join(first_move + second_move)

    elif board.is_castling(chess.Move.from_uci(move)):
        if move == "e8c8":
            # Move king to c8: "e8c8"
            first_move = generate_gcode_move("e8c8")
            # Move bishop: "a8d8"
            second_move = generate_gcode_move("a8d8")

            return "\n".join(first_move + second_move)

        elif move == "e8g8":
            # Move king: "e8g8"
            first_move = generate_gcode_move("e8g8")
            # Move bishop: "h8f8"
            second_move = generate_gcode_move("h8f8")

            return "\n".join(first_move + second_move)
    else:
        return "\n".join(generate_gcode_move(move))

b = chess.Board()
b.push_uci("c2c4")
b.push_uci("d7d5")
b.push_uci("a2a3")

gcode_string = generate_gcode(b, "d5c4")

f = open("inputs.txt", "w")
f.write(gcode_string)
f.close()