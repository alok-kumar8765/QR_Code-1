
import pyqrcode
import pandas as pd

#Simple Code
text = "www.google.com"
image=pyqrcode.create(text)
image.svg("QRCode.svg",scale=5)

def createQRCode():


    df = pd.read_csv("Data.csv")

    for index, values in df.iterrows():

        brand = values["Brand"]
        name = values["Name"]
        category = values["Category"]
        barcode = values["Barcode"]

        data = f'''

        Name: {name} \n
        Barcode: {barcode} \n
        Category: {category} \n
        Brand: {brand}
        '''
        image = pyqrcode.create(data)
        image.svg(f"{name}_{barcode}.svg", scale="5")
        print(data)



createQRCode()
