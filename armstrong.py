number = 1634
digits = len(str(number))
temp = number
add_sum = 0
while temp != 0:
    # get the last digit in the number
    k = temp % 10
    # find k^digits
    add_sum += k**digits
    # floor division
    # which updates the number with the second last digit as the last digit
    temp = temp//10
if add_sum == number:
    print('Given number is an Armstrong Number')
else:
    print('Given number is not a Armstrong Number')

