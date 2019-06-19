# 문제1. 파이썬 경로명
# s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요

s = '/usr/local/bin/python'

splitS = s[1:].split('/')
directory = ','.join(splitS)
print('디렉토리 경로명 :', directory)

# 디렉토리 경로명과 파일명을 분리하여 출력하세요.
rsplitS = ','.join(s.rsplit('/', 1))
print('디렉토리 경로명, 파일명 분리 :' , rsplitS)

