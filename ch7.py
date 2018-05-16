months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n=int(input("Enter a month number: "))
begin=int((n-1)*3)
end=begin+3
abb=months[begin:end]
print('The 3 letter abbreviation is ', abb)

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))