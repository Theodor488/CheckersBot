import random as rand
import board as bd
import move as mv


# Daniel created this Dumb thing
class DumbBot:
    def __init__(self):
        self.x_locations = []   # tracks all positions of x pieces
        self.o_locations = []   # tracks all positions of o pieces
        self.all_valid_moves = []
        self.potential_jumps = []
        self.piece = None
        self.normal_moves = []
        self.all_jump_moves = []

# Searches game board for starting point of all pieces and appends them to locations list
    def dumb_helper(self, board):
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if col == 'x' or col == 'X':
                    self.x_locations.append([x, y])

                if col == 'o' or col == 'O':
                    self.o_locations.append([x, y])

        return [self.x_locations, self.o_locations]

    def is_on_board(self, point):
        row = point[0]
        col = point[1]
        return 1 <= row < 9 and \
            1 <= col < 9

    def select_piece(self, decision):
        if not decision:
            return False

        index = rand.randint(0, len(decision) - 1)
        self.piece = decision[index]
        return self.piece

    def add_to_list(self, viable_moves):
        if viable_moves is not None:
            for i in viable_moves:
                self.all_valid_moves.append(i)

    def valid_ai_move(self, selected_piece):
        self.piece = selected_piece
        if self.piece[0] == 1 and self.piece[1] < 8:
            self.normal_moves.append([self.piece[0] + 1, self.piece[1] + 1])

        elif self.piece[0] == 8 and self.piece[1] < 8:
            self.normal_moves.append([self.piece[0] - 1, self.piece[1] + 1])

        elif 2 <= self.piece[0] < 8 and 0 < self.piece[1] < 8:
            self.normal_moves.append([self.piece[0] + 1, self.piece[1] + 1])
            self.normal_moves.append([self.piece[0] - 1, self.piece[1] + 1])

        return self.normal_moves

    # Checks to see if any moves calculated are taken by its own pieces
    def check_spots(self, current_locations, moves):
        self.x_locations = current_locations[0]
        self.o_locations = current_locations[1]
        self.normal_moves = moves

        for i in self.normal_moves[:]:
            if i in self.o_locations:
                self.potential_jumps.append(i)
                self.normal_moves.remove(i)
                continue
            if i in self.x_locations:
                self.normal_moves.remove(i)
                continue
        # If list is empty then it will return False and you will have to rerun select_piece upto this function
        # in a loop until it is not empty

        self.add_to_list(self.normal_moves)

    def calc_jumps2(self, pieces):
        jumps = []
        for piece in pieces:

            p3 = [piece[0] - 1, piece[1] + 1]
            p4 = [piece[0] + 1, piece[1] + 1]
            jump_left = [piece[0] - 2, piece[1] + 2]
            jump_right = [piece[0] + 2, piece[1] + 2]
            if self.is_on_board(piece) is False:
                break

            elif self.is_on_board(jump_left) is False and \
                    self.is_on_board(jump_right) is False:
                break

            elif jump_left in self.o_locations \
                    and jump_right in self.o_locations:
                break

            elif jump_left in self.x_locations \
                    and jump_right in self.o_locations:
                break

            elif jump_left in self.o_locations \
                    and jump_right in self.x_locations:
                break

            elif jump_left in self.o_locations \
                    and jump_right in self.o_locations:
                break

            if jump_left in jumps \
                    or jump_right in jumps:
                break

            else:

                if p3 in self.o_locations:
                    jumps.append(jump_left)

                if p4 in self.o_locations:
                    jumps.append(jump_right)

                for i in jumps[:]:

                    if i in self.o_locations:
                        jumps.remove(i)

                    elif i in self.x_locations:
                        jumps.remove(i)

                    else:
                        self.all_jump_moves.append(i)
                        self.calc_jumps2(jumps)

        return self.all_jump_moves

    def format_jump_path(self, piece):
        for i, j in enumerate(self.all_jump_moves):
            if [piece[0] + 2, piece[1] + 2] and [piece[0] - 2, piece[1] + 2] in \
                    self.all_jump_moves:
                if j == [piece[0] + 2, piece[1] + 2]:
                    self.all_jump_moves = [self.all_jump_moves[:i], self.all_jump_moves[i:]]
        return self.all_jump_moves


    def temp_name(self):
        for i in self.x_locations:
            moves = self.valid_ai_move(i)
            self.check_spots(i, moves)
            self.calc_jumps2(i)
            print(self.all_moves())

    def all_moves(self):
        if not self.all_valid_moves:
            return False
        else:
            return [[self.all_valid_moves]]


db = DumbBot()
board = bd.Board()
board.generate_board()
game = board.grid
move = mv.Move(game)
print(board.print_player_board())


move.move_piece('o', [1, 6], [2, 5])
move.move_piece('o', [2, 5], [3, 4])
move.move_piece('o', [7, 6], [8, 5])
move.move_piece('o', [6, 7], [7, 6])
move.move_piece('o', [5, 6], [6, 5])
move.remove_piece(1,2)
move.remove_piece(2,1)
move.remove_piece(3,2)

#testing of make_king
move.move_piece("o",[3,6],[2,5])
move.move_piece('o',[2,5],[1,4])
move.move_piece('o',[1,4],[2,3])
move.move_piece('o',[2,3],[1,2])
move.move_piece('o',[1,2],[2,1])


print(board.print_player_board())
x = db.dumb_helper(game)
y = db.valid_ai_move([2, 3])
db.check_spots(x, y)
z = db.calc_jumps2([[2, 3]])
print(db.format_jump_path([2,3]))

"""
move.move_piece('o', [1, 6], [2, 5])
move.move_piece('o', [2, 5], [3, 4])
move.move_piece('o', [7, 6], [8, 5])
move.move_piece('o', [6, 7], [7, 6])
move.move_piece('o', [5, 6], [6, 5])
move.move_piece('o', [4, 7], [5, 6])
move.move_piece('o', [6, 5], [5, 4])
"""