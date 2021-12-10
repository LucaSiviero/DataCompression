alphabets_ = {
    # zero entropy source
    "CONST" : {
        "a" : 1,
        "b" : 0,
        "c" : 0,
    },

    # 1/4 entropy source
    "K-ARY-25" : {
        "a" : .25,
        "b" : .15,
        "c" : .15,
        "d" : .15,
        "e" : .15,
        "f" : .15,
    },

    # 1/2 entropy source
    "K-ARY-50" : {
        "a" : .50,
        "b" : .25,
        "c" : .25,
    },

    # 3/4 entropy source
    "K-ARY-75" : {
        "a" : .75,
        "b" : .05,
        "c" : .05,
        "d" : .05,
        "e" : .05,
        "f" : .05,
    },

    # full (1) entropy source
    "RANDOM" : {
        "a" : .25,
        "b" : .25,
        "c" : .25,
        "d" : .25,
    },
}