class StudentsScore:
  def __init__(self , hakbunlist , namelist , korlist , englist , mathlist):
    self.hakbunlist = hakbunlist
    self.namelist = namelist
    self.korlist = korlist
    self.englist = englist
    self.mathlist = mathlist
  
  def calList(self, korlist, englist , mathlist):
    self.totlist = []
    self.avglist = []
    self.haksjumlist = []
    total = 0
    avg = 0.0

    for i in range(len(korlist)):
      total = korlist[i] + englist[i] + mathlist[i]
      avg = total / 3.0
      self.totlist.append(total)
      self.avglist.append(avg)

      if avg >= 90:
        grade = 'A'
      elif avg >= 80:
        grade = 'B'
      elif avg >= 70:
        grade = 'C'
      elif avg >= 60:
        grade = 'D'
      else:
        grade = 'F'
      self.haksjumlist.append(grade)
      
  
  def printScore(self):
    print("=" * 70)
    print(" 번호\t\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
    print("=" * 70)
    for i in range(len(self.hakbunlist)):
      print("%10s%8s%8d%8d%8d%8d\t%.2f%7s"%(self.hakbunlist[i], self.namelist[i] , self.korlist[i] , self.englist[i] , self.mathlist[i] , self.totlist[i] , self.avglist[i] , self.haksjumlist[i]))


def readList():
  hakbunlist = []
  namelist = []
  korlist = []
  englist = []
  mathlist = []

  flag = True
  print("프로그램을 종료하려면 학번에 '0'을 입력하시오")
  while flag:
    hakbun = input("학번을 입력하시오: ")
    if hakbun == '0':
      flag = False
    else :
      name = input("이름을 입력하시오: ")
      kor = int(input("국어점수를 입력하시오: "))
      eng = int(input("영어점수를 입력하시오: "))
      math = int(input("수학점수를 입력하시오: "))
      
      hakbunlist.append(hakbun)
      namelist.append(name)
      korlist.append(kor)
      englist.append(eng)
      mathlist.append(math)

  return hakbunlist, namelist, korlist, englist, mathlist



def main():
  hakbunlist , namelist , korlist , englist , mathlist = readList()
  smart_ai = StudentsScore(hakbunlist , namelist , korlist , englist , mathlist)
  smart_ai.calList(smart_ai.korlist , smart_ai.englist , smart_ai.mathlist)
  smart_ai.printScore()
  

if __name__ == "__main__":
  main()
