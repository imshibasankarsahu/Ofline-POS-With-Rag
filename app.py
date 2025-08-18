# app.py
from stt import transcribe_audio
from rag import load_inventory, embed_inventory, build_faiss_index, search_inventory
from llm import generate_response
from utils import Cart
from sentence_transformers import SentenceTransformer
#main() Function
def main(audio_path):
    transcript = transcribe_audio(audio_path)
    print("Transcript:", transcript)
    #Load Inventory and Build Search Index
    inventory = load_inventory()
    embeddings, embedder = embed_inventory(inventory)
    index = build_faiss_index(embeddings)
    cart = Cart()
    #Possible Commands
    commands = ['add', 'remove', 'checkout']
    #Command Execution Loop
    for command in commands:
        if command in transcript:
            if command == 'add':
                products = search_inventory(transcript, embedder, index, inventory)
                product_row = products.iloc[0]
                cart.add_item(product_row["name"], product_row["price"], qty=1)
                print(f"Added {product_row['name']} to cart!")
            elif command == 'remove':
                products = search_inventory(transcript, embedder, index, inventory)
                product_row = products.iloc[0]
                cart.remove_item(product_row["name"], product_row["price"], qty=1)
                print(f"Removed {product_row['name']} from cart!")
            elif command == 'checkout':
                items, total = cart.show_cart()
                print(f"Checked out: {items} | Total: {total}")
            break

    print("Cart state:", cart.show_cart())

# file run of wav file 
if __name__ == "__main__":
    main("sample_audio.wav")  
