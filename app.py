import streamlit as st
import streamlit.components.v1 as components

# Configuração para o site ocupar a tela toda
st.set_page_config(page_title="Para Minha Pequenina", layout="wide")

# Link da música (Poesia 6 - Parte do Orochi)
musica_url = "https://www.youtube.com/embed/m0py2-J6TN4?autoplay=1&start=395"

# Código HTML/JS/CSS tudo junto
codigo_do_site = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&family=Dancing+Script:wght@700&display=swap');
        
        body {{
            margin: 0;
            background: #0a0a0a;
            color: white;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        canvas {{ position: fixed; top: 0; left: 0; z-index: -1; }}

        .main {{
            text-align: center;
            display: none; /* Escondido até o clique */
            flex-direction: column;
            align-items: center;
            gap: 20px;
            z-index: 10;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            width: 350px;
            box-shadow: 0 10px 30px rgba(255, 0, 80, 0.2);
        }}

        .title {{ font-family: 'Dancing Script', cursive; color: #ff0050; font-size: 2rem; margin: 0; }}
        
        .btn-clique {{
            background: #ff0050;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-weight: bold;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(255, 0, 80, 0.6);
        }}

        iframe {{ border-radius: 15px; margin-top: 10px; }}
    </style>
</head>
<body>
    <canvas id="stars"></canvas>

    <button id="btnInit" class="btn-clique" onclick="iniciar()">Clique aqui ❤️</button>

    <div id="conteudo" class="main">
        <div class="card">
            <h1 class="title">Minha Pequenina</h1>
            <p>Minha <b>Princesa</b>, você é o motivo do meu sorriso e a razão da minha felicidade. Te amo além das palavras! ❤️</p>
        </div>

        <div class="card">
            <h1 class="title">Poesia Acústica #6</h1>
            <p>"Cada vez que eu olho nos seus olho me espelho, cê sabe, né?"</p>
            <iframe width="100%" height="80" src="{musica_url}" frameborder="0" allow="autoplay"></iframe>
        </div>
    </div>

    <script>
        function iniciar() {{
            document.getElementById('btnInit').style.display = 'none';
            document.getElementById('conteudo').style.display = 'flex';
        }}

        // Animação das estrelas no fundo
        const canvas = document.getElementById('stars');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        let particles = [];

        class Particle {{
            constructor() {{
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2;
                this.speedY = Math.random() * 0.5;
                this.opacity = Math.random();
            }}
            update() {{
                this.y -= this.speedY;
                if (this.y < 0) this.y = canvas.height;
            }}
            draw() {{
                ctx.fillStyle = "rgba(255, 255, 255, " + this.opacity + ")";
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }}
        }}

        for(let i=0; i<100; i++) particles.push(new Particle());

        function animate() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {{ p.update(); p.draw(); }});
            requestAnimationFrame(animate);
        }}
        animate();
    </script>
</body>
</html>
"""

# Comando que faz o Streamlit mostrar o seu site de verdade
components.html(codigo_do_site, height=800)
