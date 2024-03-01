import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities


start_session = pd.Timestamp('2007-1-3', tz='utc')
end_session = pd.Timestamp('2023-12-15', tz='utc')

register(
    'thesis1-bundle',
    csvdir_equities(
        ['daily'],
        'C:\Users\r0913246\thesis_backtest\data_preparation\thesis_1',
    ),
    calendar_name='NYSE', # US equities
    start_session=start_session,
    end_session=end_session
)