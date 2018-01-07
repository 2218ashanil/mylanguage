#Ashley Anil
reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'print' : 'PRINT',
   'and'   : 'AND',
   'or'    : 'OR',
   'not'    : 'NOT',
   'in'    : 'IN'
}

variables = {}

class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class IndexNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        index = self.v1.evaluate()[self.v2.evaluate()]
        return index

class ListNode(Node):
    def __init__(self, v1):
        self.value = v1

    def evaluate(self):
        #list1 = self.value
        #evaluates every node in the list
        for i, element in enumerate(self.value):
            #evaluatedList = element.evaluate()
            evaluated = 1
            #stores every evaluated node in list back into list
            self.value[i] = element.evaluate()
            #list.value[i] = evaluatedList
        return self.value

class NumberNode(Node):
    def __init__(self, v1):
        #check if the number is a float or an integer
        if('.' not in v1):
            self.value = int(v1)
        else:
            self.value = float(v1)

    def evaluate(self):
        return self.value

class VariableNode(Node):
    def __init__(self, v1):
        self.v1 = v1

    def var_name(self):
        return self.v1

    def evaluate(self):
        value = variables.get(self.v1)
        if (value != None):
            return value
        else:
            return("SEMANTIC ERROR")

class PrintNode(Node):
    def __init__(self, v1):
       self.v1 = v1

    def execute(self):
        print(self.v1.evaluate())

class AssignmentNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def execute(self):
        variables[self.v1.var_name()] = self.v2.evaluate()

class AssignmentIndexNode(Node):
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def execute(self):
        variables[self.v1.var_name()][self.v2.evaluate()] = self.v3.evaluate()

#and, or
class BooleanAndNode(Node):
    def __init__(self, operand, v1, v2):
        self.operand = operand
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        evaluated1 = self.v1.evaluate()
        evaluated2 = self.v2.evaluate()
        if((type(evaluated1) is int) and (type(evaluated2) is int)):
            error = 0
            return (evaluated1 and evaluated2)
        #the type is not integer
        else:
            error = 1
            return("SEMANTIC ERROR")

class BooleanOrNode(Node):
    def __init__(self, operand, v1, v2):
        self.operand = operand
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        evaluated1 = self.v1.evaluate()
        evaluated2 = self.v2.evaluate()
        #a or/ and operator should only check integers
        if((type(evaluated1) is int) and (type(evaluated2) is int)):
            error = 0
            return (evaluated1 or evaluated2)
        #the type is not integer
        else:
            error = 1
            return("SEMANTIC ERROR")

class NotNode(Node):
    def __init__(self, operand, v1):
        self.operand = operand
        self.v1 = v1

    def evaluate(self):
        evaluated = self.v1.evaluate()
        if(type(evaluated) is not int):
            error = 1
            return("SEMANTIC ERROR")
        else:
            error = 0
            return (not evaluated)

#tyoe of in should only be string or list
class InNode(Node):
    def __init__(self, operand, v1, v2):
        self.operand = operand
        self.v2 = v2
        self.v1 = v1

    def evaluate(self):
        evaluated1 = self.v1.evaluate()
        evaluated2 = self.v2.evaluate()
        error = 0
        #an in operator should only check lists and strings
        if(type(evaluated2) is list):
            error = 0
            return (evaluated1 in evaluated2)
        elif((type(evaluated1) is str) and (type(evaluated2) is str)):
            error = 0
            return (evaluated1 in evaluated2)
        else:
            error = 1
            return("SEMANTIC ERROR")

#==, <>, <, <=, >=
class ComparisonNode(Node):
    def __init__(self, operand, v1, v2):
        self.operand = operand
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        evaluated1 = self.v1.evaluate()
        evaluated2 = self.v2.evaluate()
        #an evaluated1 should only be an int or float
        #an evaluated2 should only be an int or float
        error = 0
        if((type(evaluated1) is int or type(evaluated1) is float) and (type(evaluated2) is int or type(evaluated2) is float)):
            if (self.operand == '=='):
                error = 0
                if evaluated1 == evaluated2: return 1
                else: return 0
            elif (self.operand == '<>'):
                error = 0
                if evaluated1 != evaluated2: return 1
                else: return 0
            elif (self.operand == '<'):
                error = 0
                if evaluated1 < evaluated2: return 1
                else: return 0
            elif (self.operand == '<='):
                error = 0
                if evaluated1 <= evaluated2: return 1
                else: return 0
            elif (self.operand == '>'):
                error = 0
                if evaluated1 > evaluated2: return 1
                else: return 0
            elif (self.operand == '>='):
                error = 0
                if evaluated1 >= evaluated2: return 1
                else: return 0
        else:
            error = 1
            return("SEMANTIC ERROR")

