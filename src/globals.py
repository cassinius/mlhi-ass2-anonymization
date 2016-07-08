## GLOBAL VARIABLES

# The k anonymization factor
K_FACTOR = 9

# Weight of the Generalization Information Loss
ALPHA = 1

# Weight of the Structural Information Loss
BETA = 0

# Weight vector for generalization categories
GEN_WEIGHT_VECTORS = {
    'equal': {
        'categorical': {
            'workclass': 1.0/6.0,
            'native-country': 1.0/6.0,
            'sex': 1.0/6.0,
            'race': 1.0/6.0,
            'marital-status': 1.0/6.0
        },
        'range': {
            'age': 1.0/6.0
        }
    },
    'emph_race': {
        'categorical': {
            'workclass': 0.02,
            'native-country': 0.02,
            'sex': 0.02,
            'race': 0.9,
            'marital-status': 0.02,
        },
        'range': {
            'age': 0.02,
        }
    },
    'emph_age': {
        'categorical': {
            'workclass': 0.02,
            'native-country': 0.02,
            'sex': 0.02,
            'race': 0.02,
            'marital-status': 0.02,
        },
        'range': {
            'age': 0.9,
        }
    }
}

# Chosen weight vector
VECTOR = 'emph_age'
