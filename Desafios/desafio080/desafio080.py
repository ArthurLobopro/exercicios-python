sequence = []
maior = 0

for a in range(5):
    num = int(input(f"Digite o {a+1}° número: ").strip())

    if a == 0:
        maior = num
        sequence.append(num)
        continue
    
    if num >= maior:
        sequence.append(num)
    else:
        for i,v in enumerate(sequence):
            if v > num:
                sequence.insert(i, num)
                break

print(f"Sequencia ordenada: {sequence}")