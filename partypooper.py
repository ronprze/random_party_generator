import csv
from random import randint, choice, shuffle

class PartyPooper:

    def __init__(self):
        self.is_biased = False
        self._parties = []
        with open("parties2019.csv", "r", encoding="utf8") as f:
            readcsv = csv.reader(f, delimiter=",")
            for row in readcsv:
                self._parties.append(tuple(row))

    def poop_my_party(self):
        # self.unsafe_shuffle()
        #return self._parties[randint(0, len(self._parties) - 1)][:2]
        self.shuffle_parties()
        return choice(self._parties)

    def shuffle_parties(self):
        return shuffle(self._parties)


    def unsafe_shuffle(self):
        """
            Fisher–Yates shuffle Algorithm
            just for fun and experimenting
        :return: A shuffled list
        """
        for i in range(len(self._parties) -1, 0,-1):
            j = randint(0, i + 1)
            self.swap_array(i, j)

        return self._parties

    def swap_array(self, i, j):
        self._parties[i], self._parties[j] = self._parties[j], self._parties[i]
        return self._parties

    def left_biased(self):
        """
            Biased RNG just for biased ppl
            Don't try this at home
        :return: RNG out of 2 parties
        """
        tmp_parties = [
            ('TYPE_PARTY_NAME'),
            ('TYPE_PARTY_NAME')
        ]
        return choice(tmp_parties)

party = PartyPooper()
pp = party.poop_my_party()
print("My selected party: " + str(pp[0]) + " - "
      + str(pp[1]))
