def wage_for_day(hr: int, rate: float) -> float:
 if hr<=8:
   return hr * rate
 elif hr>8:
   return 8*rate + (hr-8)*1.5*rate


print(wage_for_day(9,250))