from blockchain import Blockchain

blockchain = Blockchain()

#versi halal
blockchain.add_block({
    "Merek": "Mie Samyang",
    "Flavour": "Keju",
    "Ingredients": [
        "Tepung Terigu", 
        "Tapioka", 
        "Minyak Wijen",
        "Ekstrak Cabai"
    ], 
    "Production": "PT. GayaBebas"
})

#versi haram
blockchain.add_block({
    "Merek": "Mie Samyang",
    "Flavour": "Spicy Pork",
    "Ingredients": [
        "Tepung Terigu",
        "Minyak Babi",
        "Pork Extract"
    ],
    "Production": "PT. GayaBebas"
})

#cetak isi wir!
for block in blockchain.chain:
    print("=" * 50)
    print("INDEX   :", block.index)
    print("ID      :", block.id)
    print("EXPIRED :", block.expired)
    print("DATA    :", block.data)
    print("PREV    :", block.previous_hash)
    print("HASH    :", block.hash)
    
print("\nBlockchain valid:", blockchain.is_valid())