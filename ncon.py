import string

filestructure = ["Timespan", "\t", "content", "\n"]

with open("captions.sbv", "r") as f:
  toread = f.read()
  alter1 = toread.replace(",","-")
  alter2 = alter1.replace("Â\xa0\n", " ")
  alter3 = alter2.replace("\n", "$")
  alter4 = alter3.replace("$$", "\n")
  alter5 = alter4.replace("$","\t")

  #finaltext.append(alter)
  print(alter5)

  with open("captions_for_Nvivo.txt", "w") as l:
    for structure in filestructure:
      l.write(structure)
    for final in alter5:
      l.write(final)
