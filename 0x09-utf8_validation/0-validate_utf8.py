#!/usr/bin/python3
"""
Validate UTF8
"""


def validUTF8(data):
    """
    if data are UTF8 chars
    """
    binaryData = []
    charBytesPrv = 0
    charBytesCur = 0
    f = True

    for number in data:
        binaryData.append('{0:08b}'.format((number & 255)))

    for binary in binaryData:
        charBytesCur = countBytes(binary)
        if f:
            if charBytesCur == 0:
                continue

            if charBytesCur >= 2 and charBytesCur <= 4:
                charBytesPrv = charBytesCur
                f = False
                continue

            return False
        else:
            if binary[0] == '1' and binary[1] == '0':
                charBytesPrv -= 1
            elif charBytesPrv - 1 == charBytesCur:
                charBytesPrv = charBytesCur
            else:
                return False

            if charBytesPrv == 1:
                    f = True
    return f


def countBytes(binary):
    """
    count of bytes
    """
    Cnt1 = 0
    for i in binary:
        if int(i) == 0:
            break
        Cnt1 += 1
    return Cnt1
