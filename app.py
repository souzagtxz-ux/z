import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para remover margens e menus do Streamlit
st.set_page_config(page_title="Para Minha Princesa", layout="wide")

# Ocultar o cabeçalho e rodapé padrão do Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Link da música Poesia Acústica #6 (Orochi - a parte que você pediu)
# Inicia em 395 segundos (6 minutos e 35 segundos) para o trecho do Orochi
musica_url = "https://www.youtube.com/embed/m0py2-J6TN4?autoplay=1&start=395&controls=0&mute=0"


html_completo = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Para Minha Princesa</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(45deg, #0f0c29, #302b63, #24243e);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            font-family: 'Poppins', sans-serif;
            color: #fff;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}

        @keyframes gradientBG {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        /* Efeito de Corações Flutuantes (agora são pontos brilhantes para combinar com o fundo) */
        canvas {{
            position: fixed;
            top: 0;
            left: 0;
            z-index: 1;
            pointer-events: none;
        }}

        .main-container {{
            position: relative;
            z-index: 10;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 30px; /* Espaçamento entre os elementos */
            padding: 40px 20px;
            max-width: 900px;
            width: 100%;
            opacity: 0; /* Começa invisível */
            transform: translateY(20px);
            animation: fadeIn 1s forwards;
            animation-delay: 1s; /* Atraso para aparecer depois do "Clique aqui" */
        }}
        
        @keyframes fadeIn {{
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .content-hidden {{
            display: none; /* Esconde o conteúdo inicial */
            flex-direction: column;
            align-items: center;
            gap: 30px;
            width: 100%;
        }}

        .cards-row {{
            display: flex;
            justify-content: center;
            gap: 25px;
            width: 100%;
            flex-wrap: wrap; /* Quebra linha em telas pequenas */
        }}

        .card {{
            background: rgba(255, 255, 255, 0.08); /* Fundo com transparência */
            backdrop-filter: blur(10px); /* Efeito de vidro fosco */
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            max-width: 380px;
            width: 100%;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: pulseCard 3s infinite ease-in-out;
            min-height: 150px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

        .card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(255, 0, 80, 0.3);
        }}

        @keyframes pulseCard {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.02); }}
        }}

        .card-title {{
            font-family: 'Dancing Script', cursive;
            color: #ff0050;
            font-size: 1.8rem;
            margin-bottom: 15px;
            text-shadow: 0 0 10px rgba(255, 0, 80, 0.5);
        }}

        .card-text {{
            font-size: 1rem;
            line-height: 1.6;
            color: #e0e0e0;
        }}

        .highlight {{ color: #ff0050; font-weight: 700; }}

        /* Player de Música */
        .music-player-container {{
            width: 100%;
            max-width: 450px;
            margin-top: 30px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(8px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            overflow: hidden; /* Garante que o iframe não escape */
        }}
        .music-player-container iframe {{
            width: 100%;
            height: 80px; /* Altura menor para o player discreto */
            border-radius: 10px;
        }}

        /* Botão Inicial "Clique aqui" */
        #initial-button-wrapper {{
            position: absolute;
            z-index: 100;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100vw;
            height: 100vh;
            background: rgba(0,0,0,0.8); /* Fundo escuro para destacar o botão */
            transition: opacity 0.5s ease;
        }}

        #initial-button {{
            background: #ff0050;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-weight: 700;
            font-size: 1.3rem;
            cursor: pointer;
            box-shadow: 0 0 25px rgba(255, 0, 80, 0.6);
            animation: pulsate 2s infinite;
        }}
        #initial-button:hover {{
            transform: scale(1.05);
            background: #ff4d6d;
        }}
        @keyframes pulsate {{
            0% {{ box-shadow: 0 0 20px rgba(255, 0, 80, 0.4); }}
            50% {{ box-shadow: 0 0 40px rgba(255, 0, 80, 0.8); }}
            100% {{ box-shadow: 0 0 20px rgba(255, 0, 80, 0.4); }}
        }}

        @media (max-width: 768px) {{
            .cards-row {{ flex-direction: column; align-items: center; }}
            .card {{ max-width: 90%; }}
            .card-title {{ font-size: 1.5rem; }}
            .card-text {{ font-size: 0.9rem; }}
        }}
    </style>
</head>
<body>
    <canvas id="starCanvas"></canvas>

    <div id="initial-button-wrapper">
        <button id="initial-button" onclick="startExperience()">Clique aqui ❤️</button>
    </div>

    <div class="main-container" id="mainContent">
        <div class="cards-row">
            <div class="card">
                <h2 class="card-title">Minha Pequenina ❤️</h2>
                <p class="card-text">
                    Para minha <span class="highlight">Princesa</span>, você é o motivo do meu sorriso e a razão mais que me faz feliz! Te amo mais que tudo.
                </p>
            </div>

            <div class="card">
                <h2 class="card-title">Poesia Acústica #6</h2>
                <p class="card-text">
                    "Cada vez que eu olho nos seus olho<br>Me espelho, cê sabe, né?"
                </p>
            </div>
        </div>
        
        <div class="music-player-container">
            <iframe src="{musica_url}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        </div>
    </div>

    <script>
        // JS para o botão inicial e mostrar o conteúdo
        function startExperience() {{
            document.getElementById('initial-button-wrapper').style.opacity = '0';
            setTimeout(() => {{
                document.getElementById('initial-button-wrapper').style.display = 'none';
                document.getElementById('mainContent').style.opacity = '1';
                document.getElementById('mainContent').style.transform = 'translateY(0)';
            }}, 500);
            
            // Tenta dar play na música automaticamente
            // Note: Navegadores modernos podem bloquear autoplay sem interação prévia.
            // O iframe com autoplay=1 já é a melhor tentativa.
        }}

        // JS para o efeito de estrelas/corações no fundo
        const canvas = document.getElementById('starCanvas');
        const ctx = canvas.getContext('2d');
        let particles = [];

        function resizeCanvas() {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }}
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        class Particle {{
            constructor() {{
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2 + 1; // Pequenos pontos brilhantes
                this.speedX = (Math.random() - 0.5) * 0.5;
                this.speedY = (Math.random() - 0.5) * 0.5;
                this.opacity = Math.random() * 0.7 + 0.3;
            }}
            update() {{
                this.x += this.speedX;
                this.y += this.speedY;

                if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
                if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
            }}
            draw() {{
                ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }}
        }}

        function initParticles() {{
            particles = [];
            for (let i = 0; i < 100; i++) {{ // 100 pontos brilhantes
                particles.push(new Particle());
            }}
        }}

        function animateParticles() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {{
                p.update();
                p.draw();
            }});
            requestAnimationFrame(animateParticles);
        }}

        initParticles();
        animateParticles();
    </script>
</body>
</html>
"""

components.html(html_completo, height=900) # Ajuste a altura se precisar de mais espaço
