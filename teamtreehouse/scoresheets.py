class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)
    
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)
    
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)
    
    
    def score_chance(self, hand):
        return sum(hand)

    def score_yatzy(self, hand):
        score = 50
        check_value = hand[0]

        for i in hand:
            if i != hand[0]:
                score = 0
                break

        return score