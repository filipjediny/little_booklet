# little_booklet
generate_booklet reorders pages of an input pdf so that you can print two-sided A6 booklets on A4 paper. 
If you only need the page ordering, you can use generate_sequence.

generate_booklet uses PyPDF2 library which is in the lib folder.
To use your own globally-installed PyPDF2 library, don't forget to change
the imports in generate_booklet from (from lib.PyPDF2 import PdfFileWriter, from lib.PyPDF2 import PdfFileReader) to (from PyPDF2 import PdfFileWriter, PdfFileReader).
