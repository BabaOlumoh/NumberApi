
def prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print(prime_number(371))

def armstrong_number(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

print(armstrong_number(371))



def perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

print(perfect_number(371))


def digits_sum(number):
    return sum(int(d) for d in str(number))

print(digits_sum(371))


number = 4
properties = []
if armstrong_number(number):
    properties.append("armstrong")
properties.append("odd" if number % 2 != 0 else "even")

print(properties)



