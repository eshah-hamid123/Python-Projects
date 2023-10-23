number = int(input())
count = "{0:b}"
spaces = len(count.format(number))
spaces+= 1
for i in range(1, number+1):
    bin_num = '{0:b}'
    bin_num = bin_num.format(i)
    hex_num = '{0:X}'
    hex_num = hex_num.format(i)
    oct_num = '{0:o}'
    oct_num = oct_num.format(i)
    # txt = "str.({0}).rjust(spaces, ' '){0:o} {0:X} {0:b}"
    print(str(i).rjust(spaces, ' ') + oct_num.rjust(spaces, ' ') + hex_num.rjust(spaces, ' ') + bin_num.rjust(spaces,' '))
