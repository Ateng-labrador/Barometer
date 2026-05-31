import pandas as pd

def conver(a, b):
    """
    a = nama file
    b = data
    """
    with open(a, 'w') as file_csv:
        file_csv.write(b)


DataPercobaan1Naik = """
Temperature,Pressure,Altitude
31.08,995.89,145.57
31.42,995.95,145.05
31.44,995.96,144.93
31.46,995.96,144.94
31.46,995.90,145.43
31.47,995.88,145.59
31.47,995.84,146.00
31.47,995.82,146.13
31.47,995.79,146.38
31.48,995.78,146.48
31.48,995.76,146.64
"""

DataPercobaan2Naik = """
Temperature,Pressure,Altitude
31.52,995.98,144.79
31.53,996.03,144.38
31.53,996.00,144.64
31.52,995.95,145.03
31.52,995.92,145.26
31.52,995.88,145.59
31.52,995.85,145.88
31.53,995.84,145.97
31.53,995.82,146.16
31.54,995.76,146.62
"""


DataPercobaan3Naik = """
Temperature,Pressure,Altitude
31.20,995.93,145.25
31.54,995.97,144.84
31.56,995.92,145.29
31.58,995.88,145.62
31.58,995.88,145.64
31.58,995.85,145.90
31.59,995.84,145.97
24.56,760.13,2359.66
24.56,760.13,2359.66
24.56,760.13,2359.66
"""

DataPercobaan1Turun = """
Temperature,Pressure,Altitude
31.08,995.55,148.39
31.43,995.62,147.86
31.45,995.62,147.80
31.46,995.64,147.65
31.46,995.67,147.37
31.45,995.73,146.87
31.44,995.75,146.75
31.43,995.79,146.38
31.43,995.76,146.63
31.42,995.79,146.43
"""

DataPercobaan2Turun = """
Temperature,Pressure,Altitude
31.56,995.61,147.91
31.56,995.56,148.32
31.56,995.64,147.63
31.55,995.66,147.48
31.55,995.66,147.52
31.55,995.70,147.19
31.55,995.79,146.37
31.55,995.80,146.33
31.52,995.78,146.47
31.54,995.79,146.35
"""

DataPercobaan3Turun = """
Temperature,Pressure,Altitude
31.42,995.58,148.17
31.44,995.60,147.96
31.43,995.66,147.52
31.43,995.64,147.66
31.44,995.67,147.41
31.44,995.71,147.08
31.43,995.72,147.01
31.40,995.77,146.53
31.40,995.76,146.65
31.41,995.75,146.75
"""




a1 = "DataPercobaan1naik.csv"
a2 = "DataPercobaan2naik.csv"
a3 = "DataPercobaan3naik.csv"

a4 = "DataPercobaan1turun.csv"
a5 = "DataPercobaan2turun.csv"
a6 = "DataPercobaan3turun.csv"

conver(a=a1,b=DataPercobaan1Naik)
conver(a=a2,b=DataPercobaan2Naik)
conver(a=a3,b=DataPercobaan3Naik)

conver(a=a4,b=DataPercobaan1Turun)
conver(a=a5,b=DataPercobaan2Turun)
conver(a=a6,b=DataPercobaan3Turun)
