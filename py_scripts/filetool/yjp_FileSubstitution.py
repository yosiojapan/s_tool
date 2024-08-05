# -*- coding: utf-8 -*-
import codecs
import string
import re

def main(infile, outfile, sourcetxt, newtxt):
    f_in  = codecs.open(infile, 'r','Shift_JIS')
    lines = f_in.readlines()
    lines2 = []
    for line in lines:
        line = line.replace(sourcetxt,newtxt)
        lines2.append(line)
    else:
        f_in.close()
        f_out = codecs.open(outfile, 'w', 'Shift_JIS')
        f_out.write(string.join(lines2,''))
        f_out.close()