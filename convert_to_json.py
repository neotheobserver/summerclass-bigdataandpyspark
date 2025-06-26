import json

with open("dict_artists.json", "r") as f:
    data = json.load(f)

with open("fixed_da.json", "w", encoding="utf-8") as f_out:
    for key, value in data.items():
        record = {"id": key, "related_ids": value}
        json.dump(record, f_out, ensure_ascii=False)
        f_out.write("\n")
