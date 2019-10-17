import numpy as np

class Transition:

    def __init__(self, q1, s1, q2, s2, dir):
        self.q1 = q1
        self.s1 = s1
        self.q2 = q2
        self.s2 = s2
        self.dir = dir
        
    def accept(self, q, s):
        return q == self.q1 and s == self.s1

class MT:
    def __init__(self, alphabet, etats, etat_init, etats_finales, transitions=[]):
        self.alphabet = alphabet
        self.etats = etats
        self.etat_init = etat_init
        self.etats_finales = etats_finales
        self.transitions = transitions
        self.bande = list(" ")
        self.etat_c = etat_init
        self.i_tete = 0

    def step(self):
        for transi in self.transitions:
            if transi.accept(self.etat_c, self.bande[self.i_tete]):
                self.bande[self.i_tete] = transi.s2
                self.etat_c = transi.q2
                self.i_tete += transi.dir
                if self.i_tete == len(self.bande):
                    self.bande.append(" ")
                elif self.i_tete < 0:
                    self.bande.insert(0, " ")
                    self.i_tete = 0
                return True

        return False
    def run(self, mot):
        self.bande = list(mot)
        while(self.step()):
            print("==============================================")
            print(self.i_tete, " / ", self.etat_c)
            for i in range(self.i_tete+1):
                if i < self.i_tete:
                    for j in range(len(self.bande[i])):
                        print("     ", end="")
                else:
                    print("  V", end="")
            print()
                
            print(self.bande)
            print()

    def add_transi(self, q1, s1, q2, s2, dir):
        self.transitions.append(Transition(q1, s1, q2, s2, dir))

if __name__ == "__main__":
    alphabet = ["S", "1"]
    etats = ["q1", "q2", "q3", "q4"]
    etat_init = "q1"
    etats_finales = ["q1"]
    

    mt = MT(alphabet, etats, etat_init, etats_finales)

    mt.add_transi("q1", " ", "q4", " ", -1)

    mt.add_transi("q1", "S", "q1", "S",  1)
    mt.add_transi("q1", "1", "q2", "S", -1)

    mt.add_transi("q2", "S", "q2", "S", -1)
    mt.add_transi("q2", "1", "q2", "1", -1)

    mt.add_transi("q2", " ", "q3", " ", -1)

    mt.add_transi("q3", " ", "q3", "1",  1)
    mt.add_transi("q3", "1", "q3", "1",  1)

    mt.add_transi("q3", "S", "q1", "S",  1)

    mt.add_transi("q3", " ", "q4", " ", -1)
    mt.add_transi("q4", "S", "q4", " ", -1)

    mt.run("1111")
