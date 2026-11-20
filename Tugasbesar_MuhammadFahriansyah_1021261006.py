import streamlit as st
import base64
import os

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Laundry Kiloan",
    page_icon="⚡",
    layout="wide"
)

# =====================================================
# FUNGSI MEMBACA GAMBAR
# =====================================================

def image_to_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()

    return None


zenitsu1 = image_to_base64("zenitsu1.jpg")
zenitsu2 = image_to_base64("zenitsu2.jpg")


# =====================================================
# CSS / TAMPILAN / ANIMASI
# =====================================================

st.markdown("""
<style>

/* ================================
   BACKGROUND
================================ */

.stApp {
    background:
        radial-gradient(
            circle at 80% 20%,
            rgba(255, 193, 7, 0.18),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #050505 0%,
            #101010 50%,
            #251700 100%
        );

    color: white;
}


/* ================================
   CONTAINER
================================ */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
}


/* ================================
   JUDUL
================================ */

.title-box {
    text-align: center;
    margin-bottom: 25px;

    animation:
        glowTitle 2s ease-in-out infinite alternate;
}

.title {
    font-size: 44px;
    font-weight: 1000;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #ffd000,
            #ffffff,
            #ff9800
        );

    background-size: 300% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation:
        textMove 5s linear infinite;
}

.subtitle {
    color: #cccccc;
    font-size: 16px;
}


/* ================================
   ANIMASI JUDUL
================================ */

@keyframes textMove {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 300% center;
    }

}

@keyframes glowTitle {

    from {
        filter:
            drop-shadow(
                0 0 5px rgba(255,193,7,0.3)
            );
    }

    to {
        filter:
            drop-shadow(
                0 0 25px rgba(255,193,7,0.9)
            );
    }

}


/* ================================
   ZENITSU CONTAINER
================================ */

.zenitsu-container {

    position: relative;

    height: 560px;

    overflow: hidden;

    border-radius: 25px;

    border:
        2px solid rgba(255,193,7,0.55);

    background: #050505;

    box-shadow:
        0 0 35px rgba(255,193,7,0.25);

}


/* ================================
   GAMBAR BACKGROUND
================================ */

.zenitsu1 {

    position: absolute;

    width: 100%;
    height: 100%;

    object-fit: cover;

    opacity: 0.75;

    animation:
        zoomMove 8s ease-in-out infinite alternate;

}


/* ================================
   GAMBAR ZENITSU 2
================================ */

.zenitsu2 {

    position: absolute;

    width: 58%;

    max-height: 100%;

    right: -30px;

    bottom: -25px;

    object-fit: contain;

    filter:
        drop-shadow(
            0 0 15px rgba(255,193,7,0.8)
        );

    animation:
        floatZenitsu 3s ease-in-out infinite,
        glowZenitsu 1.5s ease-in-out infinite alternate;

}


/* ================================
   ZOOM BACKGROUND
================================ */

@keyframes zoomMove {

    0% {
        transform:
            scale(1)
            translateX(0px);
    }

    100% {
        transform:
            scale(1.12)
            translateX(-10px);
    }

}


/* ================================
   GERAK ZENITSU
================================ */

@keyframes floatZenitsu {

    0% {
        transform:
            translateY(0px);
    }

    50% {
        transform:
            translateY(-12px);
    }

    100% {
        transform:
            translateY(0px);
    }

}


/* ================================
   GLOW ZENITSU
================================ */

@keyframes glowZenitsu {

    from {
        filter:
            drop-shadow(
                0 0 10px rgba(255,193,7,0.4)
            );
    }

    to {
        filter:
            drop-shadow(
                0 0 35px rgba(255,193,7,1)
            );
    }

}


/* ================================
   EFEK PETIR
================================ */

.lightning {

    position: absolute;

    width: 100%;
    height: 100%;

    pointer-events: none;

    background:
        linear-gradient(
            115deg,
            transparent 20%,
            transparent 40%,
            rgba(255,193,7,0.55) 50%,
            transparent 60%,
            transparent 80%
        );

    background-size: 250% 250%;

    animation:
        lightningMove 3s linear infinite;

    mix-blend-mode: screen;

}


/* ================================
   ANIMASI PETIR
================================ */

@keyframes lightningMove {

    0% {
        opacity: 0;
        background-position: 100% 0%;
    }

    40% {
        opacity: 0;
    }

    45% {
        opacity: 1;
    }

    48% {
        opacity: 0.15;
    }

    50% {
        opacity: 1;
    }

    53% {
        opacity: 0.1;
    }

    60% {
        opacity: 0;
    }

    100% {
        background-position: 0% 100%;
        opacity: 0;
    }

}


/* ================================
   PARTIKEL
================================ */

.spark {

    position: absolute;

    width: 5px;
    height: 5px;

    background: #ffd000;

    border-radius: 50%;

    box-shadow:
        0 0 10px #ffd000,
        0 0 25px #ff9800;

    animation:
        sparkMove 2s infinite;

}

.spark1 {
    left: 15%;
    top: 30%;
    animation-delay: 0.2s;
}

.spark2 {
    left: 35%;
    top: 60%;
    animation-delay: 0.8s;
}

.spark3 {
    left: 65%;
    top: 25%;
    animation-delay: 1.2s;
}

.spark4 {
    left: 80%;
    top: 65%;
    animation-delay: 1.7s;
}


@keyframes sparkMove {

    0% {
        opacity: 0;
        transform:
            translateY(20px)
            scale(0.5);
    }

    50% {
        opacity: 1;
        transform:
            translateY(-20px)
            scale(1.5);
    }

    100% {
        opacity: 0;
        transform:
            translateY(-50px)
            scale(0.2);
    }

}


/* ================================
   PANEL
================================ */

.panel {

    background:
        rgba(15,15,15,0.88);

    border:
        1px solid rgba(255,193,7,0.4);

    border-radius: 20px;

    padding: 25px;

    box-shadow:
        0 0 25px rgba(255,193,7,0.1);

}


/* ================================
   INPUT
================================ */

.stTextInput input,
.stNumberInput input {

    background:
        #191919 !important;

    color:
        white !important;

    border:
        1px solid #555 !important;

    border-radius:
        10px !important;

}


/* ================================
   BUTTON
================================ */

.stButton button {

    width: 100%;

    border-radius: 12px;

    min-height: 48px;

    background:
        linear-gradient(
            135deg,
            #ffd000,
            #ff9800
        );

    color: black;

    font-weight: 900;

    border: none;

    transition: 0.2s;

}

.stButton button:hover {

    transform:
        translateY(-3px)
        scale(1.02);

    box-shadow:
        0 0 25px rgba(255,193,7,0.8);

}


/* ================================
   HASIL
================================ */

.result {

    background:
        linear-gradient(
            135deg,
            rgba(35,30,10,0.95),
            rgba(15,15,15,0.95)
        );

    border:
        1px solid rgba(255,193,7,0.45);

    border-radius:
        20px;

    padding:
        25px;

    animation:
        resultAppear 0.6s ease;

}


@keyframes resultAppear {

    from {
        opacity: 0;
        transform:
            translateY(20px);
    }

    to {
        opacity: 1;
        transform:
            translateY(0);
    }

}


/* ================================
   TOTAL
================================ */

.total {

    margin-top: 20px;

    padding: 20px;

    text-align: center;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            #ffd000,
            #ff9800
        );

    color: black;

    box-shadow:
        0 0 35px rgba(255,193,7,0.65);

    animation:
        totalPulse 1.5s infinite alternate;

}

@keyframes totalPulse {

    from {
        transform:
            scale(1);

        box-shadow:
            0 0 15px rgba(255,193,7,0.4);
    }

    to {
        transform:
            scale(1.02);

        box-shadow:
            0 0 40px rgba(255,193,7,0.9);
    }

}


/* ================================
   FOOTER
================================ */

.footer {

    text-align: center;

    color: #777;

    margin-top: 30px;

}

</style>
""", unsafe_allow_html=True)


