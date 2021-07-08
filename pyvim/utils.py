from PyQt5 import QtGui

INSERT_MODE_KEYS = [
    "0x61",  # a
    "0x41",  # i
    "0x69",  # A
    "0x49",  # I
    "0x1000006",  # insert key
]


def key_to_hex(k: QtGui.QKeyEvent) -> str:
    """
    Takes a key event and returns it as
        a hexadecimal number (which is a string).

    Args:
        k (QtGui.QKeyEvent): Key event.

    Returns:
        str: Hexadecimal number (which is a string).
    """
    key_hex = None

    try:
        if 65 <= ord(k.text()) <= 122:
            key_hex = hex(k.nativeVirtualKey())
        else:
            key_hex = hex(k.key())
    except Exception:
        pass
    finally:
        if key_hex is None:
            key_hex = hex(k.key())

    return key_hex
