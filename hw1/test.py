import datetime

# 多态类
class AboutBook:
    def printName(self, who) -> None:
        print(who.getName())

    def printAuthor(self, who) -> None:
        print(who.getAuthor())

    def printLanguage(self, who) -> None:
        print(who.getLanguage())

    def printPrice(self, who) -> None:
        print(who.getPrice())

    def printClassDes(self, who) -> None:
        print(who.getClassDes())

    def printDetail(self, who) -> None:
        who.printDetail()


# 父类
class Book:
    # 类属性
    __name = "book"
    __author = "John Doe"
    __language = "English"
    __price = 0.0
    __id = 0

    # 对象方法
    def __init__(self, name, author, language, price) -> None:
        self.__name = name
        self.__author = author
        self.__language = language
        self.__price = price
        self.__setId()

    def getId(self) -> int:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def getAuthor(self) -> str:
        return self.__author

    def getLanguage(self) -> str:
        return self.__language

    def getPrice(self) -> str:
        return self.__price

    # 占位函数
    def printDetail(self) -> None:
        pass

    # 类方法
    @classmethod
    def __setId(cls) -> None:
        cls.__id += 1

    # 静态方法
    @staticmethod
    def getClassDes() -> str:
        return "书籍类：父类"


# 子类1，继承自父类
class Dictionary(Book):
    __secondLanguage = "None"

    def setSecondLanguage(self, secondLanguage) -> None:
        self.__secondLanguage = secondLanguage

    def getSecondLanguage(self) -> str:
        return self.__secondLanguage

    def printDetail(self) -> None:
        print("书籍类型：字典")
        print("书籍编号：", self.getId())
        print("书籍名称：", self.getName())
        print("书籍作者：", self.getAuthor())
        print("书籍语言：", self.getLanguage())
        print("书籍第二语言：", self.__secondLanguage)
        print("书籍价格:", self.getPrice())

    @staticmethod
    def getClassDes() -> str:
        return "字典类：继承自书籍父类"


# 子类2，继承自父类
class ScienceFiction(Book):
    __trend = "Classic"

    def setTrend(self, trend) -> None:
        self.__trend = trend

    def getTrend(self) -> str:
        return self.__trend

    def printDetail(self) -> None:
        print("书籍类型：科幻小说")
        print("书籍编号：", self.getId())
        print("书籍名称：", self.getName())
        print("书籍作者：", self.getAuthor())
        print("书籍语言：", self.getLanguage())
        print("书籍流派：", self.__trend)
        print("书籍价格:", self.getPrice())

    @staticmethod
    def getClassDes() -> str:
        return "科幻小说类：继承自书籍父类"


# 子类3，继承自父类
class ProfessionalReference(Book):
    __profession = "Profession"

    def setProfession(self, profession) -> None:
        self.__profession = profession

    def getProfession(self) -> str:
        return self.__profession

    def printDetail(self) -> None:
        print("书籍类型：专业参考")
        print("书籍编号：", self.getId())
        print("书籍名称：", self.getName())
        print("书籍作者：", self.getAuthor())
        print("书籍语言：", self.getLanguage())
        print("书籍专业：", self.__profession)
        print("书籍价格:", self.getPrice())

    @staticmethod
    def getClassDes() -> str:
        return "专业参考类：继承自书籍父类"


# 静态方法演示
print(Book.getClassDes())
print(Dictionary.getClassDes())
print(ScienceFiction.getClassDes())
print(ProfessionalReference.getClassDes())

print("词典书籍数量：", Dictionary.getId(Dictionary))
print("科幻小说数量：", ScienceFiction.getId(ScienceFiction))
print("专业参考数量：", ProfessionalReference.getId(ProfessionalReference))

# 对象实例化
a = Dictionary("牛津英汉大词典", "牛津", "英文", 199)
a.setSecondLanguage("中文")
print("实例化了一个字典类的对象")

b = ScienceFiction("三体II：黑暗森林", "刘慈欣", "中文", 59)
b.setTrend("硬科幻")
b.publishedDate = datetime.date(2008, 5, 1)  # 对象属性
print("实例化了一个科幻小说类的对象")

c = ProfessionalReference("Effective Python", "Brett Slatkin", "English", 79)
c.setProfession("IT, python")
print("实例化了一个专业参考类型的对象")

# 类方法效果
print("词典书籍数量：", Dictionary.getId(Dictionary))
print("科幻小说数量：", ScienceFiction.getId(ScienceFiction))
print("专业参考数量：", ProfessionalReference.getId(ProfessionalReference))

# 多态
detail = AboutBook()

detail.printClassDes(a)
detail.printDetail(a)
detail.printClassDes(b)
detail.printDetail(b)
print("出版时间：", b.publishedDate)
detail.printClassDes(c)
detail.printDetail(c)
