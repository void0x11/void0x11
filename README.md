<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ahmed Amin | GitHub Profile</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            padding: 20px;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .logo {
            margin-bottom: 20px;
        }
        
        .logo img {
            max-width: 400px;
            height: auto;
        }
        
        .typing-container {
            margin: 30px 0;
            min-height: 65px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .typing-text {
            font-size: 28px;
            font-weight: bold;
            color: #1fd454;
            font-family: 'Fira Code', monospace;
        }
        
        .typing-cursor {
            display: inline-block;
            width: 3px;
            height: 28px;
            background-color: #1fd454;
            margin-left: 5px;
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
        }
        
        .social-icons a {
            display: inline-block;
            transition: transform 0.3s ease;
        }
        
        .social-icons a:hover {
            transform: scale(1.2);
        }
        
        .social-icons img {
            width: 32px;
            height: 32px;
        }
        
        .signature {
            margin: 40px 0;
            text-align: center;
        }
        
        .signature img {
            max-width: 500px;
            width: 100%;
            height: auto;
        }
        
        .section {
            margin: 40px 0;
            padding: 20px;
            background-color: #161b22;
            border-radius: 10px;
        }
        
        .section-title {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            font-size: 24px;
            color: #58a6ff;
        }
        
        .section-title img {
            margin-right: 10px;
        }
        
        .about-content {
            display: flex;
            align-items: flex-start;
            gap: 20px;
        }
        
        .about-text {
            flex: 1;
        }
        
        .about-gif {
            flex-shrink: 0;
        }
        
        .ctf-profiles {
            text-align: center;
            margin: 30px 0;
        }
        
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin: 20px 0;
        }
        
        .tech-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 80px;
        }
        
        .tech-item img {
            width: 50px;
            height: 50px;
            margin-bottom: 10px;
        }
        
        .stats {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
            margin: 30px 0;
        }
        
        .stats img {
            max-width: 100%;
            height: auto;
        }
        
        @media (max-width: 768px) {
            .about-content {
                flex-direction: column;
            }
            
            .logo img {
                max-width: 280px;
            }
            
            .typing-text {
                font-size: 22px;
            }
            
            .signature img {
                max-width: 300px;
            }
            
            .tech-stack {
                gap: 15px;
            }
            
            .tech-item {
                width: 70px;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <div class="header">
        <div class="logo">
            <a href="https://www.linkedin.com/in/void0x11/">
                <img src="https://github.com/void0x11/void0x11/blob/main/2.png?raw=true" alt="Ahmed Amin">
            </a>
        </div>
        
        <div class="typing-container">
            <div class="typing-text">
                <span id="typing"></span>
                <span class="typing-cursor"></span>
            </div>
        </div>
        
        <div class="social-icons">
            <a href="https://twitter.com/void0x10" title="X">
                <img src="https://github.com/void0x11/void0x11/blob/main/twitter-circle.svg?raw=true" alt="X">
            </a>
            <a href="https://www.linkedin.com/in/void0x11/" title="LinkedIn">
                <img src="https://github.com/void0x11/void0x11/blob/main/linkedin.svg?raw=true" alt="LinkedIn">
            </a>
        </div>
        
        <div class="signature">
            <img src="https://github.com/void0x11/void0x11/blob/main/Logo.png?raw=true" alt="Signature">
        </div>
    </div>

    <!-- About Me Section -->
    <div class="section">
        <div class="section-title">
            <img src="https://github.com/void0x11/void0x11/blob/main/about_me.gif?raw=true" width="50" alt="About me">
            <h2>About me</h2>
        </div>
        <div class="about-content">
            <div class="about-text">
                <p>- 👋 Hi, I'm Void</p>
                <p>- 👀 I'm a Tech Enthusiast.</p>
                <p>- 🌱 I'm currently studying at SUU</p>
                <p>- 💞️ I'm looking to collaborate with Embedded, Electronics or Cyber Security Projects.</p>
                <p>- Feel free to connect with me on Linkedin.</p>
                <p>- Learning new technologies everyday to become better than my past self.</p>
            </div>
            <div class="about-gif">
                <img src="https://github.com/void0x11/void0x11/blob/main/giphy.gif?raw=true" alt="Coding GIF">
            </div>
        </div>
    </div>

    <!-- CTF Profiles Section -->
    <div class="section">
        <h2 class="section-title">CTF profiles:</h2>
        <div class="ctf-profiles">
            <a href="https://tryhackme.com/p/void0x11"><img src="https://tryhackme-badges.s3.amazonaws.com/void0x11.png" height="50" alt="TryHackMe"></a>
            <a href="https://app.hackthebox.com/profile/839521"><img src="https://www.hackthebox.com/badge/image/839521" height="50" alt="HackTheBox"></a>
        </div>
    </div>

    <!-- Tech Stack Section -->
    <div class="section">
        <h2 class="section-title">Tech Stack:</h2>
        <div class="tech-stack">
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/cpp-icon.svg" alt="C++">
                <span>C++</span>
            </div>
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/python-icon.svg" alt="Python">
                <span>Python</span>
            </div>
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/github-icon.svg" alt="GitHub">
                <span>GitHub</span>
            </div>
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/mysql-icon.svg" alt="MySQL">
                <span>MySQL</span>
            </div>
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/java-icon.svg" alt="Java">
                <span>Java</span>
            </div>
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/js-icon.svg" alt="JavaScript">
                <span>JavaScript</span>
            </div>
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/ts-icon.svg" alt="TypeScript">
                <span>TypeScript</span>
            </div>
            <div class="tech-item">
                <img src="https://techstack-generator.vercel.app/docker-icon.svg" alt="Docker">
                <span>Docker</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" alt="C">
                <span>C</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg" alt="R">
                <span>R</span>
            </div>
            <div class="tech-item">
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="MATLAB">
                <span>MATLAB</span>
            </div>
            <div class="tech-item">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg" alt="Ruby">
                <span>Ruby</span>
            </div>
            <div class="tech-item">
                <img src="https://github.com/void0x11/void0x11/blob/main/ASM_Logo.svg?raw=true" alt="ASM">
                <span>ASM</span>
            </div>
        </div>
    </div>

    <!-- GitHub Stats Section -->
    <div class="section">
        <h2 class="section-title">GitHub Stats:</h2>
        <div class="stats">
            <img src="https://github-readme-stats.vercel.app/api?username=void0x11&theme=tokyonight&hide_border=false&include_all_commits=true&count_private=true" alt="GitHub Stats">
            <img src="https://github-readme-streak-stats.herokuapp.com/?user=void0x11&theme=tokyonight&hide_border=false" alt="GitHub Streak">
        </div>
    </div>

    <!-- Top Contributed Repo Section -->
    <div class="section">
        <h2 class="section-title">Top Contributed Repo</h2>
        <div class="stats">
            <img src="https://github-contributor-stats.vercel.app/api?username=void0x11&limit=5&theme=tokyonight&combine_all_yearly_contributions=true" alt="Top Contributed Repo">
        </div>
    </div>

    <script>
        // Typing animation simulation
        const texts = ["Researcher", "Electronics Engineer", "AI/Cyber Enthusiast"];
        let textIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        let typingDelay = 100;
        let eraseDelay = 50;
        let newTextDelay = 2000;
        
        function type() {
            const currentText = texts[textIndex];
            const typingElement = document.getElementById("typing");
            
            if (isDeleting) {
                // Remove characters
                typingElement.textContent = currentText.substring(0, charIndex - 1);
                charIndex--;
                typingDelay = eraseDelay;
            } else {
                // Add characters
                typingElement.textContent = currentText.substring(0, charIndex + 1);
                charIndex++;
                typingDelay = 100;
            }
            
            // Check if current text is complete
            if (!isDeleting && charIndex === currentText.length) {
                isDeleting = true;
                typingDelay = newTextDelay;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                textIndex = (textIndex + 1) % texts.length;
                typingDelay = 500;
            }
            
            setTimeout(type, typingDelay);
        }
        
        // Start the typing effect when the page loads
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(type, 1000);
        });
    </script>
</body>
</html>
