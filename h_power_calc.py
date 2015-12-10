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
# h power calculator
#
# A very simple heuristic to evaluate the hand quality

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
import timeit
from pokereval import PokerEval

__author__ = 'gogo40'

pe = PokerEval()

ranks_ = ["h", "c", "d", "s"]

game_ = "holdem"
iterations_ = 5000000
dead_ = []

#######################################
#h_power calculator
def h_power_calc(result_):
    total_ = 0.0
    ev_ = []
    for r in result_['eval']:
        v = float(r['ev'])
        ev_.append(v)
        total_ = total_ + v
    threshold_ = 100.0 / n_players_
    id = 1
    P = []
    H = []
    for e in ev_:
        p = (100.0 * e) / total_
        h = p / threshold_
        print "p[%d] = %.02f%%" % (id, p)
        print "H[%d] = %.02f" % (id, h)

        P.append(p)
        H.append(h)

        id = id + 1

    return (P, H, threshold_)
#######################################


print "deck =  %s\n" % pe.card2string(pe.deck())

print "---------------------------------------"
n_players_ = input("N players> ")
big_blind_ = input("Big Blind> ")

print "---------------------------------------"
print "cards> 2, ... , 9, T, J, Q, K, A"
print "ranks> %s" % ranks_

player_hand_ = []
for i in range(1, 3):
    player_hand_.append(input("Player card %d> " % (i)))
pockets_ = [player_hand_]

print player_hand_

print "---------------------------------------"
n_known_cards_ = input("Number of known hands> ")
for i in range(1, n_known_cards_):
    c1 = input("\t(%d) CARD1>" % (i))
    c2 = input("\t(%d) CARD2>" % (i))
    print "\n"
    pockets_.append([c1, c2])


for i in range(n_known_cards_, n_players_):
    pockets_.append(["__", "__"])

print "Pockets> "
print pockets_

print "---------------------------------------"
board_ = []

print "cards> 2, ... , 9, T, J, Q, K, A"
print "ranks> %s" % ranks_

n_known_cards_ = input("Number of known cards> ")

for i in range(1, n_known_cards_ + 1):
    board_.append(input("Board card %d> " % (i)))

for i in range(n_known_cards_, 5):
    board_.append("__")

print "Board> "
print board_
print "---------------------------------------"

time_start = timeit.default_timer()

result_ = pe.poker_eval(game=game_, pockets=pockets_, dead=dead_, board=board_, iterations=iterations_)

time_end = timeit.default_timer()


(P, H, threshold) = h_power_calc(result_)


print "Player win probability: P = %.02f" % P[0]
print "Player power:  H = %.02f" % H[0]
print "Threshold: threshold = %.02f" % threshold
print "Big blind: %.02f" % big_blind_
print "Bid: %.02f" % (big_blind_ * H[0])

print "Processing time elapsed: %.06f s" % (time_end - time_start)