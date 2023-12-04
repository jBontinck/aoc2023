import re
def has_special_char(text: str) -> bool:
  text = text if len(text)>0 else ""
  text ="".join([str(i) for i in text])
  print('\t checking '+ text)
  
  special_char = False
  for letter in text:
    if (not letter.isnumeric() and not letter.isdigit() and not letter =="."):
        special_char = True
        break
  return special_char

def parse_3(raw_input):
  total_sum = 0
  content = [list(x) for x in  raw_input.splitlines()]
  for r in range(len(content)):
    startindex = -1
    endindex = -1
    substr = ""
    print('scanning row '+ str(r) + '------------------------------------------')
    for c in range(len(content[r])):
      if c<endindex:
        continue
      else:
        if(content[r][c].isdigit()):
          startindex = c
          i = 1
          substr = "".join([str(i) for i in content[r][c:c+i]])
          while (substr.isdigit() and c+i-1<len(content[r])):
            i+=1
            substr = "".join([str(letter) for letter in content[r][c:c+i]])
          i-=1
          endindex = c+i
          substr = "".join([str(letter) for letter in content[r][c:c+i]])
      
          print('found: ' + substr)

          has_token = False
          print(endindex)
          has_token = has_token or has_special_char(content[r][startindex-1])
          if(endindex == len(content[0])):
            endindex-=1
          has_token = has_token or has_special_char(content[r][endindex])
          endindex+=1

          if(r>0):
            has_token = has_token or has_special_char(content[r-1][startindex-1:endindex+1]) #check previous row
          if(r<len(content)-1):
            has_token = has_token or has_special_char(content[r+1][startindex-1:endindex+1])
            
          if(has_token):
            print('add to sum' + substr)
            total_sum += int(substr)
          else:
            print('rejected: ' + substr)



            

  return total_sum

result = parse_3(input_3)
print(result)


#too high : 536066