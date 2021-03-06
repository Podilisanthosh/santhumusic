""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="ð á´á´É´á´", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="ðµsá´Éªá´", callback_data=f'skip_current_song'),
      InlineKeyboardButton(text="ðá´ á´Êá´á´á´", callback_data=f'change_volume'),
    ], 
    [
      InlineKeyboardButton(text="ðÉ´á´á´á´¡á´Êá´ð¡", url="https://t.me/santhubotupadates"),
      InlineKeyboardButton(text="ðÉ¢Êá´á´á´ð", url="https://t.me/santhuvc"),
    ], 
    [ 
      InlineKeyboardButton(text="ðá´Êá´sá´", callback_data=f'set_close'),
    ]
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="ð¶sá´á´á´", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="ð¤á´á´á´sá´", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="ðÊá´sá´á´á´", callback_data=f'set_resume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="ðá´á´á´á´", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="ðá´É´á´á´á´á´", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="â", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "ð á´Êá´sá´", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "â", callback_data="stream_menu_panel"
      )
    ]
  ]
)
