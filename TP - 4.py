class PatriciaMerkleTrie:
    __slots__ = ['letter', 'children']   # shinks memory usage

    def __init__(self, letter):
        self.letter = letter
        self.children = []

    def __contains__(self, item):
        for c in self.children:
            if c.letter == item:
                return True

        return False

    def __eq__(self, other):
        if other == self.letter:
            return True

        return False

    def __len__(self):
        return len(self.children)

    def __str__(self):
        return self.letter

    def is_leaf(self):
        if len(self.children) == 0:
            return True

        else:
            return False

    def add(self, letter):
        for child in self.children:
            if child.letter == letter:
                return child

        obj = PatriciaMerkleTrie(letter)  # On cree une nouvelle lettre
        self.children.append(obj)         # On l'ajoute aux enfants de la lettre en cours
        return obj                        # On la retourne pour etre utilisee comme lettre courante plus tard

    def get(self, letter):
        for child in self.children:
            if child.letter == letter:
                return child

        return None

    def dump(self, racine):
        if self.is_leaf():
            print(racine + self.letter)

        else:
            for child in self.children:
                child.dump(racine + self.letter)

    def hash(self):
        if self.is_leaf():
            return hash(self.letter)

        else:
            h = hash(self.letter)
            for c in self.children:
                h += c.hash()
            return hash(h)


# 1. Ajouter des mots entiers
def add_new_word(root, new_word):
    """
    add_new_word(r,"Rubens")
    -> var= r.add("u")
    -> varr = var.add("b")
       var.add("e")
    """
    if new_word[0].lower() == root:
        var = root
        for l in new_word[1:]:
            var = var.add(l.lower())

    else:
        return


# 2. Verifier l'appartenance d'un mot dans la structure
def has_word(root, word):
    if word[0].lower() == root:
        var = root
        for l in word[1:]:
            var = var.get(l.lower())
            if var is None:
                return False
    else:
        return False

    return True


if __name__ == "__main__":
    dictionary = ['romane', 'romanus', 'romulus', 'rubens', 'ruber', 'rubicon', 'rubicundus']

    r = PatriciaMerkleTrie('r')
    for word in dictionary:
        add_new_word(r, word)

    r.dump('')

    print(has_word(r, "rubens"))
    print(has_word(r, "patricia"))
    print(has_word(r, "x_ae_12"))
    print(hex(r.hash()))