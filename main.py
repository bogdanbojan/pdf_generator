import os


import sys
sys.path.append(r"C:\Users\bbogd\AppData\Local\Programs\Python\Python39\Lib\site-packages") #??
sys.path.append(r"C:\Users\bbogd\AppData\Local\Programs\Python\Python39\Lib")
sys.path.append(r"C:\Users\bbogd\AppData\Local\Programs\Python\Python39\Lib\npath.py")
from selenium import webdriver

from photoshop import Session

import examples._psd_files as psd  # Import from examples.

PSD_FILE = psd.get_psd_files()




class Export:

    def hide_all_layers(self,layers):
        for layer in layers:
            layer.visible = False

    def export_pdf(self):
        image_path = os.path.join(self.layer_path, f"{self.layer.name}.pdf")
        self.doc.saveAs(image_path, self.options, True)

    def setup_layers_for_export(self):
        for self.layer in self.layers: #??
            self.hide_all_layers(self.layers)
            self.layer.visible = True
            self.layer_path = os.path.join(self.doc.path)
            print(self.layer_path)

            self.layer.name = str(self.count)
            self.count += 1  # ??
            print(self.layer.name)

            if not os.path.exists(self.layer_path):
                os.makedirs(self.layer_path)

    def setup_session(self):
        psd_file = PSD_FILE["export_layers_as_png.psd"]
        with Session(psd_file, action="open") as ps:
            self.doc = ps.active_document
            self.options = ps.PDFSaveOptions()
            self.layers = self.doc.artLayers
            self.count = 1

            self.setup_layers_for_export()
            self.export_pdf()

            ps.alert("Task done!")
            ps.echo(self.doc.activeLayer)

#
# def export_layers_in_ascending_order():
#     psd_file = PSD_FILE["export_layers_as_png.psd"]
#     with Session(psd_file, action="open") as ps:
#         doc = ps.active_document
#         options = ps.PDFSaveOptions()
#         layers = doc.artLayers
#         count = 1
#
#         for layer in layers:
#             hide_all_layers(layers)
#             layer.visible = True
#             layer_path = os.path.join(doc.path)
#             print(layer_path)
#
#             layer.name = str(count)
#             count += 1
#             print(layer.name)
#
#             if not os.path.exists(layer_path):
#                 os.makedirs(layer_path)
#
#             image_path = os.path.join(layer_path, f"{layer.name}.pdf")
#             doc.saveAs(image_path, options, True)
#

    driver = webdriver.Chrome(
        executable_path=r'C:\Program Files\Adobe\Adobe Photoshop 2020\Presets\Scripts\photoshop_python_integration\python\Lib\site-packages\multi_script_editor\examples\files\chromedriver.exe')
    driver.get("https://www.ilovepdf.com/merge_pdf")

    button = driver.find_element_by_css_selector("input[type=file]")

    for image in range(1, len(layers) + 1):
        button.send_keys(
            r"C:\Program Files\Adobe\Adobe Photoshop 2020\Presets\Scripts\photoshop_python_integration\python\Lib\site-packages\examples\files\%s.pdf" % (
                image))

    # button.click()
    convert_button = driver.find_element_by_xpath('//*[@id="processTask"]')
    convert_button.click()


if __name__ == "__main__":
    export_layers_in_ascending_order()