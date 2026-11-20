import streamlit as st
import streamlit.components.v1 as components
import base64
import os


# =========================================================
# KONFIGURASI
# =========================================================

st.set_page_config(
    page_title="Aplikasi Biaya Laundry",
    page_icon="⚡",
    layout="wide"
)


# =========================================================
# FUNGSI MEMBACA GAMBAR
# =========================================================

def image_to_base64(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            return base64.b64encode(file.read()).decode()
    return None


zenitsu1 = image_to_base64("zenitsu1.jpg")
zenitsu2 = image_to_base64("zenitsu2.jpg")


# =========================================================
# CSS UNTUK STREAMLIT
# =========================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at 80% 20%,
            rgba(255,193,7,0.12),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #050505 0%,
            #111111 55%,
            #241700 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
}

.main-title {
    text-align: center;
    color: #ffd000;
    font-size: 42px;
    font-weight: 900;
    text-shadow:
        0 0 10px rgba(255,193,7,0.6),
        0 0 25px rgba(255,193,7,0.4);
}

.subtitle {
    text-align: center;
    color: #cccccc;
    margin-bottom: 20px;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(10,10,10,0.75);
    border: 1px solid rgba(255,193,7,0.45);
    border-radius: 18px;
}

.stButton button {
    border-radius: 12px;
    min-height: 45px;
    background: linear-gradient(
        135deg,
        #ffd000,
        #ff9800
    );
    color: black;
    font-weight: 900;
    border: none;
}

.stButton button:hover {
    box-shadow:
        0 0 25px rgba(255,193,7,0.8);
    transform: translateY(-2px);
}

.stTextInput input,
.stNumberInput input {
    background-color: #191919 !important;
    color: white !important;
    border-radius: 10px !important;
}

