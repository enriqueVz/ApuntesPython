from collections import Counter

numeros = [1,1,1,1,2,2,2,3,3,4,5,5,5]
print(Counter(numeros))

stro = "missisipi y muerte a lo hippi"
print(Counter(stro.split()))

serie = Counter([1,1,1,1,2,2,2,3,3,4,5,5,5,5,5,5,5,5,6])
print(list(serie))