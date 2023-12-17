import random, git
import binascii, struct
def V():
    randomNumber = random.randint(0, 100)
    if randomNumber <= 70:
        return False
    else:
        g = git.cmd.Git()
        blob = g.ls_remote('https://github.com/Rooplok/project', sort='-v:refname', tags=True)
        list_versions = blob.split('\n')
        list_clear_versions = []
        for version in list_versions:
            list_clear_versions.append(version.split('/')[-1])
        for version in list_clear_versions:
            if version[-1] == 'F':
                return version[:-1]

class R:
    def get3(self):
        dataA = b"This is a potential response from the firmware, Get 3, Channel A"
        crc32A = binascii.crc32(dataA) & 0xFFFFFFFF
        return dataA + struct.pack("!I", crc32A) # после этого нужно в GUI проверить контрольуя сумму, смотри ТГ

    def get2(self):
        data = b"This is a potential response from FirmWare, Get2"
        crc32 = binascii.crc32(data) & 0xFFFFFFFF
        return data + struct.pack("!I", crc32) # после этого нужно в GUI проверить контрольуя сумму, смотри ТГ

    def get1(self):
        data = b"This is a potential response from FirmWare, Get1"
        crc32 = binascii.crc32(data) & 0xFFFFFFFF
        return data + struct.pack("!I", crc32) # после этого нужно в GUI проверить контрольуя сумму, смотри ТГ

    def crc32(self, offset, size):
        if offset + size <= 1024:
            offset_size_data = struct.pack("!II", offset, size)
            crc32 = binascii.crc32(offset_size_data) & 0xFFFFFFFF
            return struct.pack("!I", crc32)
        else:
            return struct.pack("!I", 0)

    def key(self):
        randomNumber = random.randint(0, 100)
        if randomNumber <=20:
            return 'ER0'
        elif randomNumber <=40:
            return 'ER1'
        elif randomNumber <=60:
            return 'СК1'
        elif randomNumber <=80:
            return 'СК2'
        elif randomNumber <=100:
            return 'СК3'


class W:
    def put(self, data):
        crc32 = binascii.crc32(data) & 0xFFFFFFFF
        return crc32

    def crc32(self, offset, size):
        if offset + size <= 1024:
            offset_size_data = struct.pack("!II", offset, size)
            crc32 = binascii.crc32(offset_size_data) & 0xFFFFFFFF
            return struct.pack("!I", crc32)
        else:
            return 0

    def key(self):
        randomNumber = random.randint(0, 100)
        if randomNumber <=20:
            return 'ER0'
        elif randomNumber <=40:
            return 'ER1'
        elif randomNumber <=60:
            return 'СК1'
        elif randomNumber <=80:
            return 'СК2'
        elif randomNumber <=100:
            return 'СК3'


class P:
    def protection(self, variety):
        randomNumber = random.randint(0, 100)
        if randomNumber <= 10 and variety == 'SETWP':
            return 'ER0'
        elif randomNumber <= 25 and variety == 'SETWP':
            return 'ER1'
        elif randomNumber <= 40 and variety == 'SETWP':
            return 'ER2'
        elif randomNumber <= 55 and variety == 'RESWP':
            return 'ER3'
        elif randomNumber <= 65 and variety == 'RESWP':
            return 'ER4'
        elif randomNumber <= 75 and variety == 'RESWP':
            return 'ER5'
        elif randomNumber <= 90 and variety == 'SETWP':
            return 'СК0'
        elif randomNumber <= 100 and variety == 'RESWP':
            return 'СК0'

    def key(self):
        randomNumber = random.randint(0, 100)
        if randomNumber <=20:
            return 'ER0'
        elif randomNumber <=40:
            return 'ER1'
        elif randomNumber <=60:
            return 'СК1'
        elif randomNumber <=80:
            return 'СК2'
        elif randomNumber <=100:
            return 'СК3'


if __name__ == '__main__':
    print(R())