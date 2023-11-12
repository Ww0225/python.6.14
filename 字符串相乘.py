# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1,len2 = len(num1),len(num2)
        result = [0]*(len1+len2)
        for i in range(len1-1,-1,-1):
            carry = 0
            for j in range(len2-1,-1,-1):
                tmp_sum = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))+result[i+j+1]+carry
                result[i+j+1] = tmp_sum%10
                carry = tmp_sum//10
            result[i] += carry
        result_str = ''.join(map(str,result)).lstrip('0')
        return result_str if result_str else '0'