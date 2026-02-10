import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Para Minha Pequenina", layout="wide", initial_sidebar_state="collapsed")

# Esconde tudo que é padrão do Streamlit para o celular focar só no site
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
""", unsafe_allow_html=True)

# Link da Poesia Acústica #2 (Já configurado para autoplay)
musica_url = "https://www.youtube.com/embed/m0py2-J6TN4?autoplay=1&start=0&controls=0&modestbranding=1"

html_foda = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Montserrat:wght@300;600;800&family=Dancing+Script:wght@700&display=swap');

        * {{ margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}

        body {{
            background: #000;
            color: #fff;
            font-family: 'Montserrat', sans-serif;
            overflow-x: hidden;
            height: 100vh;
            width: 100vw;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        /* Fundo de Partículas Interativo */
        #bg-canvas {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }}

        /* Camada de Brilho Neon */
        .overlay {{
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at center, rgba(255,0,80,0.1) 0%, transparent 80%);
            z-index: 2;
            pointer-events: none;
        }}

        /* Botão de Entrada IMPACTANTE */
        #entry-screen {{
            position: fixed;
            z-index: 999;
            width: 100%;
            height: 100%;
            background: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: opacity 1s ease;
        }}

        .btn-portal {{
            padding: 20px 40px;
            font-family: 'Syncopate', sans-serif;
            font-size: 0.8rem;
            letter-spacing: 5px;
            color: #ff0050;
            background: transparent;
            border: 1px solid #ff0050;
            text-transform: uppercase;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(255, 0, 80, 0.4);
            animation: pulse 2s infinite;
        }}

        /* Conteúdo Principal */
        #main-content {{
            display: none;
            z-index: 10;
            width: 90%;
            max-width: 400px;
            flex-direction: column;
            gap: 20px;
            animation: slideUp 1.5s cubic-bezier(0.23, 1, 0.32, 1);
        }}

        .card {{
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 25px;
            padding: 30px;
            text-align: left;
            position: relative;
            overflow: hidden;
        }}

        .card::before {{
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
            transition: 0.5s;
        }}

        .card-title {{
            font-family: 'Syncopate', sans-serif;
            font-size: 0.7rem;
            color: #ff0050;
            letter-spacing: 3px;
            margin-bottom: 15px;
            display: block;
        }}

        .card-text {{
            font-size: 1.1rem;
            font-weight: 300;
            line-height: 1.5;
            color: #efefef;
        }}

        .poesia-box {{
            background: linear-gradient(180deg, rgba(255,0,80,0.2) 0%, rgba(0,0,0,0) 100%);
            border: 1px solid rgba(255, 0, 80, 0.3);
            padding: 35px 25px;
            border-radius: 30px;
            text-align: center;
        }}

        .frase-impacto {{
            font-family: 'Dancing Script', cursive;
            font-size: 2rem;
            color: #fff;
            margin-bottom: 20px;
            line-height: 1.2;
            text-shadow: 0 0 15px rgba(255,0,80,0.6);
        }}

        .sub-letra {{
            font-size: 0.9rem;
            color: #ff0050;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        iframe {{
            margin-top: 25px;
            width: 100%;
            height: 60px;
            border-radius: 50px;
            opacity: 0.3;
        }}

        @keyframes pulse {{
            0% {{ box-shadow: 0 0 10px rgba(255, 0, 80, 0.4); transform: scale(1); }}
            50% {{ box-shadow: 0 0 30px rgba(255, 0, 80, 0.7); transform: scale(1.05); }}
            100% {{ box-shadow: 0 0 10px rgba(255, 0, 80, 0.4); transform: scale(1); }}
        }}

        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(100px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body>
    <canvas id="bg-canvas"></canvas>
    <div class="overlay"></div>

    <div id="entry-screen">
        <button class="btn-portal" onclick="unlock()">Iniciar Experiência</button>
    </div>

    <div id="main-content">
        <div class="card">
            <span class="card-title">01. Pequenina</span>
            <p class="card-text">Você é a prova de que as melhores coisas do mundo não são coisas, são pessoas como você.</p>
        </div>

        <div class="card">
            <span class="card-title">02. Minha Princesa</span>
            <p class="card-text">O brilho desse site não chega aos pés do que eu vejo quando você sorri pra mim.</p>
        </div>

        <div class="poesia-box">
            <p class="frase-impacto">
                "E cada vez que eu olho nos teus olhos... Te espelho com desejo, eu te beijo e me vejo"
            </p>
            <p class="sub-letra">Decretando o fim</p>
            <iframe src="{musica_url}" frameborder="0" allow="autoplay"></iframe>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('bg-canvas');
        const ctx = canvas.getContext('2d');
        let particles = [];

        function initCanvas() {{
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }}

        class Particle {{
            constructor() {{
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2;
                this.speedX = (Math.random() - 0.5) * 0.5;
                this.speedY = (Math.random() - 0.5) * 0.5;
            }}
            update() {{
                this.x += this.speedX;
                this.y += this.speedY;
                if(this.x > canvas.width) this.x = 0;
                if(this.x < 0) this.x = canvas.width;
                if(this.y > canvas.height) this.y = 0;
                if(this.y < 0) this.y = canvas.height;
            }}
            draw() {{
                ctx.fillStyle = 'rgba(255, 0, 80, 0.5)';
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
            }}
        }}

        function setup() {{
            initCanvas();
            for(let i=0; i<100; i++) particles.push(new Particle());
            animate();
        }}

        function animate() {{
            ctx.clearRect(0,0,canvas.width, canvas.height);
            particles.forEach(p => {{ p.update(); p.draw(); }});
            requestAnimationFrame(animate);
        }}

        function unlock() {{
            document.getElementById('entry-screen').style.opacity = '0';
            setTimeout(() => {{
                document.getElementById('entry-screen').style.display = 'none';
                document.getElementById('main-content').style.display = 'flex';
            }}, 1000);
        }}

        window.addEventListener('resize', initCanvas);
        setup();
    </script>
</body>
</html>
"""

components.html(html_foda, height=1200, scrolling=True)
