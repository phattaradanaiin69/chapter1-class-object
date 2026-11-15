class Member:
    def __init__(self, name , visit ,months):
        self.name = name
        self.visit = visit
        self.months = months

    def is_at_risk(self):
        return self.visit < 4 and self.months > 6

m1 = Member("joe", 2 , 10)

print("ชื่อสามชิก :", m1.name)
print("เสี่ยงเลิกใช้บริการ :", m1.is_at_risk())