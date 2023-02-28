sp = 67836.43
mg = 29229.88
rj = 36678.66
es = 27165.48
outros = 19849.53
soma = sp + mg + rj + es + outros

print(f'Soma total dos faturamentos: R${soma:.2f}')
print(f'São Paulo faturou R${sp:.2f} que representa {sp/soma:.2%} do total')
print(f'Minas Gerais faturou R${mg:.2f} que representa {mg/soma:.2%} do total')
print(f'Rio de Janeiro faturou R${rj:.2f} que representa {rj/soma:.2%} do total')
print(f'Espírito Santo faturou R${es:.2f} que representa {es/soma:.2%} do total')
print(f'Outros estados faturaram R${outros:.2f} que representam {outros/soma:.2%} do total')