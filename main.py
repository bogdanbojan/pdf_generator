import os
from selenium import webdriver
from photoshop import Session
import examples._psd_files as psd
from config import CHROME_WEBDRIVER, PDF_FILES, WEBSITE_PDF_CONVERTER

PSD_FILE = psd.get_psd_files()


class PdfConverter:
    def setup_files_for_web_upload(self):
        psd_file = PSD_FILE["export_layers_as_png.psd"]
        with Session(psd_file, action="open") as ps:
            self.doc = ps.active_document
            self.options = ps.PDFSaveOptions()
            self.layers = self.doc.artLayers
            self.count = 1

            self.export_layers()

            ps.alert("Task done!")
            ps.echo(self.doc.activeLayer)

    def export_layers(self):
        for self.layer in self.layers:
            self.hide_all_layers(self.layers)

            self.layer.visible = True
            self.layer_path = os.path.join(self.doc.path)
            print(self.layer_path)

            self.layer.name = str(self.count)
            self.count += 1
            print(self.layer.name)

            self.export_pdf(self.layer)

            if not os.path.exists(self.layer_path):
                os.makedirs(self.layer_path)

    def hide_all_layers(self,layers):
        for layer in layers:
            layer.visible = False

    def export_pdf(self,layer):
        image_path = os.path.join(self.layer_path, f"{layer.name}.pdf")
        self.doc.saveAs(image_path, self.options, True)




    def download_converted_pdf_from_website(self):
        self.driver = webdriver.Chrome(
            executable_path=CHROME_WEBDRIVER)
        self.driver.get(WEBSITE_PDF_CONVERTER)
        self.button = self.driver.find_element_by_css_selector("input[type=file]")

        self.upload_pdf_files_to_website()

        convert_button = self.driver.find_element_by_xpath('//*[@id="processTask"]')
        convert_button.click()

    def upload_pdf_files_to_website(self):
        for image in range(1, len(self.layers) + 1):
            self.button.send_keys(PDF_FILES + '/%s.pdf' % (image))

if __name__ == "__main__":
    PdfConverter().setup_files_for_web_upload()