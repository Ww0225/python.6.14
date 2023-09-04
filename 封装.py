class Phone:
    __current_voltage = None

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1 :
            print("5g通话开启")
        else:
            self.__keep_single_core()

phone = Phone()
phone.call_by_5g()
