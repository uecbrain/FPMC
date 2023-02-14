# FPMCのデータにフォーマットを合わせる前処理
import pandas as pd

# すみやさんのコードで作成したsession_idを付与したデータ
df = pd.read_csv("{INPUT_PATH}/20_35.csv")

df["item_id"] = df["genre_1"] + df["genre_2"] + df["genre_3"]
df[["session_id", "item_id"]] = df[["session_id", "item_id"]].astype(int)

df['session_id'] = df['session_id'].dropna().apply(lambda x: str(int(x)))
df['item_id'] = df['item_id'].dropna().apply(lambda x: str(int(x)))

session_id = str(df.at[0, "session_id"])
txt = ""
txt_list = []
for index, row in df.iterrows():
    if(session_id == str(row['session_id'])):
        txt = txt + " " + str(row['item_id'])
    else:
        txt_list.append(txt)
        session_id = str(row['session_id'])
        txt = str(row['session_id']) + " " + str(row['item_id'])

user_id_list = df["session_id"].unique().tolist()
item_id = df["item_id"].unique().tolist()

with open("./rakuten_data/user_idx_list.txt", 'wt') as f:
    for ele in user_id_list[:30000]:
        f.write(ele + '\n')

with open("./rakuten_data/idxseq.txt", 'wt') as f:
    for ele in txt_list[:30000]:
        f.write(ele + '\n')

with open("./rakuten_data/item_idx_list.txt", 'wt') as f:
    for ele in item_id:
        f.write(ele + '\n')
