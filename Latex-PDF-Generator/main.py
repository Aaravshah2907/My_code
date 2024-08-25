import matplotlib.pyplot as plt
from PIL import Image
from pdf2image import convert_from_path

def latex_to_png(latex_str : str):
    fig = plt.figure()
    
    plt.axes(None)
    plt.text(0.5,.5,f"${latex_str}$", size = 50, ha = "center", va = "center")
    
    pdf_path = "result.pdf"
    png_path = "result.png"
    
    plt.savefig(pdf_path,format="pdf", bbox_inches ="tight", pad_inches = 0.4)
    
    plt.close(fig)
    images = convert_from_path(pdf_path, poppler_path=None)
    images[0].save(png_path,"PNG")
    
    return png_path


latex_formula = r"\theta^{3} = x_1 + y_2"

png_path = latex_to_png(latex_formula)
image = Image.open(png_path)
image.show()