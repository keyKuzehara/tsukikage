#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from pydub import AudioSegment
import random

############################################################
#指定した音声ファイルらをランダム結合して一つの音声ファイルにするスクリプト#
#終了きっかけの音声ファイルがいつくるかでそれぞれの生成数を操作する      #
############################################################


#使用音声ファイル定義

start = AudioSegment.from_file("start.mp3", format="mp3")
normal = AudioSegment.from_file("normal.mp3", format="mp3")
sokuho = AudioSegment.from_file("sokuho.mp3", format="mp3")
atsumori = AudioSegment.from_file("atsumori.mp3", format="mp3")
corner = AudioSegment.from_file("corner.mp3", format="mp3")

n_end1 = AudioSegment.from_file("n_end1.mp3", format="mp3")
n_end2 = AudioSegment.from_file("n_end2.mp3", format="mp3")
n_end3 = AudioSegment.from_file("n_end3.mp3", format="mp3")
n_end4 = AudioSegment.from_file("n_end4.mp3", format="mp3")

s_end1 = AudioSegment.from_file("s_end1.mp3", format="mp3")
s_end2 = AudioSegment.from_file("s_end2.mp3", format="mp3")
s_end3 = AudioSegment.from_file("s_end3.mp3", format="mp3")
s_end4 = AudioSegment.from_file("s_end4.mp3", format="mp3")

a_end1 = AudioSegment.from_file("a_end1.mp3", format="mp3")
a_end2 = AudioSegment.from_file("a_end2.mp3", format="mp3")
a_end3 = AudioSegment.from_file("a_end3.mp3", format="mp3")
a_end4 = AudioSegment.from_file("a_end4.mp3", format="mp3")

c_end1 = AudioSegment.from_file("c_end1.mp3", format="mp3")
c_end2 = AudioSegment.from_file("c_end2.mp3", format="mp3")
c_end3 = AudioSegment.from_file("c_end3.mp3", format="mp3")
c_end4 = AudioSegment.from_file("c_end4.mp3", format="mp3")


#ファイル末尾連番名初期値定義
i = 0
#ループ回数定義
j = 190

#終了きっかけ音声ファイルごとの生成数定義
endmark1 = 10
endmark2 = 10
endmark3 = 16
endmark4 = 20
endmark5 = 24
endmark6 = 34
endmark7 = 36
endmark8 = 30
endmark9 = 10

#変数初期化
period1 = period2 = period3 = period4 = period5 = period6 = period7 = period8 = period9 = 0
while i < j:
    result = "combined_sounds"

#終了きっかけになる音声ファイルをリスト化してシャッフル
    endlist = ["n_end1", "n_end2", "n_end3", "n_end4", "s_end1", "s_end2", "s_end3", "s_end4", "a_end1", "a_end2", "a_end3", "a_end4", "c_end1", "c_end2", "c_end3", "c_end4"]
    random.shuffle(endlist)
    end = endlist[0]

#決定した終了ファイルで場合分けして、使用する音声ファイル組み合わせを定義
    if "n_end" in end:
        if end == "n_end1":
            end = n_end1
        elif end == "n_end2":
            end = n_end2
        elif end == "n_end3":
            end = n_end3
        elif end == "n_end4":
            end = n_end4
        l = [normal, normal, sokuho, sokuho, atsumori, atsumori, corner, corner, end]
    elif "s_end" in end:
        if end == "s_end1":
            end = s_end1
        elif end == "s_end2":
            end = s_end2
        elif end == "s_end3":
            end = s_end3
        elif end == "s_end4":
            end = s_end4
        l = [normal, normal, normal, sokuho, atsumori, atsumori, corner, corner, end]    
    elif "a_end" in end:
        if end == "a_end1":
            end = a_end1
        elif end == "a_end2":
            end = a_end2
        elif end == "a_end3":
            end = a_end3
        elif end == "a_end4":
            end = a_end4
        l = [normal, normal, normal, sokuho, sokuho, atsumori, corner, corner, end]
    elif "c_end" in end:
        if end == "c_end1":
            end = c_end1
        elif end == "c_end2":
            end = c_end2
        elif end == "c_end3":
            end = c_end3
        elif end == "c_end4":
            end = c_end4
        l = [normal, normal, normal, sokuho, sokuho, atsumori, atsumori, corner, end] 

#使用音声ファイルシャッフル
    random.shuffle(l)
    print(l)
    combined_sounds = start + l[0]
    if l[0] == end:
        if period1 == endmark1:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period1 += 1
        i += 1
        continue
    combined_sounds = combined_sounds + l[1]
    if l[1] == end:
        if period2 == endmark2:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period2 += 1
        i += 1
        continue
    combined_sounds = combined_sounds + l[2]
    if l[2] == end:
        if period3 == endmark3:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period3 += 1
        i += 1
        continue
    combined_sounds = combined_sounds + l[3]
    if l[3] == end:
        if period4 == endmark4:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period4 += 1                
        i += 1
        continue
    combined_sounds = combined_sounds + l[4]
    if l[4] == end:
        if period5 == endmark5:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period5 += 1
        i += 1
        continue
    combined_sounds = combined_sounds + l[5]
    if l[5] == end:
        if period6 == endmark6:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period6 += 1
        i += 1
        continue
    combined_sounds = combined_sounds + l[6]
    if l[6] == end:
        if period7 == endmark7:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period7 += 1
        i += 1
        continue
    combined_sounds = combined_sounds + l[7]
    if l[7] == end:
        if period8 == endmark8:
            continue
        result = result + str(i) + ".mp3"  
        combined_sounds.export(result, format="mp3")
        period8 += 1
        i += 1
        continue
    combined_sounds = combined_sounds + l[8]
    if l[8] == end:
        if period9 == endmark9: 
            continue
        result = result + str(i) + ".mp3" 
        combined_sounds.export(result, format="mp3")
        period9 += 1
        i += 1
        continue
    print("out")
    break
print("end")
