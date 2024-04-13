How to ingest the backtesting data:
1. Use dataloader notebook to prepare the data for ingesting.
2. Change create extension.py file in $ZIPLINE_ROOT dir (https://zipline.ml4trading.io/bundles.html#ingesting-data-from-csv-files)
3. run 'zipline ingest -b bundle_name'
4. Fix zipline db issues (https://github.com/stefan-jansen/machine-learning-for-trading/issues/21). On lib PC you can use VS code.