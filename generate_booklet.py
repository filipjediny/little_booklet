import math
from lib.PyPDF2 import PdfFileWriter
from lib.PyPDF2 import PdfFileReader

output_pdf = PdfFileWriter()

with open(input("filename: "), "rb") as readfile:
    input_pdf = PdfFileReader(readfile)
    pg = len(input_pdf.pages)
    sh = math.ceil(pg/8)
    mid = math.floor(pg/2)
    seq = []
    for fp_sh in range(sh):
        seq.append(mid-4*fp_sh)
        seq.append(mid+1+4*fp_sh)
        seq.append(mid-2-4*fp_sh)
        seq.append(mid+3+4*fp_sh)
    for bp_sh in range(sh):
        seq.append(mid+2+4*bp_sh)
        seq.append(mid-1-4*bp_sh)
        seq.append(mid+4+4*bp_sh)
        seq.append(mid-3-4*bp_sh)
    filtered_seq = [0 if x not in range(pg+1) else x for x in seq]
    for i in filtered_seq:
        if i!=0:
            output_pdf.addPage(input_pdf.pages[i-1])
        else:
            output_pdf.add_blank_page()
    with open("output.pdf", "wb") as writefile:
        output_pdf.write(writefile)
