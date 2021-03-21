# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge import userge

import ujson
import aiofiles
async with aiofiles.open("userge/xcache/get_me.json", "w+") as fn:
   json_data = await userge.get_me()
   await fn.write(json_data)

if __name__ == "__main__":
    userge.begin()
