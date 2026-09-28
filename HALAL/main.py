from block import Block
<<<<<<< HEAD
from blockchain import Blockchain
from pow import proof_of_work
from pos import proof_of_stake

blockchain = Blockchain()

difficulty = 2

#disini aktor 1 - 4
# AKTOR 1 - Pabrik
blockchain.add_block({
    "no_produk": "SAMYANG-001",
    "product": "Samyang Buldak Hot Lava",
    "production_date": "2026-09-01",
    "expiry_date": "2028-09-01",
    "actor": "Pabrik",
    "location": "Korea Selatan"
})

# AKTOR 2 - BPOM
blockchain.add_block({
    "no_produk": "SAMYANG-001",
    "product": "Samyang Buldak Hot Lava",
    "actor": "BPOM",
    "status": "Terverifikasi",
    "bpom": "Terdaftar"
})

# AKTOR 3 - Distributor
blockchain.add_block({
    "no_produk": "SAMYANG-001",
    "product": "Samyang Buldak Hot Lava",
    "actor": "Distributor",
    "location": "Cirebon",
    "status": "Diterima"
})

# AKTOR 4 - Toko
blockchain.add_block({
    "no_produk": "SAMYANG-001",
    "product": "Samyang Buldak Hot Lava",
    "actor": "Toko",
    "location": "Cirebon",
    "status": "Ready untuk dijual"
})

=======
from pow import proof_of_work
from pos import proof_of_stake

>>>>>>> b64a8071cb42b633e5562e12c5ee7d780bbb6990
print("PROOF OF WORK")

block = Block(
    index=1,
    data="Produk telah diverifikasi",
    previous_hash="0"
)


<<<<<<< HEAD
difficulty = 6 #hmmmini dipake ga ya
=======
difficulty = 6
>>>>>>> b64a8071cb42b633e5562e12c5ee7d780bbb6990

print("\nData Block      :", block.data)
print("Difficulty      :", difficulty)

proof_of_work(block, difficulty)

print("Nonce           :", block.nonce)
print("Hash            :", block.hash)

print("\nPROOF OF STAKE")

validators = {
<<<<<<< HEAD
    "Pabrik": 10,
    "BPOM": 20,
    "Distributor": 30,
    "Toko": 40
=======
    "Farmer": 10,
    "Distributor": 20,
    "Warehouse": 30,
    "Retailer": 40
>>>>>>> b64a8071cb42b633e5562e12c5ee7d780bbb6990
}

print("\nValidator:")
for validator, stake in validators.items():
    print(f"- {validator}: {stake} stake")

selected = proof_of_stake(validators)

<<<<<<< HEAD
print("\nValidator terpilih:", selected)
=======
print("\nValidator terpilih:", selected)
>>>>>>> b64a8071cb42b633e5562e12c5ee7d780bbb6990