# =====================================================
# JUDUL
# =====================================================

st.markdown("""
<div class="title-box">

<div class="title">
⚡ APLIKASI BIAYA LAUNDRY KILOAN ⚡
</div>

<div class="subtitle">
Hitung cepat biaya laundry dengan tema Thunder Zenitsu
</div>

</div>
""", unsafe_allow_html=True)


# =====================================================
# ANIMASI ZENITSU
# =====================================================

if zenitsu1 and zenitsu2:

    st.markdown(f"""
    <div class="zenitsu-container">

        <img
            class="zenitsu1"
            src="data:image/jpeg;base64,{zenitsu1}"
        >

        <div class="lightning"></div>

        <div class="spark spark1"></div>
        <div class="spark spark2"></div>
        <div class="spark spark3"></div>
        <div class="spark spark4"></div>

        <img
            class="zenitsu2"
            src="data:image/jpeg;base64,{zenitsu2}"
        >

    </div>
    """, unsafe_allow_html=True)

else:

    st.warning(
        "Gambar Zenitsu belum ditemukan. "
        "Pastikan zenitsu1.jpg dan zenitsu2.jpg "
        "berada di folder yang sama."
    )


st.write("")


# =====================================================
# FORM
# =====================================================

col1, col2 = st.columns(2)


