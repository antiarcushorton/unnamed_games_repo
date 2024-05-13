from ingestion import nba_ingestion as nba, mlb_ingestion as mlb
import pandas as pd

nba_sched = nba.ingest_nba()
mlb_sched = mlb.ingest_mlb()

final_df = pd.concat([nba_sched, mlb_sched])
print(final_df)
