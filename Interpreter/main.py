#!/usr/bin/env python

class AbstractExpression():
    "All terminal and non-terminal expressions will implement an interpret method"

    @staticmethod
    def interpret():
        """The 'interpret method gets called recursively for each AbstractExpression"""


class Number(AbstractExpression):
    def __int__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Add(AbstractExpression):
    "non-terminal expression"

    def __int__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Subtract(AbstractExpression):
    "non-terminal expression"

    def __int__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"


# the client
# the sentence compiles with a simple grammar of Number -> Operator -> Number -> etc.

SENTENCE = "5 + 4 -3 + 7 - 2"
print(SENTENCE)

# split the sentence into individual expressions that will be added to an abstract syntax tree (AST) as terminal and non-terminal expressions

TOKENS = SENTENCE.split(" ")
print(TOKENS)

# Manually Creating an AST from tokens
AST: list [AbstractExpression] = []
AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))
AST.append(Subtract(AST[0], Number(TOKENS[4])))
AST.append(Add(AST[1], Number(TOKENS[6])))
AST.append((Subtract(AST[2], Number(TOKENS[8]))))

# use the final AST row as the root node
AST_ROOT = AST.pop()

# interpret recursively through the full AST starting from the root
print(AST_ROOT.interpret())

# print out a representation of the AST_ROOT
print(AST_ROOT)
