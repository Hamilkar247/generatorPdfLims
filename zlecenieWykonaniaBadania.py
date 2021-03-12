# -*- coding: utf-8 -*-

import logging
import argparse
from fpdf import FPDF

def def_params():
    parser = argparse.ArgumentParser(
            description="Description to fill"
    )
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG, force=True)
        print("args:" + str(args))
    return args

class PDF(FPDF):

    #def __init__(self):
    #    pass

    def header(self):
        zdjecie="rac.png"
        polozenieXzdj=8
        polozenieYzdj=8
        rozmiarZdjecia=33
        # Logo (zdjecie, polozenie x, polozenie y, rozmiar)
        self.image(zdjecie, polozenieXzdj, polozenieYzdj, rozmiarZdjecia)
        # Arial bold 15
        self.set_font('Arial', 'B', 12)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    #first page
    def firstPage(self):
        x=1000
        y=40
        ############# TYTUL
        self.ln(40)
        #self.set_left_margin(3)
        self.add_font('ArialUnicode', fname='Arial-Unicode-Regular.ttf', uni=True)
        self.set_font('ArialUnicode', 'B', 29)
        self.set_text_color(0,200,0)
        #cell(x,y, "tekst", wielkosc ramki(0 brak ramkii), nie wiem)
        self.cell(x, 0, 'ZLECENIE WYKONANIA BADANIA', 0, 1)
        self.ln(20)

        ############# DANE ZLECENIODAWCY
        # Zapisane 'top' koordynat
        top = self.y

        #Obliczenie x kolejnej komorki
        offset = self.x + 80

        # Calculate x position
        #self.set_font('Arial', '', 10)
        self.set_font('ArialUnicode', 'B', 29)
        self.set_text_color(0,0,0)
        self.multi_cell(50, 15, 'Danie Zleceniodawcy\n(do faktury noty ksiegowej)\nnazwa, adres, NIP', 1, 1)

        #Resetowanie koordynatów
        self.y = top

        #Przenieś na obliczenie offset
        self.x = offset
        self.multi_cell(75, 15, 'Dane Zleceniodawcy\n(do Raportu z badań)\nnazwa, adres, NIP',1,1)

def main():
    def_params()
    # Instantiation of inherited class
    pdf = PDF()

    #pdf.set_doc_option('core_fonts_encoding', 'utf-8')
    pdf.alias_nb_pages(str(2))

    pdf.add_page()
    pdf.set_font('Times', '', 12)
    pdf.set_left_margin(32)
    pdf.set_right_margin(32)
    #pdf.set_doc_option('core_fonts_encoding', 'utf-8')
    pdf.firstPage()

#    pdf.output(dest='S').encode('latin-1','ignore')

    #pdf.set_doc_option('core_fonts_encoding', 'utf-8')
    pdf.output('zlecenie.pdf', 'F')

if __name__ == "__main__":
    main()
