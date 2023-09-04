class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("父使用5g网络进行通话")

class MyPhone(Phone):
    producer = "ITWW"

    def call_by_5g(self):
        print("子5g")