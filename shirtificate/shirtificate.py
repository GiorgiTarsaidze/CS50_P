from fpdf import FPDF

# Creating 'PDF' class with super class of original FPDF imported
class PDF(FPDF):
    # In name function, we return our user's input
    def name(self):
        return input("Name: ")
    # In shirt functio, using library's functions, we align render the image
    def shirt(self):
        self.add_page()
        self.set_font("helvetica","",55)
        # Here, we set cursor and apply our header text, aligning margins and centering it
        self.cell(0,60,"CS50 Shirtificate",0,new_x="LMARGIN",new_y="NEXT",align="C")
        # Passing pdf.epw to the width parameter of the image below to scale it horizontally to a full page width
        self.image("shirtificate.png",w=pdf.epw)
        # Getting ready another font for our text on the shirt
        self.set_font("helvetica","B",25)
        # Setting color to white
        self.set_text_color(255,255,255)
        self.text(x=49, y = 135, txt=self.name() + " took CS50")

        # Output as a pdf file
        self.output("shirtificate.pdf")

pdf = PDF()
pdf.shirt()
# This code works perfectly for the "Giorgi Tarsaidze" input