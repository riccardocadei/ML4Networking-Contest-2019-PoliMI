from imblearn.combine import SMOTETomek
 
def OverSampleUnderSampleA (X_tr, y_tr):
    smt = SMOTETomek(ratio='auto')
    X_smt, y_smt = smt.fit_sample(X_tr, y_tr)
    return X_smt, y_smt

from imblearn.under_sampling import RandomUnderSampler

def RandomUSOSA (X_tr, y_tr):
    rus = RandomUnderSampler(return_indices=True)
    X_rus, y_rus, id_rus = rus.fit_sample(X_tr, y_tr)
    print('Removed indexes:', id_rus)
    
    return X_rus, y_rus
