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

def change_fonts():
    pdf = FPDF()
    pdf.add_page()
    font_size = 8
    for font in pdf.core_fonts:
        if any([letter for letter in font if letter.isupper()]):
            # skip this font
            continue
        pdf.set_font(font, size=font_size)
        txt = "Font name: {} - {} pts".format(font, font_size)
        pdf.cell(0, 10, txt=txt, ln=1, align="C")
        font_size += 2
    pdf.output("change_fonts.pdf")

def add_image(image_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, x=10, y=8, w=100)
    pdf.set_font("Arial", size=12)
    pdf.ln(85)
    pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
    pdf.output("add_image.pdf")

def multipage_simple():
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()
    line_no = 1
    for i in range(100):
        pdf.cell(0, 10, txt="Line #{}".format(line_no), ln=1)
        line_no += 1
    pdf.output("multipage_simple.pdf")

class CustomPDF(FPDF):

    def header(self):
        #Set up a logo
        self.image("rac.png", 10, 8, 33)
        self.set_font('Arial', "B", 15)

        #Add an address
        self.cell(100)
        self.cell(0, 5, "Mike Driscoll", ln=1)
        self.cell(100)
        self.cell(0, 5, "123 American Way", ln=1)
        self.cell(100)
        self.cell(0, 5, "Any Town, USA", ln=1)

        #Line break
        self.ln(20)

    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', 'I', 8)

        #Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

def footandheader(pdf_path):
    pdf = CustomPDF()
    #Create the special value {nb}
    #pdf.alias_nb_pages() - nie wiem dlaczego wywala mi tutaj
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    line_no = 1
    for i in range(50):
        pdf.cell(0, 10, txt="Line #{}".format(line_no), ln=1)
        line_no += 1
    pdf.output(pdf_path)

def main():
    args=def_params()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
    pdf.output("simple_demo.pdf")
    change_fonts()
    add_image("rac.png")
    multipage_simple()
    footandheader('header_footer.pdf')

if __name__ == "__main__":
    main()
