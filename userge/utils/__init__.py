from .aiohttp_helper import AioHttp as get_response
from .functions import (
    check_owner,
    cleanhtml,
    deEmojify,
    escape_markdown,
    media_to_image,
    mention_html,
    mention_markdown,
    rand_array,
    rand_key,
    thumb_from_audio,
)
from .progress import progress
from .sys_tools import SafeDict, get_import_path, secure_text, terminate
from .tools import (
    get_file_id,
    humanbytes,
    parse_buttons,
    post_to_telegraph,
    runcmd,
    safe_filename,
    sublists,
    take_screen_shot,
    time_formatter,
)

import ujson
import aiofiles
from userge import userge

async def __init__():
  async with aiofiles.open("userge/xcache/get_me.json", "w+") as fn:
      json_data = await userge.get_me()
      await fn.write(json_data)
