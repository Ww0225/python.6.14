class Phone:
    IMEI = None
    producer = "WW"

    def call_by_4g(self):
        print("4g")

class Phone2022(Phone):
    face_id = "1001"

    def call_by_5g(self):
        print("5g")

phone = Phone2022()
phone.IMEI
phone.call_by_5g()
phone.call_by_4g()
phone.producer


