#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from pydub import AudioSegment
import random

#########################################################
#指定したファイルらをランダム結合して一つの音声ファイルにするスクリプト#
#########################################################

#mp3ファイルを結合操作できる形で格納

start = AudioSegment.from_file("start.mp3", format="mp3")
normal = AudioSegment.from_file("normal.mp3", format="mp3")
sokuho = AudioSegment.from_file("sokuho.mp3", format="mp3")
atsumori = AudioSegment.from_file("atsumori.mp3", format="mp3")
corner = AudioSegment.from_file("corner.mp3", format="mp3")

n_end1 = AudioSegment.from_file("n_end1.mp3", format="mp3")
n_end2 = AudioSegment.from_file("n_end2.mp3", format="mp3")
n_end3 = AudioSegment.from_file("n_end3.mp3", format="mp3")
n_end4 = AudioSegment.from_file("n_end4.mp3", format="mp3")

a_end1 = AudioSegment.from_file("a_end1.mp3", format="mp3")
a_end2 = AudioSegment.from_file("a_end2.mp3", format="mp3")
a_end3 = AudioSegment.from_file("a_end3.mp3", format="mp3")
a_end4 = AudioSegment.from_file("a_end4.mp3", format="mp3")

c_end1 = AudioSegment.from_file("c_end1.mp3", format="mp3")
c_end2 = AudioSegment.from_file("c_end2.mp3", format="mp3")
c_end3 = AudioSegment.from_file("c_end3.mp3", format="mp3")
c_end4 = AudioSegment.from_file("c_end4.mp3", format="mp3")

n_sokuho1 = AudioSegment.from_file("s1_normal.mp3", format="mp3")
n_sokuho2 = AudioSegment.from_file("s2_normal.mp3", format="mp3")
n_sokuho3 = AudioSegment.from_file("s3_normal.mp3", format="mp3")

c_sokuho1 = AudioSegment.from_file("s1_corner.mp3", format="mp3")
c_sokuho2 = AudioSegment.from_file("s2_corner.mp3", format="mp3")
c_sokuho3 = AudioSegment.from_file("s3_corner.mp3", format="mp3")

a_sokuho1 = AudioSegment.from_file("s1_atsumori.mp3", format="mp3")
a_sokuho2 = AudioSegment.from_file("s2_atsumori.mp3", format="mp3")
a_sokuho3 = AudioSegment.from_file("s3_atsumori.mp3", format="mp3")


#ファイル末尾連番名初期値定義
#変数初期化
i = 354
period1 = period2 = period3 = period4 = period5 = period6 = period7 = 0

#ループ処理開始
while i < 484:
    result = "combined_sounds"

#終了きっかけになる音声をリスト化してシャッフル
    endlist = ["n_end1", "n_end2", "n_end3", "n_end4", "a_end1", "a_end2", "a_end3", "a_end4", "c_end1", "c_end2", "c_end3", "c_end4"]
    random.shuffle(endlist)

    end0 = endlist[0]
    if "n_end" in end0:
        if end0 == "n_end1":
            end = n_end1
        elif end0 == "n_end2":
            end = n_end2
        elif end0 == "n_end3":
            end = n_end3
        elif end0 == "n_end4":
            end = n_end4
    elif "a_end" in end0:
        if end0 == "a_end1":
            end = a_end1
        elif end0 == "a_end2":
            end = a_end2
        elif end0 == "a_end3":
            end = a_end3
        elif end0 == "a_end4":
            end = a_end4
    elif "c_end" in end0:
        if end0 == "c_end1":
            end = c_end1
        elif end0 == "c_end2":
            end = c_end2
        elif end0 == "c_end3":
            end = c_end3
        elif end0 == "c_end4":
            end = c_end4

#結合中、指定したグループ内で2回しか登場させないファイルをリスト化してシャッフル

    warikomilist = ["n_sokuho1", "n_sokuho2", "n_sokuho3", "c_sokuho1", "c_sokuho2", "c_sokuho3", "a_sokuho1", "a_sokuho2", "a_sokuho3"]
    random.shuffle(warikomilist)
    warikomi0 = warikomilist[0]
    warikomi00 = warikomilist[1]
    if "n_sokuho1" == warikomi0:
        warikomi = n_sokuho1
    elif "n_sokuho2" == warikomi0:
        warikomi = n_sokuho2
    elif "n_sokuho3" == warikomi0:
        warikomi = n_sokuho3
    elif "c_sokuho1" == warikomi0:
        warikomi = c_sokuho1
    elif "c_sokuho2" == warikomi0:
        warikomi = c_sokuho2
    elif "c_sokuho3" == warikomi0:
        warikomi = c_sokuho3
    elif "a_sokuho1" == warikomi0:
        warikomi = a_sokuho1
    elif "a_sokuho2" == warikomi0:
        warikomi = a_sokuho2
    elif "a_sokuho3" == warikomi0:
        warikomi = a_sokuho3

    if "n_sokuho1" == warikomi00:
        warikomi2 = n_sokuho1
    elif "n_sokuho2" == warikomi00:
        warikomi2 = n_sokuho2
    elif "n_sokuho3" == warikomi00:
        warikomi2 = n_sokuho3
    elif "c_sokuho1" == warikomi00:
        warikomi2 = c_sokuho1
    elif "c_sokuho2" == warikomi00:
        warikomi2 = c_sokuho2
    elif "c_sokuho3" == warikomi00:
        warikomi2 = c_sokuho3
    elif "a_sokuho1" == warikomi00:
        warikomi2 = a_sokuho1
    elif "a_sokuho2" == warikomi00:
        warikomi2 = a_sokuho2
    elif "a_sokuho3" == warikomi00:
        warikomi2 = a_sokuho3


