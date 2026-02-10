import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para esconder menus do Streamlit
st.set_page_config(page_title="Para Minha Princesa", layout="centered")

html_completo = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');

        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(45deg, #0f0c29, #302b63, #24243e);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        canvas { position: fixed; top: 0; left: 0; z-index: 1; pointer-events: none; }

        .container { z-index: 10; display: flex; flex-direction: column; align-items: center; }

        /* Envelope */
        .envelope-wrapper {
            position: relative;
            width: 320px;
            height: 220px;
            background: #ff4d6d;
            border-radius: 0 0 15px 15px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.5);
            cursor: pointer;
        }

        .lid {
            position: absolute;
            top: 0; left: 0;
            border-top: 120px solid #c9184a;
            border-left: 160px solid transparent;
            border-right: 160px solid transparent;
            transform-origin: top;
            transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 3;
        }

        .letter {
            position: absolute;
            bottom: 10px; left: 10px;
            width: 300px;
            height: 190px;
            background: #fff;
            border-radius: 10px;
            padding: 20px;
            box-sizing: border-box;
            transition: 0.8s;
            z-index: 2;
            color: #333;
            text-align: center;
        }

        .letter h1 { font-family: 'Dancing Script', cursive; color: #ff0050; margin: 0; font-size: 1.5rem; }
        .letter p { font-size: 0.85rem; margin: 10px 0; }
        .poesia { font-style: italic; color: #ff0050; font-weight: 600; margin-top: 15px !important; }

        /* Animação Abrir */
        .envelope-wrapper.open .lid { transform: rotateX(180deg); z-index: 0; }
        .envelope-wrapper.open .letter { transform: translateY(-150px); height: 320px; z-index: 5; }

        .btn-abrir {
            margin-top: 80px;
            background: #ff0050;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 50px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 10px 20px rgba(255, 0, 80, 0.4);
            transition: 0.3s;
        }

        /* Player discreto */
        .music-player { margin-top: 15px; }
    </style>
</head>
<body>
    <canvas id="hearts"></canvas>

    <div class="container">
        <div class="envelope-wrapper" id="env">
            <div class="lid"></div>
            <div class="letter">
                <h1>Para minha Pequenina...</h1>
                <p>Minha <b>Princesa</b>, você é a pessoa mais especial da minha vida. Cada momento contigo é único. ❤️</p>
                <p class="poesia">"Cada vez que eu olho nos seus olho me espelho, cê sabe, né?"</p>
                
                <div class="music-player">
                    <iframe width="100%" height="60" src="https://www.youtube.com/embed/69K_m4sN_7M?start=395" frameborder="0" allow="autoplay"></iframe>
                </div>
            </div>
        </div>
        <button class="btn-abrir" onclick="document.getElementById('env').classList.toggle('open')">Clique aqui ❤️</button>
    </div>

    <script>
        const canvas = document.getElementById('hearts');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        let hearts = [];

        class Heart {
            constructor() { this.reset(); }
            reset() {
                this.x = Math.random() * canvas.width;
                this.y = canvas.height + 20;
                this.size = Math.random() * 12 + 8;
                this.speed = Math.random() * 1.5 + 0.5;
                this.opacity = Math.random() * 0.4;
            }
            update() { this.y -= this.speed; if (this.y < -20) this.reset(); }
            draw() {
                ctx.fillStyle = `rgba(255, 77, 109, ${this.opacity})`;
                ctx.font = `${this.size}px Arial`;
                ctx.fillText('❤️', this.x, this.y);
            }
        }

        for (let i = 0; i < 40; i++) hearts.push(new Heart());

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            hearts.forEach(h => { h.update(); h.draw(); });
            requestAnimationFrame(animate);
        }
        animate();
    </script>
</body>
</html>
"""

components.html(html_completo, height=700)
