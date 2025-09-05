class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True  # e를 보기 전엔 의미 없음

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
                if seen_exp:
                    digit_after_exp = True

            elif ch in ['+', '-']:
                # 부호는 시작 위치 또는 e/E 바로 뒤에서만 허용
                if i > 0 and s[i-1].lower() != 'e':
                    return False

            elif ch == '.':
                # 점은 e/E 이후 불가, 그리고 한 번만
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in ['e', 'E']:
                # e/E는 한 번만, 그리고 앞에 숫자가 있어야 함
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                digit_after_exp = False  # e 뒤에 숫자 필요

            else:
                return False

        return seen_digit and (not seen_exp or digit_after_exp)
        