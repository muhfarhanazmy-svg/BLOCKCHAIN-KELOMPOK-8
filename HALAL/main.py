from blockchain import Blockchain


blockchain = Blockchain()

#aktor 1 pabrik
blockchain.add_block({
    "no produk": "SAMYANG-001",
    "product": "Samyang Buldak Hot Lava",
    "bpom": "Terdaftar",
    "halal": "Tersertifikasi",
    "production_date": "2026-09-01",
    "expiry_date": "2028-09-01",
    "actor": "Pabrik",
    "location": "Korea Selatan"
})

#aktor 2 distributor
blockchain.add_block({
    "no produk": "SAMYANG-001",
    "product": "Samyang Buldak Hot Lava",
    "actor": "Distributor",
    "location": "Cirebon",
    "status": "Diterima"
})
#aktor3 itu tokoaja deh bikin kaya diatas 1 lagi, ststusnya ready buay dijual gitu cb ya
#
#
#
#


for block in blockchain.chain:

    print("=" * 50)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)


print("\nBlockchain valid:", blockchain.is_valid())