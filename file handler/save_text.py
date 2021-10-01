
f = open('text.txt', 'w', encoding='utf-8')

f.write('이유빈:')
f.write('초록색')
f.write('\n')
f.write('김효진:')
f.write('하늘색')

f.close()

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('이유빈:')
    f.write('초록색')
    f.write('\n')
    f.write('김효진:')
    f.write('하늘색')  # close() 필요없음 with나갈때 자동으로 close()함