import pandas as pd
from datetime import datetime

def export_csv(data):
    print('Creating CSV ...')
    df = pd.DataFrame(data)
    csv_file = 'products_{}.csv' .format(datetime.now().date())
    df.to_csv(csv_file, index=False)
    print("Done !")
