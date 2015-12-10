#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GoGo - Pokerbot
# Copyright 2015 Péricles Lopes Machado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Sandbox
#
# This script is used to test some features before integrate with the Robot

# Ranks:
# c = copas
# s = espadas
# h = paus
# d = ouros

#Values:
# 2 .. 9
# T = 10
# J, Q, K, A
# Unknown = __

from pokereval import PokerEval
from timeit import timeit

__author__ = 'gogo40'

pe = PokerEval()

ranks_ = ["h", "c", "d", "s"]

game_ = "holdem"
iterations_ = 10000000
dead_ = []

print "deck =  %s\n" % pe.card2string(pe.deck())

print "---------------------------------------"
n_players_ = input("N players> ")
print n_players_
print "---------------------------------------"

print "cards> 2, ... , 9, T, J, Q, K, A"
print "ranks> %s" % ranks_

player_hand_ = []
for i in range(1, 3):
    player_hand_.append(input("Player card %d> " % (i)))
pockets_ = [player_hand_]

print player_hand_

print "---------------------------------------"
for i in range(1, n_players_):
    pockets_.append(["__", "__"])

print "Pockets> "
print pockets_

print "---------------------------------------"
board_ = []

print "cards> 2, ... , 9, T, J, Q, K, A"
print "ranks> %s" % ranks_

for i in range(1, 6):
    board_.append(input("Board card %d> " % (i)))

print "Board> "
print board_
print "---------------------------------------"

time_start = timeit()

result_ = pe.poker_eval(game=game_, pockets=pockets_, dead=dead_, board=board_, iterations=iterations_)

time_end = timeit()

total_ = 0.0
ev_ = []
for r in result_['eval']:
    v = float(r['ev'])
    ev_.append(v)
    total_ = total_ + v

threshold_ = 100.0 / n_players_
print threshold_

id = 1

P = []
H = []

for e in ev_:
    p = (100.0 *  e) / total_
    h = p / threshold_
    print "p[%d] = %.02f%%" % (id, p)
    print "H[%d] = %.02f" % (id, h)

    P.append(p)
    H.append(h)

    id = id + 1


print "Player win probability: P = %.02f" % P[0]
print "Player power:  H = %.02f" % H[0]

print "Processing time elapsed: %.06f s" % (time_end - time_start)