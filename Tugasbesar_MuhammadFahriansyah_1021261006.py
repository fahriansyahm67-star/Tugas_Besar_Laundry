import streamlit as st
import streamlit.components.v1 as components
import base64
import os


# =========================================================
# KONFIGURASI HALAMAN
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
# CSS STREAMLIT
# =========================================================

st.markdown("""
<style>

/* ==============================
   BACKGROUND APLIKASI
============================== */

.stApp {
    background:
        radial-gradient(
            circle at 80% 20%,
            rgba(255, 193, 7, 0.15),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #050505 0%,
            #111111 50%,
            #241700 100%
        );

    color: white;
}


/* ==============================
   CONTAINER
============================== */

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}


/* ==============================
   JUDUL
============================== */

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;

    color: #ffd000;

    text-shadow:
        0 0 10px rgba(255, 193, 7, 0.7),
        0 0 25px rgba(255, 193, 7, 0.4);

    animation: titleGlow 2s infinite alternate;
}

.subtitle {
    text-align: center;
    color: #dddddd;
    font-size: 16px;
    margin-bottom: 20px;
}

@keyframes titleGlow {
    from {
        text-shadow:
            0 0 8px rgba(255, 193, 7, 0.4);
    }

    to {
        text-shadow:
            0 0 30px rgba(255, 193, 7, 1);
    }
}


/* ==============================
   PANEL DATA
============================== */

.data-panel {
    background:
        rgba(10, 10, 10, 0.85);

    border:
        1px solid rgba(255, 193, 7, 0.5);

    border-radius: 20px;

    padding: 25px;

    box-shadow:
        0 0 25px rgba(255, 193, 7, 0.12);

    margin-bottom: 15px;
}


/* ==============================
   INPUT
============================== */

.stTextInput input,
.stNumberInput input {

    background-color: #191919 !important;

    color: white !important;

    border:
        1px solid #555 !important;

    border-radius: 10px !important;
}


/* ==============================
   BUTTON
============================== */

.stButton button {

    width: 100%;

    min-height: 45px;

    border-radius: 12px;

    border: none;

    background:
        linear-gradient(
            135deg,
            #ffd000,
            #ff9800
        );

    color: #000000;

    font-weight: 900;

    transition:
        all 0.2s ease;
}


.stButton button:hover {

    transform:
        translateY(-3px)
        scale(1.02);

    box-shadow:
        0 0 25px rgba(255, 193, 7, 0.8);
}


/* ==============================
   HASIL
============================== */

.result-panel {

    background:
        rgba(10, 10, 10, 0.9);

    border:
        1px solid rgba(255, 193, 7, 0.5);

    border-radius: 20px;

    padding: 25px;

    box-shadow:
        0 0 25px rgba(255, 193, 7, 0.12);
}


/* ==============================
   TOTAL BAYAR
============================== */

.total-box {

    margin-top: 20px;

    padding: 20px;

    border-radius: 18px;

    text-align: center;

    background:
        linear-gradient(
            135deg,
            #ffd000,
            #ff9800
        );

    color: black;

    box-shadow:
        0 0 30px rgba(255, 193, 7, 0.7);

    animation:
        totalPulse 1.5s infinite alternate;
}

@keyframes totalPulse {

    from {
        transform: scale(1);
        box-shadow:
            0 0 15px rgba(255, 193, 7, 0.4);
    }

    to {
        transform: scale(1.02);
        box-shadow:
            0 0 40px rgba(255, 193, 7, 0.9);
    }
}


/* ==============================
   FOOTER
============================== */

.footer {
    text-align: center;
    color: #777777;
    margin-top: 30px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# JUDUL
# =========================================================

st.markdown("""
<div class="main-title">
⚡ APLIKASI BIAYA LAUNDRY KILOAN ⚡
</div>

<div class="subtitle">
Hitung cepat biaya laundry dengan tema Thunder Zenitsu
</div>
""", unsafe_allow_html=True)


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

    border: 2px solid rgba(255, 193, 7, 0.65);

    background: #030303;

    box-shadow:
        0 0 25px rgba(255, 193, 7, 0.3),
        inset 0 0 40px rgba(255, 193, 7, 0.08);
}}


/* =================================
   BACKGROUND ZENITSU
================================= */

.background {{
    position: absolute;

    width: 100%;
    height: 100%;

    object-fit: cover;

    opacity: 0.72;

    transform: scale(1.02);

    animation:
        backgroundMove 8s ease-in-out infinite alternate;
}}


@keyframes backgroundMove {{

    0% {{
        transform:
            scale(1.02)
            translateX(0px);
    }}

    100% {{
        transform:
            scale(1.12)
            translateX(-15px);
    }}

}}


/* =================================
   ZENITSU DEPAN
================================= */

.zenitsu {{
    position: absolute;

    width: 55%;

    height: 100%;

    right: -10px;

    bottom: -20px;

    object-fit: contain;

    filter:
        drop-shadow(
            0 0 12px rgba(255, 193, 7, 0.7)
        )
        drop-shadow(
            0 0 30px rgba(255, 170, 0, 0.4)
        );

    animation:
        zenitsuFloat 3s ease-in-out infinite,
        zenitsuGlow 1.5s ease-in-out infinite alternate;

}}


@keyframes zenitsuFloat {{

    0% {{
        transform:
            translateY(0px);
    }}

    50% {{
        transform:
            translateY(-12px);
    }}

    100% {{
        transform:
            translateY(0px);
    }}

}}


@keyframes zenitsuGlow {{

    0% {{
        filter:
            drop-shadow(
                0 0 8px rgba(255, 193, 7, 0.5)
            );
    }}

    100% {{
        filter:
            drop-shadow(
                0 0 35px rgba(255, 193, 7, 1)
            );
    }}

}}


/* =================================
   PETIR
================================= */

.lightning {{
    position: absolute;

    top: 0;
    right: 10%;

    width: 4px;
    height: 100%;

    background:
        linear-gradient(
            to bottom,
            transparent 0%,
            #ffd000 25%,
            #ffffff 45%,
            #ffd000 60%,
            transparent 100%
        );

    opacity: 0;

    filter:
        blur(1px)
        drop-shadow(
            0 0 12px #ffd000
        );

    transform:
        rotate(12deg);

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


/* =================================
   CAHAYA PETIR
================================= */

.flash {{
    position: absolute;

    inset: 0;

    background:
        rgba(255, 193, 7, 0.18);

    opacity: 0;

    animation:
        screenFlash 3.5s infinite;
}}


@keyframes screenFlash {{

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


/* =================================
   PARTIKEL
================================= */

.spark {{
    position: absolute;

    width: 5px;
    height: 5px;

    border-radius: 50%;

    background: #ffd000;

    box-shadow:
        0 0 8px #ffd000,
        0 0 20px #ff9800;

    opacity: 0;

    animation:
        sparkMove 2.5s infinite;
}}


.spark1 {{
    left: 12%;
    top: 65%;
    animation-delay: 0.1s;
}}

.spark2 {{
    left: 30%;
    top: 40%;
    animation-delay: 0.7s;
}}

.spark3 {{
    left: 55%;
    top: 25%;
    animation-delay: 1.3s;
}}

.spark4 {{
    left: 80%;
    top: 50%;
    animation-delay: 1.8s;
}}

.spark5 {{
    left: 72%;
    top: 75%;
    animation-delay: 2.1s;
}}


@keyframes sparkMove {{

    0% {{
        opacity: 0;
        transform:
            translateY(30px)
            scale(0.5);
    }}

    40% {{
        opacity: 1;
    }}

    70% {{
        opacity: 1;
        transform:
            translateY(-30px)
            scale(1.4);
    }}

    100% {{
        opacity: 0;
        transform:
            translateY(-70px)
            scale(0.2);
    }}

}}


/* =================================
   TEKS DI ATAS GAMBAR
================================= */

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
    margin: 0;

    color: #ffd000;

    font-size: 27px;
}}

.overlay p {{
    margin-top: 7px;

    color: #eeeeee;

    font-size: 14px;
}}


/* =================================
   RESPONSIVE HP
================================= */

@media (max-width: 600px) {{

    .scene {{
        height: 470px;
    }}

    .zenitsu {{
        width: 72%;
        right: -20px;
    }}

    .overlay {{
        left: 18px;
        top: 18px;
    }}

    .overlay h2 {{
        font-size: 21px;
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

    <div class="spark spark1"></div>
    <div class="spark spark2"></div>
    <div class="spark spark3"></div>
    <div class="spark spark4"></div>
    <div class="spark spark5"></div>

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
        "Gambar Zenitsu tidak ditemukan. "
        "Pastikan zenitsu1.jpg dan zenitsu2.jpg "
        "berada di repository yang sama dengan file Python."
    )


# =========================================================
# JARAK
# =========================================================

st.write("")


# =========================================================
# FUNGSI RESET
# =========================================================

def reset_form():
    st.session_state.nim = ""
    st.session_state.berat = 0


# =========================================================
# LAYOUT DATA
# =========================================================

kolom1, kolom2 = st.columns(2)


# =========================================================
# INPUT DATA
# =========================================================

with kolom1:

    st.markdown("""
    <div class="data-panel">

        <h2 style="color:#ffd000;">
            ⚡ DATA LAUNDRY
        </h2>

        <p style="color:#aaaaaa;">
            Masukkan NIM dan berat cucian.
        </p>

    </div>
    """, unsafe_allow_html=True)

    nim = st.text_input(
        "NIM (10 digit)",
        placeholder="Contoh: 1021261006",
        key="nim"
    )

    berat = st.number_input(
        "Berat Cucian (kg)",
        min_value=-1000,
        max_value=1000,
        value=0,
        step=1,
        key="berat"
    )

    st.write("")

    tombol1, tombol2 = st.columns(2)

    with tombol1:

        hitung = st.button(
            "⚡ HITUNG",
            use_container_width=True
        )

    with tombol2:

        st.button(
            "↻ RESET",
            use_container_width=True,
            on_click=reset_form
        )


# =========================================================
# FUNGSI FORMAT RUPIAH
# =========================================================

def rupiah(nilai):

    return (
        "Rp "
        + f"{nilai:,.0f}".replace(",", ".")
    )


# =========================================================
# HASIL PERHITUNGAN
# =========================================================

with kolom2:

    if hitung:

        # -----------------------------------------------
        # VALIDASI NIM
        # -----------------------------------------------

        if len(nim) != 10 or not nim.isdigit():

            st.error(
                "❌ NIM harus terdiri dari tepat 10 digit angka."
            )

        # -----------------------------------------------
        # VALIDASI BERAT
        # -----------------------------------------------

        elif berat <= 0:

            st.error(
                "❌ Berat cucian harus lebih dari 0 kg."
            )

        else:

            # -------------------------------------------
            # MENGHITUNG DIGIT
            # -------------------------------------------

            digit_terakhir = int(nim[-1])

            jumlah_digit_genap = 0

            for digit in nim:

                if int(digit) % 2 == 0:

                    jumlah_digit_genap += 1


            # -------------------------------------------
            # TARIF PER KG
            # -------------------------------------------

            tarif_per_kg = (
                5000 +
                (digit_terakhir * 500)
            )


            # -------------------------------------------
            # PERSEN DISKON
            # -------------------------------------------

            persen_diskon = jumlah_digit_genap


            # -------------------------------------------
            # BIAYA NORMAL
            # -------------------------------------------

            biaya_normal = (
                berat * tarif_per_kg
            )


            # -------------------------------------------
            # POTONGAN
            # -------------------------------------------

            potongan = (
                persen_diskon *
                biaya_normal /
                100
            )


            # -------------------------------------------
            # TOTAL BAYAR
            # -------------------------------------------

            total_bayar = (
                biaya_normal -
                potongan
            )


            # -------------------------------------------
            # TAMPILKAN HASIL
            # -------------------------------------------

            st.markdown(f"""
            <div class="result-panel">

                <h2 style="color:#ffd000;">
                    ⚡ RINCIAN PERHITUNGAN
                </h2>

                <p>
                    <b>NIM:</b> {nim}
                </p>

                <p>
                    <b>Berat cucian:</b>
                    {int(berat)} kg
                </p>

                <hr>

                <p>
                    💰 <b>Tarif per kg:</b>
                    {rupiah(tarif_per_kg)}
                </p>

                <p>
                    🔢 <b>Jumlah digit genap:</b>
                    {jumlah_digit_genap} digit
                </p>

                <p>
                    ⚡ <b>Diskon:</b>
                    {persen_diskon}%
                </p>

                <p>
                    💵 <b>Biaya normal:</b>
                    {rupiah(biaya_normal)}
                </p>

                <p>
                    ✂️ <b>Potongan:</b>
                    {rupiah(potongan)}
                </p>

            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="total-box">

                <div style="font-size:16px;">
                    ⚡ TOTAL BAYAR
                </div>

                <div style="
                    font-size:32px;
                    font-weight:900;
                    margin-top:5px;
                ">
                    {rupiah(total_bayar)}
                </div>

            </div>
            """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-panel">

            <h2 style="color:#ffd000;">
                ⚡ RINCIAN PERHITUNGAN
            </h2>

            <p style="color:#999999;">
                Masukkan NIM dan berat cucian,
                kemudian tekan tombol HITUNG.
            </p>

            <div style="
                text-align:center;
                font-size:75px;
                padding:35px 0;
            ">
                ⚡
            </div>

        </div>
        """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

⚡ Laundry Kiloan • Python + Streamlit ⚡<br>
NIM: 1021261006

</div>
""", unsafe_allow_html=True) 
