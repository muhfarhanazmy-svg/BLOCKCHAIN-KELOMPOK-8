from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()] #wadah list pertamakali sebelum ada isinya (sblm di add)
        
    def create_genesis_block(self):
        #return untuk pertamakalinya
        return Block(
            index=0,
            data={"message": "Genesis Block - Sistem Sertifikasi BPOM & Halal"},
            previous_hash="0"
        )
    
    def add_block(self, data: dict):
        #daftar bahan2 non-halal cik
        blacklist_bahan = ["babi", "pork", "lard", "gelatin babi", "alkohol industri", "minyak babi", "pork extract"]
        
        #ambil list ingredients wir
        ingredients_input = data.get("Ingredients", data.get("ingredients", []))
        
        #pengecekan ingredients, guna status verifikasi halal
        status_halal = True
        for bahan in ingredients_input:
            bahan_lower = bahan.lower()
            for haram in blacklist_bahan:
                if haram in bahan_lower:
                    status_halal = False
                    break
            if not status_halal:
                break
                
        #ubah status verifikasi
        if status_halal:
            data["status_sertifikasi"] = "HALAL"
        else:
            data["status_sertifikasi"] = "NON-HALAL"

        #update dan simpan
        previous_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            data=data,
            previous_hash=previous_block.hash
        )
        self.chain.append(new_block)

    #cek rantai blockchain
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            
            if current.hash != current.calculate_hash():
                return False
                
            if current.previous_hash != previous.hash:
                return False
                
        return True