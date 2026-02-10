import streamlit as st
import streamlit.components.v1 as components

# Força o Streamlit a usar a tela cheia e esconder elementos padrão
st.set_page_config(page_title="Para Minha Princesa", layout="wide", initial_sidebar_state="collapsed")

# Esconde o menu e o rodapé do Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body { margin: 0; }
    </style>
""", unsafe_allow_html=True)

# Link da Poesia Acústica #2 (Já no ponto da frase)
musica_url = "https://www.youtube.com/embed/m0py2-J6TN4?autoplay=1&start=0"

html_completo = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&family=Dancing+Script:wght@700&display=swap');

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #000000);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            font-family: 'Poppins', sans-serif;
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow-x: hidden;
            padding: 50px 20px;
        }}

        @keyframes gradient {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        canvas {{ position: fixed; top: 0; left: 0; z-index: 0; pointer-events: none; }}

        .container {{
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 800px;
            display: none; /* Escondido até o clique */
            flex-direction: column;
            gap: 20px;
            align-items: center;
        }}

        /* Estilo dos Cards de Elogio */
        .card-elogio {{
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            width: 90%;
            max-width: 400px;
            text-align: center;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            animation: slideIn 1s ease-out;
        }}

        /* Card Principal da Música */
        .card-principal {{
            background: rgba(255, 0, 80, 0.1);
            backdrop-filter: blur(15px);
            border: 2px solid #ff0050;
            padding: 40px 20px;
            border-radius: 25px;
            width: 100%;
            text-align: center;
            margin-top: 30px;
            box-shadow: 0 0 50px rgba(255, 0, 80, 0.2);
        }}

        .title {{ font-family: 'Dancing Script', cursive; font-size: 2.5rem; color: #ff0050; margin-bottom: 10px; }}
        .highlight {{ color: #ff0050; font-weight: 600; }}
        .letra {{ font-style: italic; font-size: 1.2rem; line-height: 1.6; margin: 20px 0; }}

        .btn-abrir {{
            background: #ff0050;
            color: white;
            border: none;
            padding: 20px 50px;
            border-radius: 50px;
            font-size: 1.5rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 0 30px rgba(255, 0, 80, 0.5);
            z-index: 20;
            transition: 0.3s;
        }}

        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        iframe {{ border-radius: 15px; margin-top: 20px; width: 100%; max-width: 500px; height: 80px; }}
    </style>
</head>
<body>
    <canvas id="stars"></canvas>

    <button id="btn" class="btn-abrir" onclick="iniciar()">Clique aqui ❤️</button>

    <div id="content" class="container">
        
        <div class="card-elogio">Você é a dona de tudo em mim, minha <span class="highlight">Pequenina</span>.</div>
        <div class="card-elogio">O mundo fica mais bonito quando você sorri, minha <span class="highlight">Princesa</span>.</div>
        <div class="card-elogio">Minha parceira, meu porto seguro, meu grande amor.</div>
        <div class="card-elogio">Nunca esqueça que você é única e preciosa para mim.</div>

        <div class="card-principal">
            <h1 class="title">Poesia Acústica #2</h1>
            <p class="letra">
                "E cada vez que eu olho nos teus olhos<br>
                Te espelho com desejo, eu te beijo e me vejo<br>
                <span class="highlight">decretando o fim."</span>
            </p>
            <iframe src="{musica_url}" frameborder="0" allow="autoplay"></iframe>
        </div>

    </div>

    <script>
        function iniciar() {{
            document.getElementById('btn').style.display = 'none';
            document.getElementById('content').style.display = 'flex';
        }}

        // Fundo de estrelas
        const canvas = document.getElementById('stars');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        let p = [];

        class Part {{
            constructor() {{
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.s = Math.random() * 2;
                this.v = Math.random() * 0.5;
            }}
            draw() {{
                ctx.fillStyle = "white";
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.s, 0, Math.PI*2);
                ctx.fill();
            }}
            up() {{
                this.y -= this.v;
                if(this.y < 0) this.y = canvas.height;
            }}
        }}

        for(let i=0; i<100; i++) p.push(new Part());
        function anim() {{
            ctx.clearRect(0,0,canvas.width, canvas.height);
            p.forEach(x => {{ x.up(); x.draw(); }});
            requestAnimationFrame(anim);
        }}
        anim();
    </script>
</body>
</html>
"""

components.html(html_completo, height=1200, scrolling=True)
