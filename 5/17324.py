
def deletion(number: str) -> str:
    return number[:number.find('1')] + number[number.find('1', 2):]

print(deletion("010010"))