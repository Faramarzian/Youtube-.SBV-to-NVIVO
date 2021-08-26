import string
# so what ever structure you have for you rows you can add here
filestructure = ["Timespan", "\t", "content", "\n"]

#here we open the sbv file we downloaded usually in the same folder
with open("/content/captions.sbv", "r") as f:
  toread = f.read()
  # so this first alter is where we fix the time span structure so Nvivo can understand using a "-"
  alter1 = toread.replace(",","-")
  # here we are just joing the line seperation in the captions that youtube puts in google colab i had to remove the "Â" 
  # for it to work so you might have to change this depending where your running this script
  alter2 = alter1.replace("\xa0\n", " ")
  # so we are just altering and loading the previous alteration to alter it furthur. here i replace the line breaks with dollar sign
  #cause for every entry there is a double linebreak and im a noob and don't know how to fix it so i am altering a the problem to a problem i can fix. you'll see
  alter3 = alter2.replace("\n", "$")
  # so here every double dollar sign because a line break and all that is left is the single dollar signs so Nvivo thinks its a new row
  alter4 = alter3.replace("$$", "\n")
  # and now all the single dollar signs are turned into a tab so w that nvivo knows when columns change
  alter5 = alter4.replace("$","\t")

  # so i just print it so i can see if it works or not
  print(alter5)

  # here i write it to a text file by adding the first row as like labels for Nviov to know what the colums in the rows are
  with open("/content/captions_for_Nvivo.txt", "w") as l:
    for structure in filestructure:
      l.write(structure)
    for final in alter5:
      l.write(final)
  
  # IMPORTANT so i don't know how to delete the last tab (\t) but this script will produce a tab at the end that you can manually remove way at the end 
  # so remember before importing to Nvivo REMOVE THE LAST EMPTY SPACE which is just a tab press or "\t"