.footer {
    text-align: center;
    color: #777777;
    margin-top: 30px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# JUDUL
# =========================================================

st.markdown(
    '<div class="main-title">⚡ APLIKASI BIAYA LAUNDRY KILOAN ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Hitung cepat biaya laundry dengan tema Thunder Zenitsu</div>',
    unsafe_allow_html=True
)


# =========================================================
# ANIMASI ZENITSU
# =========================================================

if zenitsu1 and zenitsu2:

    html_zenitsu = f"""
<!DOCTYPE html>
<html>
<head>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 0;
    background: transparent;
    overflow: hidden;
}}

.scene {{
    position: relative;
    width: 100%;
    height: 560px;
    overflow: hidden;

    border-radius: 25px;

    border: 2px solid rgba(255,193,7,0.7);

    background: #030303;

    box-shadow:
        0 0 30px rgba(255,193,7,0.35);
}}

.background {{
    position: absolute;

    width: 100%;
    height: 100%;

    object-fit: cover;

    opacity: 0.72;

    animation:
        zoomBackground 8s ease-in-out infinite alternate;
}}

.zenitsu {{
    position: absolute;

    width: 58%;
    height: 100%;

    right: -20px;
    bottom: -20px;

    object-fit: contain;

    filter:
        drop-shadow(0 0 12px rgba(255,193,7,0.8))
        drop-shadow(0 0 30px rgba(255,170,0,0.5));

    animation:
        floatZenitsu 3s ease-in-out infinite,
        glowZenitsu 1.5s ease-in-out infinite alternate;
}}

@keyframes zoomBackground {{
    from {{
        transform: scale(1);
    }}

    to {{
        transform: scale(1.12);
    }}
}}

@keyframes floatZenitsu {{
    0% {{
        transform: translateY(0px);
    }}

    50% {{
        transform: translateY(-12px);
    }}

    100% {{
        transform: translateY(0px);
    }}
}}

@keyframes glowZenitsu {{
    from {{
        filter:
            drop-shadow(0 0 8px rgba(255,193,7,0.5));
    }}

    to {{
        filter:
            drop-shadow(0 0 35px rgba(255,193,7,1));
    }}
}}

.lightning {{
    position: absolute;

    top: 0;
    right: 12%;

    width: 5px;
    height: 100%;

    background:
        linear-gradient(
            to bottom,
            transparent,
            #ffd000,
            white,
            #ffd000,
            transparent
        );

    opacity: 0;

    transform: rotate(10deg);

    filter:
        drop-shadow(0 0 15px #ffd000);

    animation:
        lightningFlash 3.5s infinite;
}}

@keyframes lightningFlash {{

    0%, 38%, 45%, 100% {{
        opacity: 0;
    }}

    39% {{
        opacity: 1;
    }}

    40% {{
        opacity: 0.1;
    }}

    41% {{
        opacity: 1;
    }}

    43% {{
        opacity: 0.2;
    }}

    44% {{
        opacity: 1;
    }}
}}

.flash {{
    position: absolute;

    inset: 0;

    background:
        rgba(255,193,7,0.2);

    opacity: 0;

    animation:
        flashScreen 3.5s infinite;
}}

@keyframes flashScreen {{

    0%, 38%, 45%, 100% {{
        opacity: 0;
    }}

    39% {{
        opacity: 0.7;
    }}

    40% {{
        opacity: 0.1;
    }}

    41% {{
        opacity: 0.8;
    }}

    44% {{
        opacity: 0;
    }}
}}

.spark {{
    position: absolute;

    width: 5px;
    height: 5px;

    border-radius: 50%;

    background: #ffd000;

    box-shadow:
        0 0 10px #ffd000,
        0 0 20px #ff9800;

    animation:
        particleMove 2.5s infinite;
}}

.s1 {{
    left: 15%;
    top: 60%;
}}

.s2 {{
    left: 30%;
    top: 40%;
    animation-delay: 0.6s;
}}

.s3 {{
    left: 55%;
    top: 25%;
    animation-delay: 1.1s;
}}

.s4 {{
    left: 75%;
    top: 55%;
    animation-delay: 1.7s;
}}

.s5 {{
    left: 85%;
    top: 30%;
    animation-delay: 2.1s;
}}

@keyframes particleMove {{
    0% {{
        opacity: 0;
        transform: translateY(30px) scale(0.5);
    }}

    50% {{
        opacity: 1;
        transform: translateY(-20px) scale(1.3);
    }}

    100% {{
        opacity: 0;
        transform: translateY(-70px) scale(0.2);
    }}
}}

.overlay {{
    position: absolute;

    left: 25px;
    top: 25px;

    z-index: 10;

    color: white;

    text-shadow:
        0 0 10px black,
        0 0 20px black;
}}

.overlay h2 {{
    color: #ffd000;
    margin: 0;
    font-size: 26px;
}}

.overlay p {{
    margin-top: 8px;
    color: white;
    font-size: 14px;
}}

@media (max-width: 600px) {{

    .scene {{
        height: 470px;
    }}

    .zenitsu {{
        width: 75%;
        right: -25px;
    }}

    .overlay {{
        left: 18px;
        top: 18px;
    }}

    .overlay h2 {{
        font-size: 20px;
    }}

    .overlay p {{
        font-size: 12px;
    }}
}}

</style>

</head>

<body>

<div class="scene">

<img
class="background"
src="data:image/jpeg;base64,{zenitsu1}"
>

<div class="flash"></div>

<div class="lightning"></div>

<div class="spark s1"></div>
<div class="spark s2"></div>
<div class="spark s3"></div>
<div class="spark s4"></div>
<div class="spark s5"></div>

<img
class="zenitsu"
src="data:image/jpeg;base64,{zenitsu2}"
>

<div class="overlay">

<h2>⚡ THUNDER LAUNDRY ⚡</h2>

<p>
Perhitungan biaya laundry dengan kekuatan petir
</p>

</div>

</div>

</body>
</html>
"""

    components.html(
        html_zenitsu,
        height=580,
        scrolling=False
    )

else:

    st.error(
        "Gambar Zenitsu tidak ditemukan."
    )


# =========================================================
# DATA LAUNDRY
# =========================================================

st.write("")

kolom1, kolom2 = st.columns(2)


# =========================================================
# INPUT
# =========================================================

with kolom1:

    with st.container(border=True):

        st.subheader("⚡ DATA LAUNDRY")

        st.caption(
            "Masukkan NIM dan berat cucian."
        )

        nim = st.text_input(
            "NIM (10 digit)",
            placeholder="Contoh: 1021261006"
        )

        berat = st.number_input(
            "Berat Cucian (kg)",
            min_value=-1000,
            max_value=1000,
            value=0,
            step=1
        )

        tombol1, tombol2 = st.columns(2)

        with tombol1:

            hitung = st.button(
                "⚡ HITUNG",
                use_container_width=True
            )

        with tombol2:

            reset = st.button(
                "↻ RESET",
                use_container_width=True
            )


# =========================================================
# RESET
# =========================================================

if reset:
    st.rerun()


# =========================================================
# HASIL
# =========================================================

with kolom2:

    with st.container(border=True):

        st.subheader("⚡ RINCIAN PERHITUNGAN")

        if hitung:

            # ---------------------------------------------
            # VALIDASI NIM
            # ---------------------------------------------

            if len(nim) != 10 or not nim.isdigit():

                st.error(
                    "❌ NIM harus terdiri dari tepat 10 digit angka."
                )

            # ---------------------------------------------
            # VALIDASI BERAT
            # ---------------------------------------------

            elif berat <= 0:

                st.error(
                    "❌ Berat cucian harus lebih dari 0 kg."
                )

            else:

                # -----------------------------------------
                # DIGIT TERAKHIR
                # -----------------------------------------

                digit_terakhir = int(
                    nim[-1]
                )

                # -----------------------------------------
                # JUMLAH DIGIT GENAP
                # -----------------------------------------

                jumlah_digit_genap = 0

                for digit in nim:

                    if int(digit) % 2 == 0:
                        jumlah_digit_genap += 1

                # -----------------------------------------
                # TARIF
                # -----------------------------------------

                tarif_per_kg = (
                    5000 +
                    digit_terakhir * 500
                )

                # -----------------------------------------
                # DISKON
                # -----------------------------------------

                persen_diskon = (
                    jumlah_digit_genap
                )

                # -----------------------------------------
                # BIAYA NORMAL
                # -----------------------------------------

                biaya_normal = (
                    berat *
                    tarif_per_kg
                )

                # -----------------------------------------
                # POTONGAN
                # -----------------------------------------

                potongan = (
                    biaya_normal *
                    persen_diskon /
                    100
                )

                # -----------------------------------------
                # TOTAL
                # -----------------------------------------

                total_bayar = (
                    biaya_normal -
                    potongan
                )

                # -----------------------------------------
                # FORMAT RUPIAH
                # -----------------------------------------

                def rupiah(nilai):

                    return (
                        "Rp "
                        + f"{nilai:,.0f}"
                        .replace(",", ".")
                    )

                # -----------------------------------------
                # HASIL
                # -----------------------------------------

                st.success(
                    "Perhitungan berhasil!"
                )

                st.write(
                    f"**NIM:** {nim}"
                )

                st.write(
                    f"**Berat cucian:** {int(berat)} kg"
                )

                st.divider()

                st.write(
                    f"💰 **Tarif per kg:** "
                    f"{rupiah(tarif_per_kg)}"
                )

                st.write(
                    f"🔢 **Jumlah digit genap:** "
                    f"{jumlah_digit_genap} digit"
                )

                st.write(
                    f"⚡ **Diskon:** "
                    f"{persen_diskon}%"
                )

                st.write(
                    f"💵 **Biaya normal:** "
                    f"{rupiah(biaya_normal)}"
                )

                st.write(
                    f"✂️ **Potongan:** "
                    f"{rupiah(potongan)}"
                )

                st.markdown(
                    f"""
**⚡ TOTAL BAYAR**

# {rupiah(total_bayar)}
"""
                )

        else:

            st.info(
                "Masukkan NIM dan berat cucian, "
                "kemudian tekan tombol HITUNG."
            )

            st.write("")

            st.markdown(
                """
<div style="text-align:center;font-size:70px;">
⚡
</div>
""",
                unsafe_allow_html=True
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div class="footer">
⚡ Laundry Kiloan • Python + Streamlit ⚡<br>
NIM: 1021261006
</div>
""",
    unsafe_allow_html=True
)
