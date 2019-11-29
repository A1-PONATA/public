# Violence와 NonViolence의 파일 리스트를 생성
# 1,0 라벨링 추가
import os

video_path = '/home/pirl/img/'

V = open('FP.txt','w')

nonV = open('LR.txt', 'w')
V3= open('RL.txt','w')
# Violence Data List

Vlist = os.listdir(video_path + 'fastpass.mp4')

Vlist7 = []
Vlist8 = []
Vlist9 = []
Vlist10 = []

for filename in Vlist:
    if len(filename) == 7:
        Vlist7.append(filename)
        Vlist7.sort()
    elif len(filename) == 8:
        Vlist8.append(filename)
        Vlist8.sort()
    elif len(filename) == 9:
        Vlist9.append(filename)
        Vlist9.sort()
    elif len(filename) == 10:
        Vlist10.append(filename)
        Vlist10.sort()
newVlist = Vlist7 + Vlist8 + Vlist9 + Vlist10

for filename in newVlist:
    name = filename.split('.')[0]
    V.write('FP/'+ name +' 1\n')

# NonViolence List

nonVlist = os.listdir(video_path + 'LR/')

nonVlist8 = []
nonVlist9 = []
nonVlist10 = []
nonVlist11 = []

for filename in nonVlist:
    if len(filename) == 8:
        nonVlist8.append(filename)
        nonVlist8.sort()
    elif len(filename) == 9:
        nonVlist9.append(filename)
        nonVlist9.sort()
    elif len(filename) == 10:
        nonVlist10.append(filename)
        nonVlist10.sort()
    elif len(filename) == 11:
        nonVlist11.append(filename)
        nonVlist11.sort()
newnonVlist = nonVlist8 + nonVlist9 + nonVlist10 + nonVlist11

for filename in newnonVlist:
    name = filename.split('.')[0]
    nonV.write('LR/'+ name +' 0\n')
#V3 list
V3list = os.listdir(video_path + 'RL/')

V3list12 = []
V3list13 = []
V3list14 = []
V3list15 = []

for filename in V3list:
    if len(filename) == 12:
        V3list12.append(filename)
        V3list12.sort()
    elif len(filename) == 13:
        V3list13.append(filename)
        V3list13.sort()
    elif len(filename) == 14:
        V3list14.append(filename)
        V3list14.sort()
    elif len(filename) == 15:
        V3list15.append(filename)
        V3list15.sort()
newV3list = V3list12 + V3list13 + V3list14 + V3list15

for filename in newV3list:
    name = filename.split('.')[0]
    V3.write('LR/'+ name +' 0\n')

V.close()
nonV.close()
V3.close()