import random

lotto_num = []
my_lotto = []

win_count = [0, 0, 0, 0, 0]

for i in range(1, 46):
    lotto_num.append(i)
    my_lotto.append(i)


def win_number():
    random.seed
    random.shuffle(lotto_num)
    return lotto_num[0:7]


def pick_number():
    random.seed
    random.shuffle(my_lotto)
    return my_lotto[0:6]


def buy_lotto_a_week(amount):
    win = win_number()
    bonus = win[6]
    win = win[0:6]

    for _ in range(amount):
        pick = pick_number()
        # print(pick)

        match_count = 0
        is_bonus_matched = False

        for i in range(6):
            if pick[i] in win:
                match_count += 1
            if pick[i] == bonus:
                is_bonus_matched = True

        win_counter(match_count, is_bonus_matched)


def win_counter(match_count, is_bonus_matched):
    if match_count == 6:
        win_count[0] += 1
    elif match_count == 5:
        if is_bonus_matched:
            win_count[1] += 1
        else:
            win_count[2] += 1
    elif match_count == 4:
        win_count[3] += 1
    elif match_count == 3:
        win_count[4] += 1


def print_result():
    for i in range(5):
        print(str(i + 1) + '등 : ' + str(win_count[i]) + '번')


def buy_lotto_a_year(weekly_amount, year):
    for _ in range(52 * year):
        buy_lotto_a_week(weekly_amount)


buy_lotto_a_year(1, 100)
print_result()
