""" 
    example of using lambda instead of ternary operator which is more efficient 
    nested 
    (lambda: falseValue, lambda: trueValue)[test]()
"""

# 'normal' condition
def calculate():
    av_score = (sum(self.scores) / len(self.scores))

        
    if av_score <= 100 and av_score >= 90:
        return 'O'
    elif av_score < 90 and av_score >= 80:
        return 'E'
    elif av_score < 80 and av_score >= 70:
        return 'A'
    elif av_score < 70 and av_score >= 55:
        return 'P'
    elif av_score < 55 and av_score >= 40:
        return 'D'
    else:
        return 'T'

# ternary operator 
def calculate(self):
    av_score = (sum(self.scores) / len(self.scores))
    return('O' if 90 <= av_score <= 100 else 'E' if 80 <= av_score < 90 else 'A' if 70 <= av_score < 80 else 'P' if 55 <= av_score < 70 else 'D' if 40 <= av_score <55 else 'T')

# using lambda
def calculate(self):
    av_score = (sum(self.scores) / len(self.scores))
    return((lambda: (lambda: (lambda: (lambda: (lambda: 'T', lambda: 'D')[40<= av_score < 55](), lambda: 'P') [55 <= av_score < 70](), lambda: 'A') [70 <= av_score < 80](), lambda: 'E')[80 <= av_score < 90](), lambda: 'O')[90 <= av_score <= 100]())