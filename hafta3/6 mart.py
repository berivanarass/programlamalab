#TT YY space, TY YT event
# * icerideki degerleri tek tek alip virgulle birlestirip gonderen bir yapi

from sympy import FiniteSet

t = FiniteSet(1,2,3)
s = FiniteSet(2,4,6)
if t == s:
    print("True")
else:
    print("False")
print(t.union(s))
print(t.intersect(s))
print(t**2) 

#event belirli bir olayı belirtir , space ise orneklem uzayını belirtir.

def probability(space, event):
    return len(event)/len(space)

#asal mi
def check_primes(number):
    if number != 1:
        for factor in range (2, number):
            if number%factor == 0:
                return False
    else:
        return False

    return True


space = FiniteSet(*range(1,21))
# append fonksiyonu icin 34.satirı yapmamız lazım. baslangic degeri vermek icin /initialize etmek için.
primes = []
for num in space:
#bütün degerler icin asal olup olmadigina bakılıyor.
    if check_primes(num):
        primes.append(num)
    event = FiniteSet(*primes)
    p = probability(space, event)
    print(p)


file1 = open("my_f.txt", "r")
file1.readlines()
content = file1.readlines()
print(content)

for line in content :
    for item in line:
        print(item)