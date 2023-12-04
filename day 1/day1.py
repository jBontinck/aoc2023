
import re

def calc_total(inputstr):
  total1 = 0
  total2 = 0
  for line in inputstr.splitlines():

    #approach 1
    regex = r'\d'
    x1 = re.findall(regex, preprocess(line))
    z1 = int(x1[0])*10+int(x1[-1])

    #approach 2
    r = r'1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'
    x2 = [*map({n: str(i%9+1) for i, n in enumerate(r.split('|'))}.get,
    re.findall(rf'(?=({r}))', line))]

    z2 = int(x2[0])*10+int(x2[-1])
    total1 += z1
    total2 += z2

    if(len(x1)!= len(x2)):
      print(line +'  ' + str(x1) + '  ' + str(x2))
  return total2

def preprocess(inputstr):
  x = inputstr
  x = x.replace("three", "3")
  x = x.replace("four", "4")
  x = x.replace("six", "6")
  x = x.replace("seven", "7")
  x = x.replace("nine", "9")
  x = x.replace("five", "5")
  x = x.replace("eight", "8")
  x = x.replace("one", "1")
  x = x.replace("two", "2")
  



  return x

total = calc_total(foo)
print(total)
