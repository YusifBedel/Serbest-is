import numpy as np

# Matrisinizi təyin edin (nümunə üçün)
matris = np.array([[1, -2, 3], [4, -5, 6], [7, 8, -9]])

# Mənfi elementləri seçin
menfi_elementler = matris[matris < 0]

# Ən böyük mənfi elementi tapın
en_boyuq_menfi = np.max(menfi_elementler)

print("Ən böyük mənfi element:", en_boyuq_menfi)