# =====================================================
# INPUT DATA
# =====================================================

with col1:

    st.markdown("""
    <div class="panel">

    <h2 style="color:#ffd000;">
    ⚡ DATA LAUNDRY
    </h2>

    <p style="color:#aaa;">
    Masukkan NIM dan berat cucian.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    nim = st.text_input(
        "NIM (10 digit)",
        placeholder="Contoh: 1021261006"
    )

    # Dibuat bisa menerima negatif supaya
    # skenario validasi tugas bisa diuji.
    berat = st.number_input(
        "Berat Cucian (kg)",
        min_value=-1000,
        max_value=1000,
        value=0,
        step=1
    )

    st.write("")

    hitung = st.button(
        "⚡ HITUNG BIAYA",
        use_container_width=True
    )

    reset = st.button(
        "↻ RESET",
        use_container_width=True
    )


# =====================================================
# RESET
# =====================================================

if reset:
    st.rerun()


# =====================================================
# HASIL
# =====================================================

with col2:

    if hitung:

        # =============================================
        # VALIDASI NIM
        # =============================================

        if len(nim) != 10 or not nim.isdigit():

            st.error(
                "❌ NIM harus terdiri dari tepat 10 digit angka."
            )

        # =============================================
        # VALIDASI BERAT
        # =============================================

        elif berat <= 0:

            st.error(
                "❌ Berat cucian harus lebih dari 0 kg."
            )

        else:

            # =========================================
            # DATA NIM
            # =========================================

            digit_nim = [
                int(x)
                for x in nim
            ]

            digit_terakhir = digit_nim[-1]

            jumlah_digit_genap = sum(
                1
                for x in digit_nim
                if x % 2 == 0
            )

            # =========================================
            # RUMUS
            # =========================================

            tarif_per_kg = (
                5000 +
                (digit_terakhir * 500)
            )

            persen_diskon = (
                jumlah_digit_genap
            )

            biaya_normal = (
                int(berat) *
                tarif_per_kg
            )

            potongan = (
                persen_diskon *
                biaya_normal /
                100
            )

            total_bayar = (
                biaya_normal -
                potongan
            )

            # =========================================
            # FORMAT RUPIAH
            # =========================================

            def rupiah(nilai):

                return (
                    f"Rp {nilai:,.0f}"
                    .replace(",", ".")
                )

            # =========================================
            # TAMPILKAN HASIL
            # =========================================

            st.markdown(f"""
            <div class="result">

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
            <div class="total">

                <div style="font-size:16px;">
                    ⚡ TOTAL BAYAR
                </div>

                <div style="font-size:34px;font-weight:900;">
                    {rupiah(total_bayar)}
                </div>

            </div>
            """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result">

        <h2 style="color:#ffd000;">
        ⚡ RINCIAN PERHITUNGAN
        </h2>

        <p style="color:#999;">
        Hasil perhitungan akan muncul di sini
        setelah data dimasukkan.
        </p>

        <div style="
            text-align:center;
            font-size:80px;
            padding:40px;
        ">
        ⚡
        </div>

        </div>
        """, unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

⚡ Laundry Kiloan • Python + Streamlit ⚡<br>
NIM: 1021261006

</div>
""", unsafe_allow_html=True)
