1. is_prime(n) funksiyasi
is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

Misollar:
Kiritish:
4
Natija:
False
(Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)

Kiritish:
7
Natija:
True
(Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
is_prime(7)




2. digit_sum(k) funksiyasi
digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

Misollar:
Kiritish:
24
Natija:
6
(Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

Kiritish:
502
Natija:
7
(Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)


def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print(digit_sum(2599))



3. Ikki sonning darajalari
Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

Misol:
Kiritish:
10
Natija:
2 4 8
(Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)



def print_powers_of_two(n):
    """
    Prints all powers of 2 that are less than or equal to n.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    k = 0
    result = []
    while True:
        power = 2 ** k
        if power > n:
            break
        result.append(power)
        k += 1
    
    # Chop etish
    print(*result)

n = 20
print_powers_of_two(n)
