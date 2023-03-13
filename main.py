# Case-study #1
# Developers:   Kuznetsov N. (60%),
#               Shishko S. (40%)

from turtle import *

def star(x, y, a):
    '''
    function drawing star
    :param x: left corner coord x
    :param y: left corner coord y
    :param a: size of side
    :return: None
    '''
    pensize(2)
    color('yellow')
    speed(100)
    up()
    setpos(x, y)
    down()
    begin_fill()
    for i in range(5):
        fd(a)
        rt(144)
    end_fill()


def circ(x, y, r, c):
    '''
    function drawing circle
    :param x: center coord x
    :param y: center coord y
    :param r: radius
    :param c: color
    :return: None
    '''
    pensize(10)
    color(c)
    speed(100)
    up()
    setpos(x, y-r)
    down()
    begin_fill()
    circle(r)
    end_fill()

def triangle(x, y, l, h, c):
    '''
    function drawing triangle
    :param x: top coord x
    :param y: top coord y
    :param l: length of 1 side
    :param h: length of 2 side
    :param c: color
    :return: None
    '''
    pensize(2)
    color(c)
    speed(100)
    up()
    setpos(x, y)
    down()
    begin_fill()
    fd(l)
    rt(90)
    fd(h)
    goto(x,y)
    end_fill()

def rectangle(x, y, a, b, c):
    '''
    function drawing rectangle
    :param x: left top corner coord x
    :param y: left top corner coord y
    :param a: length
    :param b: height
    :param c: color
    :return: None
    '''
    pensize(2)
    color(c)
    speed(100)
    up()
    setpos(x, y)
    down()
    begin_fill()
    for i in range(2):
        fd(a)
        rt(90)
        fd(b)
        rt(90)
    end_fill()

def fire(x, y):
    '''
    function drawing fire
    :param x: x coord
    :param y: y coord
    :return: None
    '''
    pensize(10)
    color('red', 'orange')
    speed(100)
    up()
    setpos(x, y)
    down()
    begin_fill()
    for i in range(18):
        fd(2)
        lt(5)
    fd(30)
    lt(135)
    fd(17)
    rt(90)
    fd(17)
    lt(90)
    fd(17)
    rt(90)
    fd(17)
    lt(135)
    fd(28)
    for i in range(18):
        fd(2)
        lt(5)
    end_fill()

def main():
    '''
    Main function.
    :return: None
    '''
    bgcolor('#000030')

    star(-234,43,15)
    star(15,-200,11)
    star(-67,187,10)
    star(110,-110,8)
    star(203,106,13)
    star(-6,217,20)
    star(198,-76,18)
    star(-145,-89,16)

    seth(180)
    triangle(30, 40, 80, 30, '#AAAAAA')
    seth(0)
    rectangle(-100,50,200,100,'white')
    seth(-45)
    triangle(100,50,70,70,'white')
    seth(-45)
    triangle(-110, 60, 35, 35, 'white')
    seth(-45)
    triangle(-110, -10, 35, 35, 'white')
    seth(90)
    fire(-120,35)
    fire(-120,-35)
    seth(0)
    circ(60,0,10,'black')
    circ(15,0,10,'black')
    circ(-30,0,10,'black')
    seth(90)
    triangle(-50,-70,30,80,'#AAAAAA')
    up()
    setpos(150,0)
    down()
    dot(10,'#AAAAAA')
    up()
    seth(0)
    circ(-300,-330,200,'#8B4513')
    circ(-285, -230, 20, '#80221D')
    circ(-180, -250, 15, '#852A2A')
    circ(-220, -190, 20, '#800000')
    circ(125,200,35, '#5F9EA0')
    circ(145,210,5, '#4682B4')

    done()


main()