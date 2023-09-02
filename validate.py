expected_tokens = {
    "code",
    "param"
}

def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code:
        return "missing paren"
    if ")" not in code:
        return "missing paren"
    #if "()" in code:
    #    return "missing param"
    for token in expected_tokens:
        if not f"({token})" in code:
            return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True

print(validate('''
               def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code:
        return "missing paren"
    if ")" not in code:
        return "missing paren"
    #if "()" in code:
    #    return "missing param"
    if not "(code)" in code:
        return "missing Param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True
               '''))


    
    