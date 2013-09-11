import sys
import os
import cStringIO

import utils

WIDE_CELL = 3

WIDTH = int(os.environ['WIDTH'])
HEIGHT = int(os.environ['HEIGHT'])
HTML = "<html><head><style>{css}</style></head>\n"\
       "<body>\n<div class='content'>\n{divs}</div>\n</body></html>"
COLORS = ['red', 'rgba(0, 0, 255, 0.8)', 'green', 'rgba(0, 0, 0, 0)']

DURATION = 15

def render(fname, pixel_w, pixel_h, animate=False):
    for cell in open(fname):
        fields = cell.split()
        key = fields[0]
        x, y, is_wide, color = map(int, fields[1:])
        width = pixel_w * WIDE_CELL if is_wide else pixel_w
        div ="<div id='%s'></div>\n" % key
        animation = "-webkit-animation-name: anim-{key}; "\
                    "-webkit-animation-duration: {duration}s; "\
                    "-webkit-animation-timing-function: ease-out; "\
                    "-webkit-animation-iteration-count: 1; "\
                    "-webkit-animation-fill-mode: forwards; "
                    #"-webkit-animation-direction: alternate; "
        css = ("{{ " + (animation if animate else '') +\
               "border: 1px solid #ccc; "
               "position: absolute; "
               "top: {top}; "
               "left: {left}; "
               "width: {width}; "
               "height: {height}; "
               "background: {color}; "
               "}}\n").format(key=key,
                              duration=DURATION,
                              top=y * pixel_h,
                              left=x * WIDE_CELL * pixel_w,
                              width=width,
                              height=pixel_h,
                              color=COLORS[color])
        yield key, div, css

def dimensions():
    max_x = 0
    max_y = 0
    for cell in utils.cells():
        max_x = max(max_x, cell.x)
        max_y = max(max_y, cell.y)
    return max_x * WIDE_CELL, max_y

def content(src_file, dst_file=None):
    total_width, total_height = dimensions()
    pixel_w = WIDTH / (total_width + 1)
    pixel_h = HEIGHT / (total_height + 1)

    css_buf = cStringIO.StringIO()
    div_buf = cStringIO.StringIO()

    css_buf.write('.content { width: %d; height: %d }' % (WIDTH, HEIGHT))

    for key, div, css in render(src_file, pixel_w, pixel_h, bool(dst_file)):
        css_buf.write("#%s %s" % (key, css))
        div_buf.write(div)

    if dst_file:
        for key, div, css in render(dst_file, pixel_w, pixel_h, False):
            css_buf.write("@-webkit-keyframes anim-{key} "
                          "{{ 100% {css} }}\n".format(key=key, css=css))

    return HTML.format(divs=div_buf.getvalue(), css=css_buf.getvalue())

if __name__ == '__main__':
    print content(*sys.argv[1:])



