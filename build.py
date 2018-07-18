#  d o c s t r i n g s
"""
!/bin/python
#
# Filename : build.py
# Script to build a language phrasesheet.
"""

#  d e p e n d e n c i e s
import os, sys


#  a t t r i b u t e s
main = "phrasesheet"
files = [ "aliases.tex", "pronunciation.tex" ]
extensions = [ "out", "aux", "log" ]


#  m a i n
# set input files
if 3>len(sys.argv):
  print "python build.py group language"

else:
  group = sys.argv[1]
  language = sys.argv[2]
  print group, language
  
  os.system( "cp %s_%s.tex %s.tex" % ( group, main, main ) )
  for f in files:
    os.system( "cp %s_%s %s" % ( language, f, f ) )

  # compile the LaTeX
  os.system( "pdflatex %s.tex" % main )
  os.system( "mv %s.pdf %s_%s.pdf" % ( main, language, main ) )
  
  # clean up
  os.system( "rm %s.tex" % main )
  for f in files:
    os.system( "rm %s" % f )

  for e in extensions:
    os.system( "rm *.%s" % e )
