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

    # Remove height tag
    pat = r"<svg(.*?) height=\"(.+?)\""
    rep = r"<svg\1"
    O = re.sub(pat, rep, I)

    # Remove width tag
    pat = r"<svg(.*?) width=\"(.+?)\""
    rep = r"<svg\1"
    O = re.sub(pat, rep, O)

    # Overwrite input file
    with open(fname, "w") as f:
        f.write(O)
