from datetime import datetime
from datetime import date

ngay = datetime.strptime("30/12/2023", "%d/%m/%Y")
ngay_date = datetime.strptime("30/12/2023", "%d/%m/%Y").date()

formatted_string = ngay.strftime("%d/%m/%Y %H:%M:%S")