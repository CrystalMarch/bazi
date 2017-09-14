import readDic
import characters
import metaphysic
import random

def main():
    print("main")
    wuxingCharacters = set(metaphysic.main())
    print("Characters got by your shenchenbazi: ")
    print(wuxingCharacters)

    desiredCharacters = set(list(readDic.main()))
    print("Characters got by your wish: ")
    print(desiredCharacters)

    gender = input("Male or female? Input 1 to represent male, input 2 to represent female: ")
    if gender == 1:
        genderCharacters = set(characters.maleNames)
    else:
        genderCharacters =set(characters.femaleNames)
    print("Characters got by gender: ")
    print(genderCharacters)
    finalResult = desiredCharacters & desiredCharacters & genderCharacters
    print('Final result: ')
    print(finalResult)
    finalResultList = list(finalResult)
    finalName = finalResultList[random.randint(0, len(finalResultList))] + finalResultList[random.randint(0, len(finalResultList))]
    print('Test name: ')
    print(finalName)

if __name__ == '__main__':
    main()