#!/usr/bin/env python
# -*- coding: utf8 -*-

import typing
from Const import ConstT
from ReqBodyFill import ReqBodyFillF
from GoalRepo import GoalRpT
from MyConfig import goal_rpOrg, from_rpUrl_ls

goal_Rp_ls:typing.List[GoalRpT]=[ GoalRpT.build(from_rpUrl_k,goal_rpOrg) for from_rpUrl_k in from_rpUrl_ls]

for goal_rpK in goal_Rp_ls:
    ReqBodyFillF(goal_rpK)


