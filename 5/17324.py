
def deletion(number: str) -> str:
    return number[number.find('1', number.find('1')+1):]

print(deletion("010010"))