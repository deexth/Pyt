def solution(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }
    roman_string = int()
    for value in sorted(roman_numerals.values(), reverse=True):
        while n >= value:
            roman_string += roman_numerals[value]
            n -= value
    # return roman_string
    print(roman_string)


solution('XXI')
