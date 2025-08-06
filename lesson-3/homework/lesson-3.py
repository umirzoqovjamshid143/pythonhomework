1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.

mevalar=['olma','gilos','qulupnay','shaftoli','olcha']

print(mevalar[2])


2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.

a = [1, 2, 3]
b = [4, 5, 6]

birlashtirish = a + b

print(birlashtirish)

3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

l1=[10,20,30,40,50,60,70,80,90]
birinchi=l1[0]
orta=l1[len(l1)//2]
oxirgi=l1[-1]

print(birinchi,orta,oxirgi)


4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.

l2 = ['Inception', 'The Matrix', 'Interstellar', 'Titanic', 'Avatar']

qotgan = tuple(l2)
print(qotgan)




5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.

davlatlar = ['uzbek', 'qozoq', 'tojik', 'Paris', 'rassia', 'usa']

if 'Paris' in davlatlar:
 
    print('Bu davlat royxatda bor')
else:
    print('Bu davlat royxatda yoq')


6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.

sonlar = [1, 2, 3, 4, 5]

ikki_marta = sonlar * 2

print(ikki_marta)


7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.

numbers=[10,20,30,40,50]

numbers[0],numbers[-1]=numbers[-1],numbers[0] 
print(numbers)

8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

sonlar = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

kesilgan_qism = sonlar[3:8]

print(kesilgan_qism)

9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.

ranglar = ["red", "blue", "green", "blue", "yellow", "blue"]
soni_qancha=ranglar.count("blue")
print(soni_qancha)


10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".

hayvonlar=('buri','ayiq','tulki','lion','quyon','sigir','echki','it')

ajratish=hayvonlar.index('lion')
print(ajratish)


11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.

son1=(12,23,34,45,56,67,78,89,90)
son2=(1968,1971)
birlashtirmoq=son1+son2
print(birlashtirmoq)


12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.

son = (10, 20, 30, 40, 50, 60, 70)
meva = ['olma', 'banan', 'olcha', 'behi', 'nok']
mevauzunligi = len(meva)
sonuzunligi = len(son)
print('Mevalar uzunligi:', mevauzunligi)
print('Tuple uzunligi:', sonuzunligi)

13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.

mytuple=(50,60,70,80,90)
mylist=list(mytuple)

print(mylist)


14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.

sonlar1=(10,20,30,40,50,60,70,80,90)
sonmax=max(sonlar1)
sonmin=min(sonlar1)


print('maxsimalson',sonmax)
print('minimalson' ,sonmin)


15. Reverse a Tuple
Create a tuple of words and print it in reverse order.

sozlar = ('salom', 'dunyo', 'python', 'kod', 'misol')

teskari=sozlar[::-1]
print(teskari)



