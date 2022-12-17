schema = {}

def loadSchema():

    schema["2s-bb"]     = ("2S-BB", None)
    schema["4s-bb"]     = ("4S-BB", None)
    schema["5s-bb"]     = ("5S-BB", None)
    schema["5s-bbv2"]   = ("5S-BBv2", None)

    schema["rwd"]       = ("RWD", None)
    schema["abs"]       = ("ABS", None)
    schema["bc"]        = ("BC", None)
    schema["speed"]     = ("SPEED", "n")

    schema["push"]      = ("PUSH", "b")
    schema["pull"]      = ("PULL", None)
    schema["halt"]      = ("HALT", None)

    schema["jump"]      = ("JP", "n")
    schema["jumpt"]     = ("JPT", "n")
    schema["jumpf"]     = ("JPF", "n")

    schema["call"]      = ("CALL", "n")
    schema["calli"]     = ("CALLI", None)
    schema["ret"]       = ("RET", None)

    schema["storea"]    = ("STA", None)
    schema["storeb"]    = ("STB", None)
    schema["storem"]    = ("STM", "s")
    schema["storei"]    = ("STI", None)
    
    schema["loada"]     = ("LDA", None)
    schema["loadb"]     = ("LDB", None)
    schema["loadm"]     = ("LDM", "s")
    schema["loadi"]     = ("LDI", None)

    schema["input"]     = ("INPUT", "s")
    schema["elemr"]     = ("ELEMR", "s")

    schema["lifo"]      = ("LIFO", "s")
    schema["iobuff"]    = ("IOBUFF", "s")
    schema["index"]     = ("INDEX", "n")
    schema["array"]     = ("ARRAY", "s")

    schema["incb"]      = ("INCB", None)
    schema["decb"]      = ("DECB", None)    
    schema["add"]       = ("ADD", None)
    schema["multi"]     = ("MULTI", None)
    schema["sub"]       = ("SUB", None)

    schema["ex"]        = ("EX", None)
    schema["testz"]     = ("TSTZ", None)
    schema["teste"]     = ("TSTE", None)
    schema["testg"]     = ("TSTG", None)

    schema["clrb"]      = ("CLRB", None)
    schema["clra"]      = ("CLRA", None)

    schema["prt"]       = ("PRT", None)
    #schema["plotter"]   = ("PLOTTER", "n")

    #schema["stop"]      = ("STOP", "s")
    schema["nop"]       = ("NOP", None)

    return(schema)


print(loadSchema())