# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 12:47
# @Author  : lx
# @IDE ：PyCharm
import random

def get_tracks(distance):
    tracks = []
    y = 0
    v = 0
    t = 1
    current = 0
    mid = distance * 3 / 4
    exceed = random.randint(40, 50)
    z = random.randint(30, 150)

    while current < (distance + exceed):
        if current < mid / 2:
            a = 2
        elif current < mid:
            a = 3
        else:
            a = -3
        a /= 2
        v0 = v
        s = v0 * t + 0.5 * a * (t * t)
        current += int(s)
        v = v0 + a * t

        y += random.randint(-3, 3)
        z = z + random.randint(6, 8)
        tracks.append([min(current, (distance + exceed)), y, z])

    while exceed > 0:
        exceed -= random.randint(0, 5)
        y += random.randint(-1, 3)
        z = z + random.randint(6, 8)
        tracks.append([min(current, (distance + exceed)), y, z])
    # return tracks
    track_str = ''
    for x in tracks:
        x = [str(i) for i in x]
        x = '|'.join(x)
        track_str += (x + ',')
    return track_str[:-1]


# test:
# dis_x =500
# print(get_tracks(int(dis_x * (392 / 118))))


