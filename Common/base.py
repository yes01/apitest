import string, random


class Base:

    # 生成随机验证码
    def generate_verification_code(self):
        capta = ''
        words = ''.join((string.ascii_lowercase, string.digits))  ##生成6位小写字母和数字串随机组合
        for i in range(6):
            capta += random.choice(words)  ##随机选择一个字母或数字
        return capta

