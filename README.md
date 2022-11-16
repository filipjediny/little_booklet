# little_booklet
*disclaimer: Only works for single-sided printing and reinsertion, sequence does not work for double-sided printing.*

generate_booklet changes the page order of the input pdf so that double-sided A6 booklets can be printed on A4 paper. 
If you only need the page order, you can use generate_sequence.

Example:
normal 4 pages per sheet pdf - 1 2 3 4, 5 6 7 8

4 pages per sheet after reordering - 4 5 2 7, 6 3 8 1

*The program lists the back pages after all the front pages, which means you should print the first ceil(P/8) pages, flip the entire stack over the main axis, load it into the tray, and then print the rest.*

The generate_booklet uses the PyPDF2 library, which is located in the lib folder.
If you are using your own globally installed PyPDF2 library, be sure to change it.
import in generate_booklet from (from lib.PyPDF2 import PdfFileWriter, from lib.PyPDF2 import PdfFileReader) to (from PyPDF2 import PdfFileWriter, PdfFileReader).
