from Si5351 import Si5351

si = Si5351()

# vco = 25 MHz * (24 + 2 / 3) = 616.67 MHz
si.setupPLL(si.PLL_A, 40, 1, 1)

# vco = 25 MHz * (24 + 3 / 3) = 616.67 MHz∫
si.setupPLL(si.PLL_B, 24, 2, 3)



print ("Set Output #0 ")
# out = 616.67 MHz / 45 = 13.703704 MHz
si.setupMultisynth(0, si.PLL_A, 254)
si.setupRdiv(0, si.R_DIV_8)

print ("Set Output #1 ")
si.setupPLL(si.PLL_B, 24, 2, 3)
si.setupMultisynth(1, si.PLL_A, 254)
si.setupRdiv(1, si.R_DIV_4)

print ("Set Output #2 ")
si.setupPLL(si.PLL_A, 40, 0, 1)
si.setupMultisynth(2, si.PLL_A, 1267)
si.setupRdiv(2, si.R_DIV_1)

si.enableOutputs(True)

def freq_gen(freq, out_sel, status_fq):

    si.setupPLL(si.PLL_A, 40, 0, 1)
    si.setupMultisynth(out_sel, si.PLL_A, 1000)
    si.setupRdiv(out_sel, si.R_DIV_1)

    si.enableOutputs(status_fq)


freq_gen(777.666,2,True)
