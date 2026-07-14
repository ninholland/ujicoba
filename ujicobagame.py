import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe Anti-Narkoba", layout="centered")

st.title("❌⭕ Game Tic-Tac-Toe: Sehat vs Narkoba")
st.subheader("Mode Lokal 2 Pemain (Satu Layar)")

# Inisialisasi State Game
if 'board' not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "🍏 Tim Sehat"
    st.session_state.winner = None

# Fungsi Reset
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "🍏 Tim Sehat"
    st.session_state.winner = None

# Fungsi Cek Pemenang
def check_winner(b):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Baris
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Kolom
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for p in win_patterns:
        if b[p[0]] == b[p[1]] == b[p[2]] != "":
            return b[p[0]]
    if "" not in b:
        return "Seri"
    return None

# Tombol Reset
st.button("🔄 Ulangi Permainan", on_click=reset_game)

# Informasi Giliran atau Hasil Akhir
if st.session_state.winner is None:
    st.write(f"📢 Giliran saat ini: *{st.session_state.current_player}*")
else:
    if st.session_state.winner == "🍏 Tim Sehat":
        st.balloons()
        st.success("🎉 SELAMAT! Tim Sehat Menang! Tubuhmu terlindungi dari zat adiktif berbahaya!")
    elif st.session_state.winner == "💀 Tim Narkoba":
        st.error("🚨 BAHAYA! Tim Narkoba Berhasil Menguasai Sel Tubuh! Segera lakukan rehabilitasi sebelum terlambat!")
    else:
        st.warning("🤝 Hasil Seri! Pertahanan tubuhmu kuat, tapi ancaman narkoba tetap mengintai.")

st.write("---")

# Render Grid 3x3
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        cell_value = st.session_state.board[idx]
        
        # Penamaan label tombol agar tidak kosong secara visual
        label = cell_value if cell_value != "" else " "
        
        # Nonaktifkan tombol jika game sudah selesai atau kotak sudah terisi
        disabled = (cell_value != "" or st.session_state.winner is not None)
        
        if cols[col].button(label, key=f"cell_{idx}", disabled=disabled, use_container_width=True):
            # Isi papan
            st.session_state.board[idx] = st.session_state.current_player
            
            # Cek status kemenangan
            winner_check = check_winner(st.session_state.board)
            if winner_check:
                st.session_state.winner = winner_check
            else:
                # Ganti giliran pemain
                st.session_state.current_player = "💀 Tim Narkoba" if st.session_state.current_player == "🍏 Tim Sehat" else "🍏 Tim Sehat"
            
            st.rerun()

st.write("---")
st.info("💡 *Aturan Edukasi:* Tim Sehat (🍏) harus memblokir pergerakan Tim Narkoba (💀) agar tidak berhasil membentuk garis lurus 3 kotak. Jangan biarkan narkoba merusak sistem pertahanan tubuh!")
