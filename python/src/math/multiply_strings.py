def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    LEN1 = len(num1)
    LEN2 = len(num2)
    res = 0
    for j in range(LEN2 - 1, -1, -1):
        digit2 = int(num2[j])
        sig2 = pow(10, LEN2 - j - 1)
        for i in range(LEN1 - 1, -1, -1):
            digit1 = int(num1[i])
            sig1 = pow(10, LEN1 - i - 1)
            res += digit2 * sig2 * digit1 * sig1

    return str(res)
