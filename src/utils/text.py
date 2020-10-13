def word_ending_by_number(number :int) -> str:
    number = abs(number)
    if number in range(11, 20):
        return 'ов'
    x = number % 10
    if x == 1:
        return ''
    elif x in range(2, 5):
        return 'а'
    else:
        return 'ов'