from unittest import *

"""
text - строка, в которой выполняется поиск
patterns = [pattern_1, pattern_2, ..., pattern_n] - массив паттернов,\
которые нужно найти в строке text.
По аналогии с оригинальным алгоритмом, \
функция возвращает массив [indices_1, indices_2, ... indices_n].
При этом indices_i - массив индексов [pos_1, pos_2, ... pos_n], \
с которых начинаетй pattern_i в строке text.
Если pattern_i ни разу не встречается в строке text, \
ему соотвествует пустой массив, т.е. indices_i = []
"""
 
def search_rabin_multi(text, patterns): 
    indices = []
    for p in patterns:
        ind_n = []
        for i in range(len(text)): 
            if text[i: i + len(p)] == p:
                ind_n.append(i)
        indices.append(ind_n)
    return indices
# сложность алгоритма O(Т + Σ(Nn*Pn)),
#где Т - длина текста, Рn - количество разных типов паттернов,
#Nn - количество найденных паттернов одного типа
"""
text = 'какао макака матата'
print(search_rabin_multi(text, ['ка', 'ма']))
"""

class SearchNaiveTest(TestCase):
    def setUp(self):
        self.search = search_rabin_multi
        
    def test_empty(self):
        text = ''
        patterns = ['to', 'ba']
        self.assertEqual(len(self.search(text, patterns)), 2)
        
    def test_biger_pattern(self):
        text = 'blabla bla'
        patterns = ['blablabla', 'blablablablabla']
        self.assertEqual(len(self.search(text, patterns)), 2)
        
    def test_count(self):
        text = 'Карл украл у Клары кораллы, \
            А Клара украла у Карла кларнет.'
        patterns = ['ла', 'ра']
        indices = [[14, 43, 52, 60, 64], [7, 21, 45, 50]]
        self.assertListEqual(self.search(text, patterns), indices)
        
case = SearchNaiveTest()
suite = TestLoader().loadTestsFromModule(case)
TextTestRunner().run(suite)


