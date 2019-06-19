# 문제 3)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper()
basicStringList = list(s.replace(',','').replace('.','').replace('\n','').split(' '))
sorted_set_basicStringList = sorted(list(set(basicStringList)))

print("""
문자 대문자 변환 후 정렬
----------------------------""")

for sortedString in sorted_set_basicStringList:
    print(sortedString)

print("""

단어의 빈도수 출력
-------------------------""")
for string in sorted_set_basicStringList:
    print("{0}:{1}".format(string, basicStringList.count(string)))