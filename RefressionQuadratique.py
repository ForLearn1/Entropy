# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:30:28 2024

@author: User
"""

import numpy as np

# Données du tableau
X_i = np.array([4, 12, 13, 14, 14])
Y_i = np.array([250, 320, 250, 380, 260])

# Régression polynomiale (polynôme de degré 2)
coefficients = np.polyfit(X_i, Y_i, 2)  # Ajustement du polynôme
polynomial = np.poly1d(coefficients)

# Extraction des coefficients
a, b, c = coefficients
print(f"Expression du polynôme : y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}")
