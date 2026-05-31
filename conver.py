import pandas as pd

def conver(a, b):
    """
    a = nama file
    b = data
    """
    with open(a, 'w') as file_csv:
        file_csv.write(b)


dataKamar = """
Temperature,Pressure,Altitude
30.22,995.61,147.89
30.22,995.60,147.99
30.22,995.59,148.08
30.22,995.57,148.26
30.23,995.56,148.31
30.24,995.59,148.06
30.24,995.60,148.00
30.25,995.62,147.93
30.25,995.56,148.30
30.24,995.60,148.01
"""

dataParkiran = """
Temperature,Pressure,Altitude
29.64,995.68,147.36
29.98,995.71,147.05
30.01,995.72,146.97
30.03,995.73,146.91
30.04,995.71,147.03
30.04,995.72,146.99
30.05,995.71,147.07
30.05,995.71,147.10
30.06,995.70,147.25
30.07,995.69,147.26
"""

dataLantaiDua = """
Temperature,Pressure,Altitude
30.39,995.09,679.30
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
"""


a1 = "DataKamar.csv"
a2 = "DataParkiran.csv"
a3 = "DataLantaiDua.csv"

conver(a=a1,b=dataKamar)
conver(a=a2,b=dataParkiran)
conver(a=a3,b=dataLantaiDua)
