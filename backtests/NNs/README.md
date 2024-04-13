* LstmNetFullOpti2(5,  0.1, 'diagonal', 1)
* LstmNetMinVar2(5,  0.2, 'diagonal', 1) 
* RnnNetMinVar3(5,  .15, None, 1)
* RnnNetFullOpti2(5,  0.2, 'diagonal', 1) # <--- Actually dropout is not applied 
* DenseNetMinVar2(1, 50, 5,  max_weight=1, p=0.2)
* DenseNetFullOpti2(1, 50, 5,  max_weight=1, p=0.2)
* ConvNetMinVar2(1, 50, 5, .15, 1)
* ConvNetFullOpti2(1, 50, 5, .15, 1)