<div align="center">

<!-- ANIMATED SVG 01: HERO (Opens Abhishek's Live Portfolio) -->
<a href="https://portfolio.getchintu.com">
  <img src="./assets/hero.svg?v=3" alt="Abhishek Tiwari — Hero Profile" width="100%" />
</a>

<br/><br/>

<!-- ANIMATED SVG 02: ABOUT & CAPABILITIES CAROUSEL (Jumps to Experience / Battle Log) -->
<a href="#experience">
  <img src="./assets/about-life.svg?v=7" alt="Abhishek Tiwari — Capabilities & Life Philosophy" width="100%" />
</a>

<br/><br/>

<!-- ANIMATED SVG 03: TECH ARSENAL ORBITS (Jumps to Shipped & Deployed Projects) -->
<a href="#projects">
  <img src="./assets/stack.svg?v=7" alt="Abhishek Tiwari — Revolving Tech Galaxy" width="100%" />
</a>

<br/><br/>

<!-- ANIMATED SVG 04: ID BADGE & VERIFIED METRICS (Opens GitHub Repositories) -->
<a href="https://github.com/Abhishek6827?tab=repositories">
  <img src="./assets/id-dashboard.svg?v=3" alt="Abhishek Tiwari — ID Badge & Credentials Dashboard" width="100%" />
</a>

<br/><br/>

<!-- SECTION 05: CONNECT & SOCIAL CTA -->
<img src="./assets/connect-header.svg?v=2" alt="Connect with Abhishek Tiwari" width="100%" />

<br/><br/>

<a href="https://www.linkedin.com/in/abhishek-tiwariiii">
  <img src="./assets/connect-linkedin.svg?v=2" alt="LinkedIn Profile" width="49%" />
</a>
<a href="https://portfolio.getchintu.com">
  <img src="./assets/connect-portfolio.svg?v=2" alt="Personal Portfolio" width="49%" />
</a>

<br/>

<a href="https://getchintu.com">
  <img src="./assets/connect-chintu.svg?v=2" alt="CHINTU AI Platform" width="49%" />
</a>
<a href="mailto:abhishektiwari@getchintu.com">
  <img src="./assets/connect-email.svg?v=2" alt="Direct Email" width="49%" />
</a>

<br/><br/>

<!-- SECTION 03: BATTLE LOG (EXPERIENCE TIMELINE) -->
<a id="experience"></a>
<a href="#experience">
  <img src="./assets/battle-log.svg?v=2" alt="Abhishek Tiwari — Battle Log Experience Timeline" width="100%" />
</a>

<br/><br/>

<!-- SECTION 04: SHIPPED & DEPLOYED FLAGSHIP PROJECTS -->
<a id="projects"></a>

<!-- Project 01: CHINTU AI -->
<a href="https://getchintu.com">
  <img src="./assets/project-chintu.svg?v=2" alt="CHINTU AI — Flagship Project 01" width="100%" />
</a>

<br/><br/>

<!-- Project 02: AI Resume Tailor & LaTeX Engine (AWS + Java Spring Boot) -->
<a href="https://resume.getchintu.com">
  <img src="./assets/project-resume.svg?v=3" alt="AI Resume Tailor & LaTeX Engine — Flagship Project 02" width="100%" />
</a>

<br/><br/>

<!-- Project 03: Social Connect -->
<a href="https://socialconnect.getchintu.com/login">
  <img src="./assets/project-social.svg?v=2" alt="Social Connect — Flagship Project 03" width="100%" />
</a>

<br/><br/>

<!-- Project 04: YouTube Automation -->
<a href="https://automation.getchintu.com">
  <img src="./assets/project-youtube.svg?v=3" alt="YouTube Automation — Flagship Project 04" width="100%" />
</a>

<br/><br/>

</div>

<!-- ============================================================== -->
<!-- SECTION: AI RESEARCH, LLM EVALS & SECURITY BENCHMARKS          -->
<!-- ============================================================== -->
<a id="ai-benchmarks"></a>

### ⚡ AI Systems, LLM Evals & Security Engineering

Empirical evaluation frameworks, adversarial red-teaming (OWASP LLM01), and production performance optimization.

| Priority & Focus | Project & Repository | Core Architecture & Mitigation | Key Benchmark Metrics | Stack & Verification |
|:---:|:---|:---|:---|:---:|
| 🥇 **#1 High-Impact**<br/>**AI Safety / Security** | [**RAG Prompt Injection & Defense Audit**](https://github.com/Abhishek6827/rag-prompt-injection-audit)<br/>*(OWASP GenAI Top 10 — LLM01)* | • **3-Tier Defense-in-Depth:** XML Data Spotlighting, Pre-Retrieval Heuristic Scanner, and Output Canary Regex Redactor.<br/>• **10 Poisoned Attack Vectors:** Delimiter breakouts, role-play switches, Hindi transliterated attacks, and markdown link exfiltration.<br/>• Programmatic synthetic canary tracking (`TIGER-42`, `ACCT-99887766`). | **• 10/10 → 0/10 Breaches** (100% Defense Rate)<br/>**• 0 False Blocks** on 20 legitimate corporate inquiries<br/>**• 1.8ms Average Latency Overhead** | ![Python](https://img.shields.io/badge/Python_3.14-3776AB?style=flat-square&logo=python&logoColor=white)<br/>![Coverage](https://img.shields.io/badge/Coverage-98%25-brightgreen?style=flat-square)<br/>![OWASP](https://img.shields.io/badge/OWASP-LLM01-blue?style=flat-square) |
| 🥈 **#2 High-Impact**<br/>**Evals & Alignment** | [**LLM-as-a-Judge Bias Audit & Calibration**](https://github.com/Abhishek6827/llm-judge-audit)<br/>*(Statistical Alignment & Evals)* | • **3-Dimensional Bias Audit:** Measures position bias (order permutation), verbosity/length bias (+150 filler words), and model self-preference.<br/>• **Statistical Alignment:** Calculates raw match % and Cohen's Kappa agreement against blinded human ground truth.<br/>• **Bidirectional Consensus Calibration:** Dual-order evaluation protocol mitigating position bias flips. | **• Agreement Calibrated:** 26/30 → 28/30 (+6.7% boost)<br/>**• Position Bias Quantified:** 4/30 verdicts flipped by presentation order<br/>**• Verbosity Bias Neutralized:** 0 filler score inflation under consensus | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)<br/>![Evals](https://img.shields.io/badge/Cohen's_Kappa-0.78-blueviolet?style=flat-square)<br/>![Coverage](https://img.shields.io/badge/Coverage-93%25-brightgreen?style=flat-square) |
| 🥉 **#3 High-Impact**<br/>**Latency & Systems** | [**Semantic Cache for FAQ Bot**](https://github.com/Abhishek6827/semantic-cache-faq)<br/>*(Latency, Cost & Multilingual Guard)* | • **Automated Threshold Sweep:** Sweeps cosine similarity thresholds (0.75-0.95) across 100 labeled technical & FAQ queries.<br/>• **Multilingual Negation Guard:** Lexical token parity check preventing false cache hits across Hindi/English negations (*"refund milega"* vs *"refund nahi milega"*).<br/>• **Cache Hygiene:** TTL-based expiry and PII scrubbers (order IDs, phone numbers, emails). | **• 67% LLM Call Reduction** (Hit rate: 67%)<br/>**• 350x Speedup:** Latency down from 420ms to 1.2ms<br/>**• 0 False Hits** at optimal 0.85 threshold | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)<br/>![Latency](https://img.shields.io/badge/Latency-1.2ms-success?style=flat-square)<br/>![Coverage](https://img.shields.io/badge/Coverage-84%25-brightgreen?style=flat-square) |

<br/>

<div align="center">

<!-- SECTION 06: MORE PROJECTS (ECOSYSTEM PRODUCTION APPS) -->
<a href="https://portfolio.getchintu.com">
  <img src="./assets/more-projects-header.svg?v=2" alt="Abhishek Tiwari — Ecosystem Production Apps" width="100%" />
</a>

<br/><br/>

<a href="https://tempomail.getchintu.com">
  <img src="./assets/tile-tempusmail.svg?v=2" alt="Tempusmail" width="49%" />
</a>
<a href="https://abhishek6827.github.io/E-commerce/">
  <img src="./assets/tile-myntra.svg?v=2" alt="Myntra Clone" width="49%" />
</a>

<br/>

<a href="https://abhishek6827.github.io/Kanban_WorkBoard/">
  <img src="./assets/tile-kanban.svg?v=2" alt="Kanban WorkBoard" width="49%" />
</a>
<a href="https://abhishek6827.github.io/Market-Seasonality-Explorer/">
  <img src="./assets/tile-market.svg?v=2" alt="Market Explorer" width="49%" />
</a>

<br/>

<a href="https://abhishek6827.github.io/Skill_Up/">
  <img src="./assets/tile-skillup.svg?v=2" alt="Skill Up" width="49%" />
</a>
<a href="https://abhishek6827.github.io/Elante_Mall/">
  <img src="./assets/tile-elante.svg?v=2" alt="Elante Mall" width="49%" />
</a>

<br/><br/>

<!-- SECTION 06: STATS THAT SPEAK (HEADER + ANALYTICS WIDGETS) -->
<a id="stats"></a>
<a href="#stats">
  <img src="./assets/stats-header.svg?v=2" alt="Stats That Speak — Metrics Header" width="100%" />
</a>

<br/><br/>

<!-- Real-Time GitHub Analytics & Streak Cards -->
<img width="49%" src="https://github-readme-stats-7ihy.vercel.app/api?username=Abhishek6827&show_icons=true&theme=radical&hide_border=true&bg_color=070b16&title_color=38bdf8&icon_color=38bdf8&text_color=94a3b8&count_private=true&rank_icon=github" />
<img width="49%" src="https://github-readme-streak-stats-eight.vercel.app?user=Abhishek6827&theme=radical&hide_border=true&background=070b16&ring=38bdf8&fire=ff354f&currStreakLabel=38bdf8&sideNums=ffffff&sideLabels=94a3b8" />

<br/>
<!-- GitHub Top Trophies -->
<img src="https://github-profile-trophy-orpin-alpha.vercel.app/?username=Abhishek6827&theme=radical&no-frame=true&no-bg=true&column=4&row=1&margin-w=10&margin-h=10&hidden=Reviews,Followers,Issues,PullRequest" width="100%" />

<br/>
<!-- Contribution Activity Graph -->
<img src="https://github-readme-activity-graph.vercel.app/graph?username=Abhishek6827&custom_title=Abhishek's+Contribution+Graph&bg_color=070b16&color=38bdf8&line=247bff&point=ff354f&area_color=247bff&area=true&hide_border=true" width="98%" />

<br/>
<!-- Contribution Snake Animation -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake.svg" />
  <img alt="github-snake" src="https://raw.githubusercontent.com/Abhishek6827/Abhishek6827/output/github-contribution-grid-snake.svg" />
</picture>

<br/><br/>

<!-- SECTION 07: ACCREDITATIONS & CERTIFICATIONS -->
<a id="certifications"></a>
<a href="#certifications">
  <img src="./assets/certifications.svg?v=2" alt="Abhishek Tiwari — Verified Industry Certifications" width="100%" />
</a>

<br/><br/>

<!-- PROFILE VIEWS COUNTER (Restored to original count + eye icon) -->
<img src="https://img.shields.io/badge/dynamic/xml?url=https%3A%2F%2Fkomarev.com%2Fghpvc%2F%3Fusername%3DAbhishek6827&query=%2F%2F%2A%5Bname%28%29%3D%22text%22%5D%5Blast%28%29%5D&label=%F0%9F%91%81%EF%B8%8F+PROFILE+VIEWS&style=for-the-badge&color=247bff&labelColor=0b1224" alt="Profile Views" />

<br/><br/>

<!-- CLOSING QUOTE CARD -->
<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical" width="70%" />

<br/><br/>

> ⚡ *"Crafting digital experiences with modern web technologies. Passionate about creating scalable solutions that make a difference."*

</div>
