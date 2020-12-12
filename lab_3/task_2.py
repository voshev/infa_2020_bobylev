import turtle

with open('font.txt') as shr:
    sh = shr.readlines()
    zero = sh[0].rstrip().split('\t')
    one = sh[1].rstrip().split('\t')
    two = sh[2].rstrip().split('\t')
    three = sh[3].rstrip().split('\t')
    four = sh[4].rstrip().split('\t')
    five = sh[5].rstrip().split('\t')
    six = sh[6].rstrip().split('\t')
    seven = sh[7].rstrip().split('\t')
    eight = sh[8].rstrip().split('\t')
    nine = sh[9].rstrip().split('\t')
cifr = [zero, one, two, three, four, five, six, seven, eight, nine]
for cif in cifr:
    for shag in cif:
        shag = shag.split(',')
ind = '141700'
for s in range(6):
    turtle.penup()
    turtle.goto(s * 40, 0)
    c = int(ind[s])
    l = cifr[c][0].split(',')
    a = int(l[0])
    b = int(l[1])
    turtle.goto(s * 40 + a, 0 + b)
    turtle.pendown()
    for w in cifr[c]:
        l = w.split(',')
        a = int(l[0])
        b = int(l[1])
        turtle.goto(s * 40 + a, b)
turtle.left(230)
