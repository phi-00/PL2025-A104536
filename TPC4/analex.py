import sys
import ply.lex as lex

tokens = (
    'SELECT', # select
    'VAR', # ?a
    'WHERE', #where
    'LCHAV', # {
    'RCHAV', # }
    'TYPE', # a
    'PREF_URI', # foaf:name, dbo:artist
    'STRING', # "Chuck Berry"@en
    'POINT', # .
    'LIMIT', # LIMIT
    'NUM', #1000
)

t_LCHAV = r'\{'
t_RCHAV = r'\}'
t_TYPE = r'a'
t_POINT = r'\.'
t_LIMIT = r'LIMIT'
t_SELECT = r'select'
t_WHERE = r'where'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'\?([a-z0-9]*)'
    t.value = t.value[1:]
    return t

def t_PREF_URI(t):
    r'[a-z]*:[a-zA-Z]*'
    return t

def t_STRING(t):
    r'"([^"]*)"@[a-zA-Z]{0,3}'
    t.value = t.value[1:t.value.find('"', 1)]
    return t

t_ignore = ' \t\n\r'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Construir o lexer
lexer = lex.lex()

def teste_lexer(data):
    lexer.input(data)
    for tok in lexer:
        print(tok)


def main():
    with open(sys.argv[1], 'r') as file:
        data = file.read()

    teste_lexer(data)

if __name__ == "__main__":
    main()