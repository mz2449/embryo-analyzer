import averager
import normalizer
'''import normalizer2'''
import csvMaker
import csvOpener
import pixel_to_embryolength
import percentify
import time
import sys

print(
    '''\n\n\nCopyright (c) 2019 Michael Zheng MICHAEL.ZHENG@NYU.EDU
\nPermission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

\nThe above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
)

print('\nVersion 0.1.2\n')

print('\nPlease read README.txt before continuing\n')

while True:
    fileDict = dict()
    numFiles = ''
    fileNorm = ''
    meanLabel = ''
    answerL = ''
    answerN = ''
    answerP = ''
    answerS = ''
    key1 = 1
    p = 'n'

    opener = lambda x: csvOpener.csvOpener(x)
    changer = lambda x: pixel_to_embryolength.changeFirstElement(x)
    normer = lambda x, y, z: normalizer.normalize(x, y, z) #Divide by mean
    """normer = lambda x, y, z: normalizer2.normalize(x, y, z) #Divide by 255/mean"""
    percentifier = lambda x: percentify.percentify(x)


    while True:
        try:
            while True:
                p = input("\nEnter Path to File " + str(key1) + " ('n' when done):")
                fileDict[key1] = opener(p) #this turns every file into a value in a dictionary, the key is the file number
                print("File", key1, " found") #the value is a list of every line in the file, which are lists (a list of lists)
                key1 += 1
                continue
        except:
            if p != 'n':
                print("\nFile not found, recheck name or path")
        finally:
            if p == 'n':
                print("All Files Selected")
                break

    while True:
        answerN = input("\nWould you like to normalize your file? (y/n)")
        if answerN in ('y', 'n'):
            break
        else:
            print('\nPlease enter either y (yes) or n (no)')
            continue

    if answerN == "y":
        while True:
            fileNorm = input("\nName or Path to File to Normalize to?")
            try:
                fileNorm = opener(fileNorm) #fileNorm is a list of every line in the file (also a list) (a list of lists)
                break
            except:
                print("\nFile not found, recheck name or path")
                continue


        while True:
            try:
                meanLabel = int(input("\nNormalizing Number Column Number:"))
                break
            except:
                print('\nPlease enter a number')
                continue
        meanLabel -= 1

    while True:
        answerP = input("\nWould you like to percentify your file? (y/n)")
        if answerP in ('y', 'n'):
            break
        else:
            print('\nPlease enter either y (yes) or n (no)')
            continue
    '''while True:
        answerS = input("\nAdd Standard Deviation Column? (y/n)")
        if answerP in ('y', 'n'):
            break
        else:
            print('\nPlease enter either y (yes) or n (no)')
            continue'''

    startTime = time.process_time()

    for key, value in fileDict.items():
        fileDict[key] = changer(fileDict[key]) #change the first value of every file to match the 100-0% A-P length
        if answerN == "y":
            fileNorm = normalizer.removeFirstElement(fileNorm)
            normer(fileDict[key], fileNorm[key - 1], meanLabel)
        if answerP == "y":
            fileDict[key] = percentifier(fileDict[key])

    csvAll = averager.compiler(list(fileDict.values()))
    averager.averager(csvAll)
    csvAll = averager.deDictionaryer(csvAll)
    csvAll = averager.sorter(csvAll)

    stopTime = time.process_time()

    print('\nFinished in', round((stopTime - startTime), 5), 'seconds!')

    path = input("\nPath to new .csv file?")
    newName = input("New .csv file name?")

    if len(fileDict) == 0:
        print("\nIf you didn't want to do anything, why did you run me?")
        sys.exit()

    try:
        if newName[-1] == "/":
            csvMaker.makeNewCsv(path + newName, csvAll)
            print("\nFile", newName, "created at", path)
        else:
            csvMaker.makeNewCsv(path + "/" + newName, csvAll)
            print("\nFile", newName, "created at", path)
    except:
        print("\nPath not found")
        sys.exit()

    while True:
        answerL = input('\nDo you have more to analyze (y/n): ')
        if answerL in ('y', 'n'):
            break
        else:
            print('\nPlease enter either y (yes) or n (no)')
            continue
    if answerL == 'y':
        continue
    else:
        print('\nGoodbye')
        break

sys.exit()