# #############################################################################
#
# Converts LaTeX-styled equations to MathJax-styled equations in Markdown.
#
# USAGE
#
#   python svg-removesize.py [-h] <FileNames>
#
# ARGS
#   FileNames - file names of svg files from which to remove size (accepts wildcards)
#
# Aug 2018
# Brendan Hasz
# winsto99@gmail.com
# brendanhasz.github.io
# #############################################################################

import argparse
import re
import glob

# Command line arguments
p = argparse.ArgumentParser(description='Remove height and width tages from svg file(s)')
p.add_argument("FileNames", help="Filename(s) of the input svg file(s) (accepts wildcards)")
args = p.parse_args()

# Convert each matching file
for fname in glob.glob(args.FileNames):

    # Load file
    with open(fname, "r") as f:
        I = f.read()

    # Remove height and width tags
    # TODO
    #ml = r'50' #max length (in chars) for inlines
    #O = re.sub(r'((?<!\$)(\$)([^\$]{1,'+ml+'}?)(\$)(?!\$))', r'\\\\( \3 \\\\)', I)

    # Overwrite input file
    with open(fname, "w") as f:
        f.write(O)

    #<svg height="291pt" version="1.1" viewBox="0 0 380 291" width="380pt" 
    #xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
