class Parser:

    def parse(self, tokens):
        self.tokens = tokens
        self.tok = None  # Last symbol consumed
        self.nexttok = None  # Next symbol tokenised
        self._advance()  # Load first token
        return self.expr()

    # Advance one token ahead
    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    # Test and consume the next token if it matches toktype
    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    # Consume next token if it matches toktype or raise Syntax Error
    def _except(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    ########################## Grammar rules: ###############################

    # expression ::= term { ('+' | '-') term }*
    def expr(self):

        termval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()

            if op == 'PLUS':
                termval = ('+', termval, right)
            elif op == 'MINUS':
                termval = ('-', termval, right)

        return termval

    # term ::= factor { ( '*' | '/' ) factor }*
    def term(self):

        termval = self.factor()
        while self._accept('MUL') or self._accept('DIV'):
            op = self.tok.type
            right = self.factor()

            if op == 'MUL':
                termval = ('*', termval, right)
            elif op == 'DIV':
                termval = ('/', termval, right)

        return termval

    # factor ::= NUM | ( expr )
    def factor(self):

        # The current token is of type NUM
        if self._accept('NUM'):
            return int(self.tok.value)

        # The current token is of type ( expr )
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._except('RPAREN')
            return exprval

        else:
            raise SyntaxError('Expected NUMBER or LPAREN')
