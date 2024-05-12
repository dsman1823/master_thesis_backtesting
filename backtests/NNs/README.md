# Experiment 1 
* The model overfitted for period from December 15, 2020, to December 15, 2023 is stored in network_overfitted_periodA.pth.
* The model overfitted for period from March 19, 2007, to December 15, 2023 is stored in network_overfitted_periodB.pth.
_____
# Experiment 2 
Experiment 2 trained models are stored in trained_on_old_data and trained_on_new_data folders.
* trained_on_old_data contains models trained for period from January 01, 2007 to December 15, 2020.
* trained_on_new_data contains models trained for period from January 01, 2007 to December 15, 2023.

All the models were trained using the following settings:

* LstmNetFullOpti3(5,  0.1, 'diagonal', 1)
* LstmNetMinVar3(5,  .15, None, 1)
* RnnNetMinVar3(5,  .15, None, 1)
* RnnNetFullOpti3(5,  0.2, 'diagonal', 1) 
* DenseNetMinVar2(1, 50, 5,  max_weight=1, p=0.2)
* DenseNetFullOpti2(1, 50, 5,  max_weight=1, p=0.2)
* ConvNetMinVar2(1, 50, 5, .15, 1)
* ConvNetFullOpti2(1, 50, 5, .15, 1)