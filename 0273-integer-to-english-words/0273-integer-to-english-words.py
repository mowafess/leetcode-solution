class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        lt20 = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 
            'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 
            'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
            'Seventeen', 'Eighteen', 'Nineteen'
        ]

        tens = [
            '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 
            'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]

        thousands = [ 
            (1_000_000_000, 'Billion'), 
            (1_000_000, 'Million'), 
            (1_000, 'Thousand')
        ]

        def translate(num):
            if num == 0:
                return ''
            elif num < 20:
                return lt20[num]
            elif num < 100:
                q, r = divmod(num, 10)
                return tens[q] + (' ' + translate(r) if r else '')
            else:
                q, r = divmod(num, 100)
                return lt20[q] + ' Hundred' + (' ' + translate(r) if r else '')

        res = []
        
        for factor, unit in thousands:
            if num >= factor:
                quotient, num = divmod(num, factor)
                res.append(translate(quotient))
                res.append(unit)
        
        if num > 0:
            res.append(translate(num))

        return ' '.join(res)