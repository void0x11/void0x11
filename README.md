<h1 align="center">
  <a href="https://www.linkedin.com/in/void0x11/">
    <img src="https://github.com/void0x11/void0x11/blob/main/2.png" alt="Ahmed Amin" width="400px" height="60px" /></a>
</h1>

<p align="center">
  <span id="typing-container" style="font-family: 'Fira Code', monospace; font-size: 28px; color: #1FD454; min-height: 55px; display: block;">
    <span id="typing-text"></span>
    <span style="display: inline-block; width: 3px; height: 28px; background-color: #1FD454; animation: blink 1s infinite;"></span>
  </span>
</p>

<style>
  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
  }
</style>

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
    const typingElement = document.getElementById("typing-text");
    
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

<!-- Social icons section -->
<p align="center">
  <a href="https://twitter.com/void0x10"><img width="32px" alt="X" title="X" src="https://github.com/void0x11/void0x11/blob/main/twitter-circle.svg"></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
  <a href="https://www.linkedin.com/in/void0x11/" alt="Linkedin" title="Linkedin"><img width="32px" src="https://github.com/void0x11/void0x11/blob/main/linkedin.svg"/></a>
  &#8287;&#8287;&#8287;&#8287;&#8287;
</p>

<div align="center">
    <picture> <img align="center" src="https://github.com/void0x11/void0x11/blob/main/Logo.png" width = 500px></picture>
</div>

## <picture><img src = "https://github.com/void0x11/void0x11/blob/main/about_me.gif" width = 50px></picture> **About me**
<picture> <img align="right" src="https://github.com/void0x11/void0x11/blob/main/giphy.gif"></picture>

- 👋 Hi, I’m Void
- 👀 I’m a Tech Enthusiast.
- 🌱 I’m currently studying at SUU
- 💞️ I’m looking to collaborate with Embedded, Electronics or Cyber Security Projects.
- Feel free to connect with me on Linkedin.
- Learning new technologies everyday to become better than my past self.

<br>
<br>

## :triangular_flag_on_post: CTF profiles:

<div align="center">
 <a href="https://tryhackme.com/p/void0x11"><img src="https://tryhackme-badges.s3.amazonaws.com/void0x11.png" height=50 alt="TryHackMe"></a>
 <a href="https://app.hackthebox.com/profile/839521"><img src="https://www.hackthebox.com/badge/image/839521" height=50 alt="HackTheBox"></a>
</div>


# 💻 Tech Stack:
<div style="display: flex; align-items: center;">
  <img src="https://techstack-generator.vercel.app/cpp-icon.svg" alt="C++ icon" width="100" style="margin-right: 100px;" />
  <img src="https://techstack-generator.vercel.app/python-icon.svg" alt="Python icon" width="100" style="margin-right: 100px;" />
  <img src="https://techstack-generator.vercel.app/github-icon.svg" alt="GitHub icon" width="100" style="margin-right: 100px;" />
  <img src="https://techstack-generator.vercel.app/mysql-icon.svg" alt="MySQL icon" width="100" style="margin-right: 100px;" />
  <img src="https://techstack-generator.vercel.app/java-icon.svg" alt="Java icon" width="100" style="margin-right: 100px;" />
  <img src="https://techstack-generator.vercel.app/js-icon.svg" alt="JavaScript icon" width="100" style="margin-right: 100px;" />
  <img src="https://techstack-generator.vercel.app/ts-icon.svg" alt="TypeScript icon" width="100" style="margin-right: 100px;" />
  <img src="https://techstack-generator.vercel.app/docker-icon.svg" alt="Docker icon" width="100" style="margin-right: 100px;" />

  <!-- C -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" alt="C icon" width="100" style="margin-right: 70px;" />
  <!-- R -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg" alt="R icon" width="100" style="margin-right: 70px;" />
  <!-- MATLAB -->
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/Matlab_Logo.png" alt="MATLAB icon" width="100" style="margin-right: 70px;" />
  <!-- Ruby -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg" alt="Ruby icon" width="100" style="margin-right: 70px;" />
  <!-- ASM -->
  <img src="https://github.com/void0x11/void0x11/blob/main/ASM_Logo.svg" alt="ASM logo" width="100" style="margin-right: 100px;" />
</div>


</div>

<br>

# 📊 GitHub Stats:
<p align="center">
  <a href="https://github.com/void0x11">
    <!-- Card 1: GitHub Stats -->
    <img align="center" src="https://github-readme-stats.vercel.app/api?username=void0x11&theme=tokyonight&hide_border=false&include_all_commits=true&count_private=true" width=500/>
  </a>
  <br>
  <br>
  <a href="https://github.com/void0x11">
    <!-- Card 2: GitHub Streak Stats -->
    <img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=void0x11&theme=tokyonight&hide_border=false" width=500/>
  </a>
</p>

<br>

### 🔝 Top Contributed Repo
<p align="center">
  <img align="center" src="https://github-contributor-stats.vercel.app/api?username=void0x11&limit=5&theme=tokyonight&combine_all_yearly_contributions=true" width=500 height=250 />
</p>

<br>
