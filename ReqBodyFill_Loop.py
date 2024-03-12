#!/usr/bin/env python
# -*- coding: utf8 -*-

import typing
from Const import ConstT
from ReqBodyFill import ReqBodyFillF
from GoalRepo import GoalRpT
from MyConfig import goal_rpOrg, goal_rpUrl_ls

goal_Rp_ls:typing.List[GoalRpT]=[ GoalRpT.build(goal_rpUrl_k,goal_rpOrg) for goal_rpUrl_k in goal_rpUrl_ls]

for goal_rpK in goal_Rp_ls:
    ReqBodyFillF(goal_rpK)