#division, floor, modulus,
class BopNodeDivision(Node):
    def __init__(self, operand, v1, v2):
        self.operand = operand
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        evaluated1 = self.v1.evaluate()
        evaluated2 = self.v2.evaluate()
        error = 0
        #divide operators should only be an int or float
        if (self.operand == '/'):
            if(((type(evaluated1) is int) or (type(evaluated1) is float)) and ((type(evaluated2) is int) or (type(evaluated2) is float))):
                error = 0
                #cannot divide by 0
                if(evaluated2 != 0):
                    #print(evaluated1 / evaluated2)
                    return(evaluated1 / evaluated2)
                else:
                    error = 0
                    #print("SEMANTIC ERROR")
                    return("SEMANTIC ERROR")
            else:
                error = 1
                #print("SEMANTIC ERROR")
                return("SEMANTIC ERROR")
        #divide operators should only be an int or float
        elif (self.operand == '%'):
            if(((type(evaluated1) is int) or (type(evaluated1) is float)) and ((type(evaluated2) is int) or (type(evaluated2) is float))):
                error = 0
                #cannot divide by 0
                if(evaluated2 != 0):
                    #print(evaluated1 % evaluated2)
                    return(evaluated1 % evaluated2)
                else:
                    error = 1
                    #print("SEMANTIC ERROR")
                    return("SEMANTIC ERROR")
            else:
                error = 1
                #print("SEMANTIC ERROR")
                return("SEMANTIC ERROR")
        #divide operators should only be an int or float
        elif (self.operand == '//'):
            if(((type(evaluated1) is int) or (type(evaluated1) is float)) and ((type(evaluated2) is int) or (type(evaluated2) is float))):
                error = 0
                #cannot divide by 0
                if(evaluated2 != 0):
                    #print(evaluated1 // evaluated2)
                    return(evaluated1 // evaluated2)
                else:
                    error = 1
                    #print("SEMANTIC ERROR")
                    return("SEMANTIC ERROR")
            else:
                error = 1
                #print("SEMANTIC ERROR")
                return("SEMANTIC ERROR")

 #exponent, addition, subtraction, multiplication
class BopNode(Node):
    def __init__(self, operand, v1, v2):
        self.operand = operand
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        evaluated1 = self.v1.evaluate()
        evaluated2 = self.v2.evaluate()
        error = 0
        #explonent operators should only be an int or float
        if (self.operand == '**'):
            if((type(evaluated1) is int or type(evaluated1) is float) and (type(evaluated2) is int or type(evaluated2) is float)):
                error = 0
                return(evaluated1 ** evaluated2)
            else:
                error = 1
                #print("SEMANTIC ERROR")
                return("SEMANTIC ERROR")
        #add operators should only be an string, list or float or int
        elif (self.operand == '+'):
            if((type(evaluated1) is str) and (type(evaluated2) is str)):
                error = 0
                return(evaluated1 + evaluated2)
            elif (((type(evaluated1) is int) or (type(evaluated1) is float)) and ((type(evaluated2) is int) or (type(evaluated2) is float))):
                error = 0
                return(evaluated1 + evaluated2)
            elif((type(evaluated1) is list) and (type(evaluated2) is list)):
                error = 0
                return(evaluated1 + evaluated2)
            else:
                error = 1
                return("SEMANTIC ERROR")
        #minus operators should only be an int or float
        elif (self.operand == '-'):
            if(((type(evaluated1) is int) or (type(evaluated1) is float)) and ((type(evaluated2) is int) or (type(evaluated2) is float))):
                error = 0
                return(evaluated1 - evaluated2)
            else:
                error = 1
                return("SEMANTIC ERROR")
        #multiply operators should only be an int or float
        elif (self.operand == '*'):
            if(((type(evaluated1) is int) or (type(evaluated1) is float)) and ((type(evaluated2) is int) or (type(evaluated2) is float))):
                error = 0
                return(evaluated1 * evaluated2)
            else:
                error = 1
                return("SEMANTIC ERROR")

class StringNode(Node):
    def __init__(self, v):
        self.value = v

    def evaluate(self):
        #remove quotes to put single quotes in later
        return self.value.strip("\"")

#while(expression) { body_stmt }
class WhileNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def execute(self):
        #print("EVALUATE: ", self.v1.evaluate())
        while(self.v1.evaluate()):
            #print("EVALUATE: ", self.v1.evaluate())
            self.v2.execute()

class IfNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def execute(self):
        #print("--hereif")
        if(self.v1.evaluate()):
            self.v2.execute()

class IfElseNode(Node):
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def execute(self):
        #print("--ifelsenode")
        if(self.v1.evaluate()):
            #print("--hereif")
            self.v2.execute()
        else:
            #print("--else")
            self.v3.execute()

class StmtBodyNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def execute(self):
        self.v1.execute()
        if(self.v2 != None):
            self.v2.execute()


tokens = [
    'NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','FLOOR',
    'LPAREN','RPAREN', 'EXPONENT', 'MODULUS',
    'GRTTHN', 'LESSTHN', 'GRTREQ','LESSEQ', 'EQUAL', 'NOTEQUAL',
    'STRING', 'COMMA', 'LBRACK', 'RBRACK', 'LCBRACE', 'RCBRACE',
    'VARIABLE', 'ASSIGN', 'SEMICOLON'
    ] + list(reserved.values())


# Tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACK  = r'\['
t_RBRACK  = r'\]'
t_EXPONENT = r'\*\*'
t_MODULUS = r'\%'
t_GRTTHN = r'\>'
t_LESSTHN = r'\<'
t_GRTREQ = r'\>\='
t_LESSEQ = r'\<\='
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\<\>'
t_STRING   = r'"[^\"]*"'
t_ASSIGN   = r'\='
t_COMMA    = r'\,'
t_FLOOR    = r'\/\/'
t_SEMICOLON = r'\;'
t_LCBRACE = r'\{'
t_RCBRACE = r'\}'

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
        #print("NumberNode")
        #print(t)
    except ValueError:
        print("NOT WITHIN BOUNDS %d", t.value)
        t.value = 0
    return t

def t_VARIABLE(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    #t.value = VariableNode(t.value)
    if( t.value in reserved.keys()):
        t.type = reserved.get(t.value)
    else:
        t.value = VariableNode(t.value)
    return t
# Ignored characters
t_ignore = " \t"

def t_error(p):
    raise ValueError("SYNTAX ERROR")

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LESSTHN', 'LESSEQ', 'EQUAL', 'NOTEQUAL', 'GRTTHN', 'GRTREQ'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'FLOOR'),
    ('left', 'EXPONENT'),
    ('left', 'MODULUS'),
    ('left', 'TIMES', 'DIVIDE')
    )


def p_root(p):
    '''root : LCBRACE stmt_body RCBRACE'''
    #print("--here in root")
    p[0] = p[2]

def p_stmt_body(p):
    '''stmt_body : stmt stmt_body
                 | '''

    if(len(p) == 3):
        #print("--stmtbody")
        p[0] = StmtBodyNode(p[1], p[2])


def p_stmt(p):
    '''stmt : varassignment
            | whilestmt
            | ifstmt
            | ifelsestmt
            | printstmt'''
    #print("--stmt")
    p[0] = p[1]

def p_print(p):
   '''printstmt : PRINT LPAREN expression RPAREN SEMICOLON'''
   p[0] = PrintNode(p[3])

def p_while_stmt(p):
    '''whilestmt : WHILE LPAREN expression RPAREN bodystmt'''
    p[0] = WhileNode(p[3], p[5])

def p_if_stmt(p):
    '''ifstmt : IF LPAREN expression RPAREN bodystmt'''
    p[0] = IfNode(p[3], p[5])

def p_ifelse_stmt(p):
    '''ifelsestmt : IF LPAREN expression RPAREN bodystmt ELSE bodystmt'''
    p[0] = IfElseNode(p[3], p[5], p[7])

def p_body_stmt(p):
    '''bodystmt : LCBRACE stmt_body RCBRACE'''
    p[0] = p[2]

def p_assignment(p):
    '''varassignment : variable ASSIGN expression SEMICOLON'''
    p[0] = AssignmentNode(p[1], p[3])


def p_index_assignment(p):
    '''varassignment : variable LBRACK expression RBRACK ASSIGN expression SEMICOLON'''
    p[0] = AssignmentIndexNode(p[1], p[3], p[6])


def p_expression_binop_div(p):
    '''expression : expression DIVIDE expression
                  | expression MODULUS expression
                  | expression FLOOR expression'''

    binary = 1
    p[0] = BopNodeDivision(p[2], p[1], p[3])

def p_expression_binop(p):
    '''expression : expression TIMES expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression EXPONENT expression'''
    binary = 1
    p[0] = BopNode(p[2], p[1], p[3])

def p_compare(p):
    '''expression : expression LESSTHN expression
                  | expression GRTTHN expression
                  | expression LESSEQ expression
                  | expression GRTREQ expression
                  | expression EQUAL expression
                  | expression NOTEQUAL expression'''
    compare = 1
    p[0] = ComparisonNode(p[2], p[1], p[3])

def p_expression_compare(p):
    '''expression : expression IN expression'''
    if(p[2] == 'in'):
        p[0] = InNode(p[2], p[1], p[3])

def p_expression_list(p):
    '''expression : LBRACK items RBRACK'''
    p[0] = ListNode(p[2])

def p_expression_items(p):
    '''items : expression endlist
             | '''
    if len(p) != 3:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]

