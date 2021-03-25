"""
Script which can read in a text file, html file or some other file and generates a PDF file out of it.
"""
import pdfkit
# TODO:Make sure that you have wkhtmltopdf in your $PATH or set via custom configuration.


path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_url("http://google.com", "out.pdf", configuration=config)

#

