from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        # Create a empty page
        self._pdf.add_page()
        # set the format font
        self._pdf.set_font("helvetica", "B", 50)
        # Create the text on top the shirt
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
        # open the image
        self._pdf.image("shirtificate.png", w = self._pdf.epw)
        # set the font size
        self._pdf.set_font_size(30)
        # set the text color in red
        self._pdf.set_text_color(255, 0, 0)
        # print the text in pdf
        self._pdf.text(x = 47.5, y = 140, text = f"{name} took CS50")

    def upload(self, name):
        # Upload the new image in pdf
        self._pdf.output(name)

def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.upload("shirtificate.pdf")

if __name__ == "__main__" :
    main()
