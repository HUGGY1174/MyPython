breads = ["호밀빵", "위트", "화이트"]
meats = ["미트볼", "소시지", "닭가슴살"]
vegis = ["양상추", "토마토", "오이"]
sauces = ["마요네즈", "허니 머스터드", "칠리"]

for bread in breads:
    for meat in meats:
        for vegi in vegis:
            for sauce in sauces:
                print(bread, "+",meat, "+",vegi, "+", sauce)
