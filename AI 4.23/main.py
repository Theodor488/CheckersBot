import board as bd
import dumb_Bot as db
import move as mv


# Theo fid the main
if __name__ == '__main__':
    print("yea boi")
    board = bd.Board()
    bot = db.DumbBot()
    move = mv.Move(board.grid)
    print('Checker Wars')

    playing = True
    board.generate_board()

    while playing:

        if bot.o_locations is None or bot.x_locations is None:
            playing = False
            break

        print(board.print_player_board())

        initial_coords_list = []
        for i in range(0, 2):
            item = int(input("Enter coord of chosen O: "))
            initial_coords_list.append(item)
        print(initial_coords_list)

        moved_coords_list = []
        for i in range(0, 2):
            item = int(input("Enter coord of where to move O: "))
            moved_coords_list.append(item)
        print(moved_coords_list)

        move.move_piece('o', initial_coords_list, moved_coords_list)
        board.print_player_board()

        comp_turn = True
        piece_not_selected = True
        while comp_turn:

            pieces = bot.dumb_helper(board.grid)
            while piece_not_selected:

                x_pieces = pieces[0]
                o_pieces = pieces[1]

                old_coor = bot.select_piece(x_pieces)
                print(old_coor)
                moves = bot.valid_ai_move(old_coor)
                valid_moves = bot.check_spots(pieces, moves)
                bot.calc_jumps(old_coor)
                print(bot.potential_jumps)
                all_moves = bot.all_moves()
                print(old_coor, all_moves)

                if all_moves is False:
                    moves = []
                    valid_moves = []
                    all_moves = []
                    bot.normal_moves = []
                    bot.potential_jumps = []
                    bot.all_valid_moves = []
                    bot.x_locations = []
                    bot.o_locations = []

                else:
                    moves = []
                    new_coor = bot.select_piece(all_moves)
                    move.move_piece('x', old_coor, new_coor)
                    bot.all_valid_moves = []
                    all_moves = []
                    bot.normal_moves = []
                    bot.all_valid_moves = []
                    pieces = []
                    bot.x_locations = []
                    bot.o_locations = []
                    x_pieces = []
                    o_pieces = []
                    bot.potential_jumps = []
                    new_coor = None
                    piece_not_selected = False
                    comp_turn = False
                    break
    print('gg')

