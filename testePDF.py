from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

cnv = canvas.Canvas('Teste.pdf', pagesize=A4)

cnv.drawString(250,450,'Macaco')


cnv.save()