def p_expression_endlist(t):
    '''endlist : COMMA expression endlist
               |'''
    if len(t) != 4:
        t[0] = []
    else:
        t[0] = [t[2]] + t[3]

def p_expression_index(p):
    '''expression : expression LBRACK expression RBRACK'''
    #[1,2,3][1] = 2
    #[1,2,3][0] = 1
    #print(p[0])
    p[0] = IndexNode(p[1], p[3])

def p_expression_boolean_and(p):
    '''expression : expression AND expression'''
    #print(p[0])
    if(p[2] == 'and'):
        #print(p[3])
        p[0] = BooleanAndNode(p[2], p[1], p[3])

def p_expression_boolean_or(p):
    '''expression : expression OR expression'''
    #print(p[0])
    if(p[2] == 'or'):
        #print(p[0])
        p[0] = BooleanOrNode(p[2], p[1], p[3])

def p_expression_boolean_not(p):
    '''expression : NOT expression'''
    #print(p[0])
    if(p[1] == 'not'):
        #print(p[0])
        p[0] = NotNode(p[1], p[2])


def p_expression_factor(p):
    '''expression : factor'''
    #print("--factor")
    p[0] = p[1]

def p_expression_variable(p):
    '''expression : variable'''
    #print("--expression variable")
    p[0] = p[1]

