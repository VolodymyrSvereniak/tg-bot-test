from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item


# main = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Catalog")],
#         [KeyboardButton(text="Cart")],
#         [KeyboardButton(text="Contacts")],
#         [KeyboardButton(text="Contacts"), KeyboardButton(text="About Us")],
#     ],
#     resize_keyboard=True,
#     input_field_placeholder="Select option",
# )


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Catalog")],
        [KeyboardButton(text="Recycle bin")],
        [KeyboardButton(text="Contacts"), KeyboardButton(text="About us")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose option...",
)


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()

    for category in all_categories:
        keyboard.add(
            InlineKeyboardButton(
                text=category.name, callback_data=f"category_{category.id}"
            )
        )

    keyboard.add(
        InlineKeyboardButton(text="Back to main page", callback_data="to_main")
    )

    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_categories = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()

    for item in all_categories:
        keyboard.add(
            InlineKeyboardButton(text=item.name, callback_data=f"category_{item.id}")
        )
    keyboard.add(
        InlineKeyboardButton(text="Back to main page", callback_data="to_main")
    )

    return keyboard.adjust(2).as_markup()


# catalog = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Shoes", callback_data="shoes")],
#         [InlineKeyboardButton(text="Clothes", callback_data="clothes")],
#     ]
# )

# user_number = ReplyKeyboardMarkup(
#     keyboard=[[KeyboardButton(text="Send number", request_contact=True)]],
#     resize_keyboard=True,
# )
