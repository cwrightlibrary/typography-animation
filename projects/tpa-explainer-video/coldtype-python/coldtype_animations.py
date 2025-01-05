from coldtype import *


@animation((1920, 1080), timeline=50, bg=hsl(0.6))
def wave(f):
    return (Glyphwise("Third Party Administrators", lambda g:
        Style(Font.Find("Hubot"), 150,
              wdth=f.adj(-g.i*3).e("seio", 1),
              wght=f.adj(-g.i*3).e("seio", 1)))
        .align(f.a.r)
        .f(1))