def p_variable(p):
    '''variable : VARIABLE'''
    #print("--variable")
    p[0] = p[1]
    #print(p[0])


def p_string(p):
    '''expression : STRING'''
    #termina;
    #print(p[0])
    p[0] = StringNode(p[1])

def p_factor_number(p):
    '''factor : NUMBER'''

    p[0] = p[1]

def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_error(p):
    raise ValueError("SYNTAX ERROR")

import ply.yacc as yacc
yacc.yacc()

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
#fd = open(sys.argv[1], 'r')
#stripped = ""
fd = open(sys.argv[1])
contents = fd.read()
fd.close()
new_contents =contents.replace('\n', ' ')
fd = open('output.txt', 'w')
fd.write(new_contents)
fd.close()
fd= open('output.txt', 'r')

for line in fd:
    stripped = line.strip()
    #print("--",stripped)
    if stripped != '':
        #print("here")
        try:
            lex.input(stripped)
            while True:
                #print("Error")
                token = lex.token()
                if not token:
                     break
                #print(token)
            ast = yacc.parse(stripped)
            error = 0
            evaluated = ast.evaluate()
            if(type(evaluated) is str):
                if(evaluated == "SEMANTIC ERROR"):
                    error = 1
                    print(evaluated)
            error = 0
            ast.execute()
        except Exception as Exc:
            error = 1
            if Exc.args[0] != "SYNTAX ERROR":
                error = 1
                print("ERROR")
            else:
                error = 1
                print("SYNTAX ERROR")
