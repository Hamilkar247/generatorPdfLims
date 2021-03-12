# -*- coding: utf-8 -*-

from fpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)

# Save top coordinate
top = pdf.y

# Calculate x position of next cell
offset = pdf.x + 40

pdf.multi_cell(40,10,'Höółello World!,how are you today',1,0)

# Reset y coordinate
pdf.y = top

# Move to computed offset
pdf.x = offset 

pdf.multi_cell(100,10,'This cell needs to beside the other',1,0)

pdf.output('ahjo.pdf','F')

