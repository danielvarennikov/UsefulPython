import re
from collections import namedtuple
class Tokeniser:

    def __init__(self):
        self.VarName = r'(?P<VAR>[a-zA-Z_][a-zA-Z0-9]*)'
        self.Num = r'(?P<NUM>\d+)'
        self.Plus = r'(?P<PLUS>\+)'
        self.Minus = r'(?P<MINUS>\-)'
        self.Mul = r'(?P<MUL>\*)'
        self.DIV = r'(?P<DIV>\\)'
        self.Eq = r'(?P<EQ>=)'
        self.Ws = r'(?P<WS>\s+)'
        self.Lparen = r'(?P<LPAREN>()'
        self.Rparen = r'(?P<RPAREN>))'

        self.master_pat = re.compile('|'.join([self.VarName, self.Plus,self.Minus, self.Mul,self.DIV, self.Eq, self.Ws, self.Num, self.Lparen, self.Rparen]))
        self.Token = namedtuple('Token', ['type', 'value'])

    def _generate_tokens(self, pat, text,whitespaces):
        scanner = pat.scanner(text)
        for m in iter(scanner.match, None):
            if not (m.lastgroup == 'WS' and (not whitespaces)):
                yield self.Token(m.lastgroup, m.group())

    def tokens_iterable(self, text):
        scanner = self.master_pat.scanner(text)
        for m in iter(scanner.match, None):
            if not (m.lastgroup == 'WS'):
                yield self.Token(m.lastgroup, m.group())




    def tokenise(self, text, whitespaces=False):
        tokens = []
        for tok in self._generate_tokens(self.master_pat, text,whitespaces): tokens.append(tok)
        return tokens
