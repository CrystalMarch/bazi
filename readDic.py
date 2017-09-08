import re

def main():
    searchTxt = input('your search txt: ')
    charExp = r"(?<=^\*)\w{1}"
    wordExp = r"(?<=^\…)\w+(?=\＠)"
    with open('modern-chinese-dic.txt', 'r', encoding='utf-8') as f:
        modernDic = f.read()
        testExpression = r'.*' + searchTxt + r'.*\n'
        results = re.findall(testExpression, modernDic)
        relatedWordsDic = {}
        relatedCharactersDic = {}
        for result in results:
            matchedWord = re.search(wordExp, result)
            if (matchedWord):
                matchedWord = matchedWord.group()
                if len(matchedWord) <= 2:
                    relatedWordsDic[matchedWord] = result
            matchedCharacter = re.search(charExp, result)
            if (matchedCharacter):
                matchedCharacter = matchedCharacter.group()
                relatedCharactersDic[matchedCharacter] = result
                print(matchedCharacter)
                print(result)
    # print(relatedWordsDic.keys())
    return relatedCharactersDic.keys()
# main()