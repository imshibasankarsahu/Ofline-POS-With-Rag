# streamlit_app.py
import streamlit as st
from stt import transcribe_audio
from rag import load_inventory, embed_inventory, build_faiss_index, search_inventory
from utils import Cart
from sentence_transformers import SentenceTransformer

# Streamlit App
def main():
    st.set_page_config(page_title="Voice Shopping Assistant", page_icon="🛒", layout="wide")
    st.title("🛒 Voice Shopping Assistant")

    # Upload audio file
    audio_file = st.file_uploader("Upload your voice command (WAV only)", type=["wav"])

    if "cart" not in st.session_state:
        st.session_state.cart = Cart()
        st.session_state.inventory = load_inventory()
        st.session_state.embeddings, st.session_state.embedder = embed_inventory(st.session_state.inventory)
        st.session_state.index = build_faiss_index(st.session_state.embeddings)

    if audio_file is not None:
        # Save uploaded file
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_file.read())

        # Transcribe
        transcript = transcribe_audio("temp_audio.wav")
        st.write("### 🎙 Transcript")
        st.success(transcript)

        # Possible commands
        commands = ['add', 'remove', 'checkout']
        for command in commands:
            if command in transcript.lower():
                if command == 'add':
                    products = search_inventory(transcript, st.session_state.embedder, st.session_state.index, st.session_state.inventory)
                    product_row = products.iloc[0]
                    st.session_state.cart.add_item(product_row["name"], product_row["price"], qty=1)
                    st.success(f"✅ Added {product_row['name']} to cart!")
                elif command == 'remove':
                    products = search_inventory(transcript, st.session_state.embedder, st.session_state.index, st.session_state.inventory)
                    product_row = products.iloc[0]
                    st.session_state.cart.remove_item(product_row["name"], product_row["price"], qty=1)
                    st.warning(f"❌ Removed {product_row['name']} from cart!")
                elif command == 'checkout':
                    items, total = st.session_state.cart.show_cart()
                    st.write("### 🛍️ Checkout Summary")
                    st.json({"items": items, "total": total})
                break

    # Show Cart
    st.write("### 🛒 Current Cart")
    items, total = st.session_state.cart.show_cart()
    st.json({"items": items, "total": total})


if __name__ == "__main__":
    main()