#終了きっかけ音声と、登場回数規定グループで場合分けしてリスト化
    if "n_end" in end0:
        if "n_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [atsumori, atsumori, corner, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, atsumori, atsumori, corner, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                l = [normal, atsumori, corner, corner, warikomi, warikomi2, end]                
        elif "a_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, atsumori, corner, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, normal, atsumori, corner, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                l = [normal, normal, corner, corner, warikomi, warikomi2, end]
        elif "c_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, atsumori, atsumori, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, normal, atsumori, atsumori, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                l = [normal, normal, atsumori, corner, warikomi, warikomi2, end]
    elif "a_end" in end0:
        if "n_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, atsumori, corner, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, normal, atsumori, corner, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                l = [normal, normal, corner, corner, warikomi, warikomi2, end]
        elif "a_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, normal, corner, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, normal, normal, corner, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                continue
        elif "c_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, normal, atsumori, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, normal, atsumori, atsumori, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                l = [normal, normal, normal, corner, warikomi, warikomi2, end]
    elif "c_end" in end0:
        if "n_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, atsumori, atsumori, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, normal, atsumori, atsumori, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                l = [normal, normal, atsumori, corner, warikomi, warikomi2, end]
        elif "a_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, normal, atsumori, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                l = [normal, normal, normal, atsumori, warikomi, warikomi2, end]
            elif "a_sokuho" in warikomi00:
                l = [normal, normal, normal, corner, warikomi, warikomi2, end]
        elif "c_sokuho" in warikomi0:
            if "n_sokuho" in warikomi00:
                l = [normal, normal, atsumori, corner, warikomi, warikomi2, end]
            elif "c_sokuho" in warikomi00:
                continue
            elif "a_sokuho" in warikomi00:
                l = [normal, normal, normal, atsumori, warikomi, warikomi2, end]

#場合分けしたリストファイルをシャッフルし、終了きっかけ音声のタイミングで生成か非生成かを決定し、順次結合、書き出し

    random.shuffle(l)
    print(l)
    combined_sounds = start + l[0]
    if l[0] == end:
        continue
    combined_sounds = combined_sounds + l[1]
    if l[1] == end:
        continue
    combined_sounds = combined_sounds + l[2]
    if l[2] == end:
        if warikomi == l[3] or warikomi == l[4] or warikomi == l[5] or warikomi ==l[6] or warikomi2 == l[3] or warikomi2 == l[4] or warikomi2 == l[5] or warikomi2 ==l[6]:
            continue
        if period3 == 16:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period3 += 1
        i += 1
        print("p3")
        print(period3)
        continue
    combined_sounds = combined_sounds + l[3]
    if l[3] == end:
        if warikomi == l[4] or warikomi == l[5] or warikomi ==l[6] or warikomi2 == l[4] or warikomi2 == l[5] or warikomi2 ==l[6]:
            continue
        if period4 == 20:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period4 += 1                
        i += 1
        print("period4")
        print(period4)
        continue
    combined_sounds = combined_sounds + l[4]
    if l[4] == end:
        if warikomi == l[5] or warikomi ==l[6] or warikomi2 == l[5] or warikomi2 ==l[6]:
            continue
        if period5 == 24:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period5 += 1
        i += 1
        print("period5")
        print(period5)
        continue
    combined_sounds = combined_sounds + l[5]
    if l[5] == end:
        if warikomi == l[6] or warikomi2 == l[6]:
            continue
        if period6 == 34:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period6 += 1
        i += 1
        print("period6")
        print(period6)
        continue
    combined_sounds = combined_sounds + l[6]
    if l[6] == end:
        if period7 == 36:
            continue
        result = result + str(i) + ".mp3"
        combined_sounds.export(result, format="mp3")
        period7 += 1
        i += 1
        print("period7")
        print(period7)
        continue
    print("out")
    break
print("end")
