from aiogram import types
from data import config
from models import Admin, User
from keyboards.inline import blank_callback, back_callback


async def get_keyboard(user: User):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    admin = await Admin().select_admin_by_user_id(user.id)
    if admin and config.ADMIN:
        for key, value in config.ADMIN.items():
            if not admin.role.name in ['improved', 'supreme'] and key == 'edit-groups':
                continue
            if (key == 'edit-faculties' or key == 'edit-admins') and admin.role.name != 'supreme':
                continue        
            keyboard.add(types.InlineKeyboardButton(value, callback_data=key))
    else:
        keyboard.add(types.InlineKeyboardButton("Нет тут ничего", callback_data=blank_callback.new(category='settings')))
    keyboard.add(types.InlineKeyboardButton('Назад', callback_data=back_callback.new(category='menu')))
    return keyboard