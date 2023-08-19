class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

c1 = Clock()
c1.id = 1003
c1.price = 8.88
print(f"闹钟id：{c1.id},价格:{c1.price}")
c1.ring()