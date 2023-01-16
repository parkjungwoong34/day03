# while

numbers = [1, 3, 10]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: # break 문이 호출되지 않은 경우
    print('No even number found')



# while True:
#     dan = int(input('Dan (0 to quit): '))
#
#     if dan == 0: # exit
#         break
#     if 1 < dan < 10: #  if dan >= 2 and dan <= 9:
#         i = 1
#         while i < 10:
#             print('{0} * {1} = {2}'.format(dan, i, dan * i))
#             i = i + 1
#     else:
#         print('2에서 9사이의 값을 입력하세요')