mtns = {'Mount Everest': 8848, 'Shishapangma': 8027, 'Cho Oyu': 8188, 'Nanga Parbat': 8126, 'Kangchenjunga': 8586}
for mtn in mtns.keys():
    print(mtn)
for height in mtns.values():
    print(height)
for mt, hgt in mtns.items():
    print(mt, "is", hgt, "meters tall")