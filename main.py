import os


import sys
sys.path.append(r"C:\Users\bbogd\AppData\Local\Programs\Python\Python39\Lib\site-packages")
sys.path.append(r"C:\Users\bbogd\AppData\Local\Programs\Python\Python39\Lib")
sys.path.append(r"C:\Users\bbogd\AppData\Local\Programs\Python\Python39\Lib\npath.py")
from selenium import webdriver

from photoshop import Session

import examples._psd_files as psd  # Import from examples.

PSD_FILE = psd.get_psd_files()


def hide_all_layers(layers):
    for layer in layers:
        layer.visible = False


def main():
    psd_file = PSD_FILE["export_layers_as_png.psd"]
    with Session(psd_file, action="open") as ps:
        doc = ps.active_document
        options = ps.PDFSaveOptions()
        layers = doc.artLayers

        count = 1

        for layer in layers:
            hide_all_layers(layers)
            layer.visible = True
            layer_path = os.path.join(doc.path)
            print(layer_path)

            layer.name = str(count)
            count += 1
            print(layer.name)

            if not os.path.exists(layer_path):
                os.makedirs(layer_path)
            image_path = os.path.join(layer_path, f"{layer.name}.pdf")
            doc.saveAs(image_path, options, True)
        ps.alert("Task done!")
        ps.echo(doc.activeLayer)

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
    main()