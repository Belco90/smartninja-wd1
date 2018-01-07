CHARACTERISTICS = {
    'hair': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC',
    },
    'face': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA',
    },
    'eyes': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC',
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC',
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG',
    }
}

SUSPECTS = {
    'Eva': {
        'hair': 'blonde',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'female',
        'race': 'white',
    },
    'Larisa': {
        'hair': 'brown',
        'face': 'oval',
        'eyes': 'brown',
        'gender': 'female',
        'race': 'white',
    },
    'Matej': {
        'hair': 'black',
        'face': 'oval',
        'eyes': 'blue',
        'gender': 'male',
        'race': 'white',
    },
    'Miha': {
        'hair': 'brown',
        'face': 'square',
        'eyes': 'green',
        'gender': 'male',
        'race': 'white',
    }
}

with open('dna.txt', 'r') as dna_file:
    guilty_dna = dna_file.read()

guilty_characteristics = {}
guilty_name = ''

for characteristic_name, values in CHARACTERISTICS.iteritems():
    for characteristic_value, dna_slice in values.iteritems():
        if guilty_dna.find(dna_slice) != -1:
            guilty_characteristics[characteristic_name] = characteristic_value
            break

for suspect_name, values in SUSPECTS.iteritems():
    guilty_name = suspect_name

    for characteristic_name, characteristic_value in values.iteritems():
        if guilty_characteristics[characteristic_name] != characteristic_value:
            guilty_name = ''
            break

    if guilty_name:
        break

if guilty_name:
    print "The person who ate the ice cream was {}".format(guilty_name)

else:
    print "OMG! We don't know who ate the ice cream!"
