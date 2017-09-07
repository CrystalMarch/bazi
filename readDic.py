import re

searchTxt = input('your search txt: ')
charExp = r"(?<=\*)\w{1}"
wordExp = r"(?<=\…)\w+(?=\＠)"

with open('modern-chinese-dic.txt', 'r', encoding='utf-8') as f:
    # print(f.read())
    modernDic = f.read()
    # print('length: ' + str(len(modernDic)))
    # expression1 = r'^\….*'
    # expression2 = r'.*\n$'
    # testExpression = r'^\….*美.*\n$'

    testExpression = r'.*' + searchTxt + r'.*\n'
    # expression = r'ｘ'
    # expression = expression1 + searchTxt + expression2
    # print(testExpression)
    results = re.findall(testExpression, modernDic)
    relatedWords = []
    relatedCharacters = []
    for result in results:
        matchedWord = re.search(wordExp, result)
        if (matchedWord):
            matchedWord = matchedWord.group()
            relatedWordDic = {matchedWord: result}
            print(matchedWord)
            # print(relatedWordDic)
            relatedWords.append(relatedWordDic)
        matchedCharacter = re.search(charExp, result)
        if (matchedCharacter):
            matchedCharacter = matchedCharacter.group()
            relatedCharacterDic = {matchedCharacter: result}
            print(matchedCharacter)
            # print(relatedCharDic)
            relatedCharacters.append(relatedCharacterDic)
# print(relatedCharacters)
# print(relatedWords)
# test1 = "*娇ｊｉāｏ（１）（小孩、花朵等）柔嫩、美丽可爱：撒～｜嫩红～绿。（２）娇气：才走几里地，就说腿酸，未免太～了。（３）过度爱护：～生惯养｜别把孩子～坏了。"
# test2 = "…娇娃＠美丽的少女（多用于戏曲中）。"

# print(re.search(charExp, test2).group())
# print(re.search(wordExp, test1).group())