import csvA


def load_syns():
  with open('synonyms.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')

    syns = {}
    for row in reader:
      temp_list2 = []
      w, pos, s = row
      temp_list = s.split(';')
      for t in temp_list:
        for tt in t.split('|'):
          temp_list2.append(tt)

      syns[w] = temp_list2
    return syns


def run():
  syns = load_syns()

  q = raw_input("Type your sentence: ")

  for word in q.split(' '):
    shortest = [len(word), word]
    if word in syns:
      for sw in syns[word]:
        if shortest[0] > len(sw):
          shortest[0] = len(sw)
          shortest[1] = sw
      print(shortest[1])
    else:
      print(word)


if __name__ == "__main__":
  run()
