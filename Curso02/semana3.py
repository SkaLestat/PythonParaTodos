#xfile = open("d:\RubenT\Tutoriales\PythonParaTodos\Code\Curso02\mbox.txt")
xfile = open("mbox.txt")#Se debe ejecutar desde consola para que encuentre la ruta relativa del archivo
count = 0
for sequence in xfile :
    # print(sequence)
    count += 1
print("Line Count:", count)

shortFile = open("mbox-short.txt")
print(shortFile)
inp = shortFile.read()#al usar read la variable shortfile no se deja acceder por el for
print(shortFile)
print(len(inp))
print(inp[: 20])
# shortFile.close() sirve para volver a acceder al archivo

shortFile2 = open("mbox-short.txt")
for line in shortFile2 :
    line = line.rstrip()
    if line.startswith("From: ") :
        print(line)#print siempre agrega nueva linea \n por eso se usa rstrip para borrar spacios o \n

shortFile3 = open("mbox-short.txt")
for line in shortFile3 :
    line = line.rstrip()
    if not "@uct.ac.za" in line :
        continue
    print(line)#print siempre agrega nueva linea \n por eso se usa rstrip para borrar spacios o \n

fileName = input("Enter the file name: ")
try :
    theFile = open(fileName)
except :
    print("File cannot be opened:", fileName)
    quit()