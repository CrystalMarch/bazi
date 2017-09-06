import re

searchTxt = input('your search txt: ')

with open('modern-chinese-dic.txt', 'r', encoding='utf-8') as f:
    # print(f.read())
    modernDic = f.read()
    print('length: ' + str(len(modernDic)))
    # expression1 = r'^\….*'
    # expression2 = r'.*\n$'
    # testExpression = r'^\….*美.*\n$'

    testExpression = r'.*' + searchTxt + r'.*\n'
    # expression = r'ｘ'
    # expression = expression1 + searchTxt + expression2
    print(testExpression)
    results = re.findall(testExpression, modernDic)
    for result in results:
        print(result)