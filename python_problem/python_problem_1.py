# write by zinhyeok david9pjh@gmail.com
import random


def brGame():
    round_num = 1
    current_num = 0
    # while문 임의로 반복횟수 할당
    while(current_num < 31):
        player_num = 0
        # change playerName by round(odd, even)
        if round_num % 2 == 1:
            playerName = "player"
            while(player_num == 0):
                try:
                    player_num = int(
                        input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
                    if player_num > 3 or player_num < 0:
                        raise IndexError

                except ValueError:
                    print('정수를 입력하세요')
                    player_num = 0
                except IndexError:
                    print('1, 2, 3 중 하나를 입력하세요')
                    player_num = 0

            # print num, add currnt_num
            for i in range(player_num):
                current_num = current_num + 1
                print("{}: {}".format(playerName, current_num))

            round_num = round_num + 1

        # computer play
        else:
            playerName = "computer"
            player_num = random.randint(1, 3)

            # print num, add currnt_num
            for i in range(player_num):
                current_num = current_num + 1
                print("{}: {}".format(playerName, current_num))

            round_num = round_num + 1

    if round_num % 2 == 1:
        print("player win!")
    else:
        print("computer win!")


brGame()
