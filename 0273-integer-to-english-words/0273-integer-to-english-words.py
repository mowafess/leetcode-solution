# class Solution:
#     def numberToWords(self, num: int) -> str:
#         if num == 0:
#             return "Zero"
        
#         lt20 = [
#             '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 
#             'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 
#             'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
#             'Seventeen', 'Eighteen', 'Nineteen'
#         ]

#         tens = [
#             '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 
#             'Sixty', 'Seventy', 'Eighty', 'Ninety'
#         ]

#         thousands = [ 
#             (1_000_000_000, 'Billion'), 
#             (1_000_000, 'Million'), 
#             (1_000, 'Thousand')
#         ]

#         def translate(num):
#             if num == 0:
#                 return ''
#             elif num < 20:
#                 return lt20[num]
#             elif num < 100:
#                 q, r = divmod(num, 10)
#                 return tens[q] + (' ' + translate(r) if r else '')
#             else:
#                 q, r = divmod(num, 100)
#                 return lt20[q] + ' Hundred' + (' ' + translate(r) if r else '')

#         res = []
        
#         for factor, unit in thousands:
#             if num >= factor:
#                 quotient, num = divmod(num, factor)
#                 res.append(translate(quotient))
#                 res.append(unit)
        
#         if num > 0:
#             res.append(translate(num))

#         return ' '.join(res)


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # All unique number words
        words = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
            30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
            80: "Eighty", 90: "Ninety", 100: "Hundred", 1000: "Thousand",
            1000000: "Million", 1000000000: "Billion"
        }
        
        TEN = 10
        TWENTY = 2 * TEN
        HUNDRED = TEN ** 2
        THOUSAND = TEN ** 3
        MILLION = TEN ** 6
        BILLION = TEN ** 9

        def helper(n):
            if n == 0:
                return []
            elif n < TWENTY:
                return [words[n]]
            elif n < HUNDRED:
                return [words[(n // TEN) * TEN]] + helper(n % TEN)
            elif n < THOUSAND:
                return [words[n // HUNDRED], "Hundred"] + helper(n % HUNDRED)
            elif n < MILLION:
                return helper(n // THOUSAND) + ["Thousand"] + helper(n % THOUSAND)
            elif n < BILLION:
                return helper(n // MILLION) + ["Million"] + helper(n % MILLION)
            else:
                return helper(n // BILLION) + ["Billion"] + helper(n % BILLION)
        
        return " ".join(helper(num))