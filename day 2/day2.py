import re

def extract_color_count(game_config, c):
  regex = r'(\d*) '+ c
  game_config = game_config.strip()
  mtch = re.findall(regex, game_config)
  return mtch[0] if len(mtch) > 0 else 0

def is_game_config_compliant(blue,red,green):
  configuration = {
    'red':12,
    'green': 13,
    'blue': 14
  }
  print('\t\t red {}, green {}, blue {}'.format(red,green,blue))
  print('\t\t red {}, green {}, blue {}'.format(configuration['red'],configuration['green'],configuration['blue']))

  return not(configuration['red'] >= int(red) and configuration['blue'] >= int(blue) and configuration['green'] >= int(green))

def parse(puzzle):
  game_ID_total = 0
  for game in puzzle.splitlines():
    print('-------------------------------------')
    print(game)
    game_compliant = True
    #parse gameID and rest
    regex = r'Game (\d*): (.*)'
    x = re.findall(regex, game)[0]
    game_ID = x[0]
    game_settings = x[1].split(';')

    #iterate over all iterations
    for gs in game_settings:
      print('\t '+ gs)
      blue = extract_color_count(gs,'blue')
      red = extract_color_count(gs,'red')
      green = extract_color_count(gs,'green')
      
      if is_game_config_compliant(blue,red,green):
        game_compliant = False
        print('!! not compliant!!')
        break

    
    #if all iterations in one game are compliant, than add it to the ID total
    if game_compliant:
      game_ID_total += int(game_ID)
    
  return game_ID_total


def parse_pt2(puzzle):
  total_power = 0
  for game in puzzle.splitlines():
    game_power = 0
    print('-------------------------------------')
    print(game)
    #parse gameID and rest
    regex = r'Game (\d*): (.*)'
    x = re.findall(regex, game)[0]
    game_ID = x[0]
    game_settings = x[1].split(';')

    #iterate over all iterations
    blues = [1]
    reds = [1]
    greens = [1]
    for gs in game_settings:
      print('\t '+ gs)
      blue = extract_color_count(gs,'blue')
      red = extract_color_count(gs,'red')
      green = extract_color_count(gs,'green')
      if int(blue)>0:
        blues.append(int(blue)) 
      if int(green)>0:
        greens.append(int(green)) 
      if int(red)>0:
        reds.append(int(red)) 
    game_power = max(blues)*max(reds)*max(greens)
    total_power += game_power

  return total_power


#sum = parse(puzzle)
#print(sum)

sum = parse_pt2(puzzle)
print(sum)
