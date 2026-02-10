import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ficar limpa
st.set_page_config(page_title="Para Minha Princesa", layout="centered")

# O código HTML/JS/CSS que eu fiz para você, encapsulado para o Streamlit
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        :root {
            --bg: #0a0a0a;
            --envelope-color: #ff4d6d;
            --lid-color: #c9184a;
            --letter-bg: #ffffff;
            --accent: #ff0050;
        }

        body {
            margin: 0;
            background: var(--bg);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            font-family: 'Arial', sans-serif;
        }

        canvas { position: fixed; top: 0; left: 0; z-index: -1; }

        .envelope-wrapper {
            position: relative;
            width: 300px;
            height: 200px;
            background: var(--envelope-color);
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        }

        .lid {
            position: absolute;
            top: 0; left: 0;
            border-top: 110px solid var(--lid-color);
            border-left: 150px solid transparent;
            border-right: 150px solid transparent;
            transform-origin: top;
            transition: transform 0.6s ease;
            z-index: 3;
        }

        .letter {
            position: absolute;
            top: 10px; left: 15px;
            width: 270px;
            height: 180px;
            background: var(--letter-bg);
            border-radius: 5px;
            padding: 20px;
            box-sizing: border-box;
            transition: transform 0.6s ease;
            z-index: 1;
            text-align: center;
        }

        .envelope-wrapper.open .lid { transform: rotateX(180deg); }
        .envelope-wrapper.open .letter { transform: translateY(-130px); height: 280px; z-index: 4; }

        .btn-abrir {
            margin-top: 50px;
            padding: 12px 25px;
            background: var(--accent);
            color: white;
            border: none;
            border-radius: 50px;
            font-weight: bold;
            cursor: pointer;
            z-index: 10;
        }
    </style>
</head>
<body>
    <canvas id="heartCanvas"></canvas>
    <div class="envelope-wrapper" id="env">
        <div class="lid"></div>
        <div class="letter">
            <p style="color: #ff0050; font-style: italic; font-size: 13px;">"Cada vez que eu olho nos seus olho me espelho, cê sabe, né?"</p>
            <p style="color: #333;">Para minha <b>Pequenina</b>,<br>minha <b>Princesa</b>.<br><br>Te amo demais! ❤️</p>
        </div>
    </div>
    <button class="btn-abrir" onclick="document.getElementById('env').classList.toggle('open')">Clique aqui ❤️</button>

    <script>
        const canvas = document.getElementById('heartCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        let hearts = [];
        class Heart {
            constructor() { this.reset(); }
            reset() {
                this.x = Math.random() * canvas.width;
                this.y = canvas.height + 20;
                this.size = Math.random() * 15 + 10;
                this.speed = Math.random() * 2 + 1;
                this.opacity = Math.random() * 0.5;
            }
            update() { this.y -= this.speed; if (this.y < -20) this.reset(); }
            draw() {
                ctx.fillStyle = `rgba(255, 0, 80, ${this.opacity})`;
                ctx.font = `${this.size}px Arial`;
                ctx.fillText('❤️', this.x, this.y);
            }
        }
        for (let i = 0; i < 30; i++) hearts.push(new Heart());
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

# Renderiza o HTML dentro do Streamlit
components.html(html_code, height=600)
