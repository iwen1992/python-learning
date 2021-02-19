class Company(object):
    def __init__(self,studentlist):
        self.student = studentlist
    def __getitem__(self, item):
        return  self.student[item]
company = Company(['tom','bob','lissa'])
company1 = company[:1]
print(company1)

for studentItem in company:
    print(studentItem)

