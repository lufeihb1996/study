/**
 * Interactive Life Reset Guide - Application Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------------------------
    // 1. Initialise Lucide Icons
    // ----------------------------------------------------------------------
    if (window.lucide) {
        lucide.createIcons();
    }

    // ----------------------------------------------------------------------
    // 2. Elements Selection
    // ----------------------------------------------------------------------
    // Input Fields
    const inputAntiVision = document.getElementById('inputAntiVision');
    const inputVision = document.getElementById('inputVision');
    const inputFear = document.getElementById('inputFear');
    const habit1 = document.getElementById('habit1');
    const habit2 = document.getElementById('habit2');
    const habit3 = document.getElementById('habit3');

    // Status Badges
    const status1 = document.getElementById('saveStatus1');
    const status2 = document.getElementById('saveStatus2');
    const status3 = document.getElementById('saveStatus3');

    // Summary Elements
    const summaryAnti = document.getElementById('summaryAnti');
    const summaryVision = document.getElementById('summaryVision');
    const summaryHabits = document.getElementById('summaryHabits');

    // Action Buttons
    const btnExport = document.getElementById('btnExport');
    const themeToggle = document.getElementById('themeToggle');
    
    // Nav & Scroll elements
    const progressBar = document.getElementById('progressBar');
    const sections = document.querySelectorAll('.doc-section');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Language Tabs
    const langTabBtns = document.querySelectorAll('.lang-tab-btn');

    // ----------------------------------------------------------------------
    // 3. Theme Toggle Setup
    // ----------------------------------------------------------------------
    const savedTheme = localStorage.getItem('life-reset-theme') || 'dark';
    const darkIcon = document.querySelector('.theme-icon-dark');
    const lightIcon = document.querySelector('.theme-icon-light');

    if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
        darkIcon.classList.add('hidden');
        lightIcon.classList.remove('hidden');
    }

    themeToggle.addEventListener('click', () => {
        const isLight = document.body.classList.toggle('light-theme');
        localStorage.setItem('life-reset-theme', isLight ? 'light' : 'dark');
        
        if (isLight) {
            darkIcon.classList.add('hidden');
            lightIcon.classList.remove('hidden');
        } else {
            darkIcon.classList.remove('hidden');
            lightIcon.classList.add('hidden');
        }
    });

    // ----------------------------------------------------------------------
    // 4. Language Selection Switching Logic
    // ----------------------------------------------------------------------
    const savedLangMode = localStorage.getItem('life-reset-lang-mode') || 'bilingual';
    
    const applyLangMode = (mode) => {
        // Set body class
        document.body.classList.remove('view-mode-bilingual', 'view-mode-en', 'view-mode-zh');
        document.body.classList.add(`view-mode-${mode}`);
        
        // Highlight active button
        langTabBtns.forEach(btn => {
            if (btn.getAttribute('data-lang-mode') === mode) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        
        // Save to storage
        localStorage.setItem('life-reset-lang-mode', mode);
        
        // Recalculate ScrollSpy layout since heights change
        setTimeout(handleScroll, 100);
    };

    // Initialize Language Mode
    applyLangMode(savedLangMode);

    // Click handler
    langTabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const mode = btn.getAttribute('data-lang-mode');
            applyLangMode(mode);
        });
    });

    // ----------------------------------------------------------------------
    // 5. Input Persistence (Local Storage Sync)
    // ----------------------------------------------------------------------
    const inputsMap = {
        'anti-vision': { el: inputAntiVision, status: status1 },
        'vision': { el: inputVision, status: status2 },
        'fear': { el: inputFear, status: status2 },
        'habit1': { el: habit1, status: status3 },
        'habit2': { el: habit2, status: status3 },
        'habit3': { el: habit3, status: status3 }
    };

    // Load saved data safely
    Object.keys(inputsMap).forEach(key => {
        if (inputsMap[key].el) {
            const savedVal = localStorage.getItem(`life-reset-${key}`);
            if (savedVal !== null) {
                inputsMap[key].el.value = savedVal;
            }
        }
    });

    // Update Live Summary Panel safely
    const updateSummary = () => {
        if (summaryAnti && inputAntiVision) {
            summaryAnti.innerText = inputAntiVision.value.trim() || '未填写';
        }
        
        if (summaryVision && inputVision && inputFear) {
            const visionText = inputVision.value.trim();
            const fearText = inputFear.value.trim();
            
            let visionSummary = '';
            if (visionText) visionSummary += `愿景：${visionText}；`;
            if (fearText) visionSummary += `恐惧：${fearText}`;
            summaryVision.innerText = visionSummary.trim() || '未填写';
        }

        if (summaryHabits && habit1 && habit2 && habit3) {
            const h1 = habit1.value.trim();
            const h2 = habit2.value.trim();
            const h3 = habit3.value.trim();
            
            const habitsList = [];
            if (h1) habitsList.push(`1. ${h1}`);
            if (h2) habitsList.push(`2. ${h2}`);
            if (h3) habitsList.push(`3. ${h3}`);

            summaryHabits.innerText = habitsList.length > 0 ? habitsList.join(' | ') : '未填写';
        }
    };

    // Initial update
    updateSummary();

    // Auto-save logic with debounce
    const saveTimeouts = {};
    const triggerSave = (key) => {
        clearTimeout(saveTimeouts[key]);
        const config = inputsMap[key];
        if (!config || !config.el) return;
        
        // Show saving feedback
        if (config.status) {
            config.status.classList.add('show');
            const dot = config.status.querySelector('.dot');
            const label = config.status.querySelector('span:not(.dot)');
            if (dot) dot.style.backgroundColor = '#f59e0b';
            if (label) label.innerText = '正在保存...';
        }

        saveTimeouts[key] = setTimeout(() => {
            if (config.el) {
                localStorage.setItem(`life-reset-${key}`, config.el.value);
                updateSummary();
            }
            
            // Show saved success feedback
            if (config.status) {
                const dot = config.status.querySelector('.dot');
                const label = config.status.querySelector('span:not(.dot)');
                if (dot) dot.style.backgroundColor = '#10b981';
                if (label) label.innerText = '已自动保存';
                
                setTimeout(() => {
                    config.status.classList.remove('show');
                }, 2000);
            }
        }, 800);
    };

    // Bind input listeners
    Object.keys(inputsMap).forEach(key => {
        if (inputsMap[key].el) {
            inputsMap[key].el.addEventListener('input', () => triggerSave(key));
        }
    });

    // ----------------------------------------------------------------------
    // 6. Progress Indicator & Scroll Navigation Tracking (ScrollSpy)
    // ----------------------------------------------------------------------
    function handleScroll() {
        // Page progress bar
        const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = totalHeight > 0 ? (window.scrollY / totalHeight) * 100 : 0;
        progressBar.style.width = `${progress}%`;

        // Active sections tracking
        let currentSectionId = '';
        const scrollPosition = window.scrollY + 180; // offset for the larger header in mobile

        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            
            if (scrollPosition >= top && scrollPosition < top + height) {
                currentSectionId = section.getAttribute('id');
                section.classList.add('active-section');
            } else {
                section.classList.remove('active-section');
            }
        });

        // Set active link in sidebar
        if (currentSectionId) {
            navLinks.forEach(link => {
                if (link.getAttribute('href') === `#${currentSectionId}`) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            });
        }
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // init on load

    // Smooth navigation click
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            
            // Automatically switch language view mode when clicking original-en, translation-zh, or bilingual-split
            if (targetId === '#original-en') {
                applyLangMode('en');
            } else if (targetId === '#translation-zh') {
                applyLangMode('zh');
            } else if (targetId === '#bilingual-split') {
                applyLangMode('bilingual');
            }

            setTimeout(() => {
                const targetEl = document.querySelector(targetId);
                if (targetEl) {
                    const headerOffset = window.innerWidth <= 900 ? 80 : 90;
                    const targetOffset = targetEl.offsetTop - headerOffset;
                    
                    window.scrollTo({
                        top: Math.max(0, targetOffset),
                        behavior: 'smooth'
                    });
                    
                    history.pushState(null, null, targetId);
                }
            }, 60);
        });
    });

    // ----------------------------------------------------------------------
    // 7. Export Blueprint Functionality
    // ----------------------------------------------------------------------
    btnExport.addEventListener('click', () => {
        const dateStr = new Date().toISOString().split('T')[0];
        const antiVisionVal = inputAntiVision.value.trim() || '（未填写）';
        const visionVal = inputVision.value.trim() || '（未填写）';
        const fearVal = inputFear.value.trim() || '（未填写）';
        const h1Val = habit1.value.trim() || '（未填写）';
        const h2Val = habit2.value.trim() || '（未填写）';
        const h3Val = habit3.value.trim() || '（未填写）';

        const blueprintTemplate = `# 我的个人人生重构蓝图 (Personal Life Reset Blueprint)
生成日期: ${dateStr}
根据 Dan Koe 的《如何在一天内重构整个人生》框架设计

---

## 1. 我的反向愿景 (My Anti-Vision)
> 写下你 5~10 年后绝对不想沦落到的状态，用痛苦作为前进的负反馈燃料。

${antiVisionVal}

---

## 2. 真实愿景 (My True Vision)
> 去除社会灌输的虚荣后，你真正渴望、认同的生活状态。

${visionVal}

---

## 3. 深层恐惧 (My Deep Fears)
> 拦在改变道路上的心理阻碍，以及你需要直面去战胜的事情。

${fearVal}

---

## 4. 日常核心习惯系统 (My Daily Systems)
> 像电子游戏中的“每日任务”一样，每天必须完成的 3 个简单核心行为，用于重新巩固新身份。

- **任务 01 (健康/体能):** ${h1Val}
- **任务 02 (事业/创造):** ${h2Val}
- **任务 03 (心理/学习):** ${h3Val}

---

*“你目前拥有的生活，是配合你当前身份而运转的结果。如果你的自我认同没有改变，你做出的任何临时努力都会被拉回到原点。从每天的微小任务开始，在大脑中重新构建新身份的自我认同。”*
`;

        const blob = new Blob([blueprintTemplate], { type: 'text/markdown;charset=utf-8;' });
        const link = document.createElement('a');
        const url = URL.createObjectURL(blob);
        
        link.setAttribute('href', url);
        link.setAttribute('download', `life_reset_blueprint_${dateStr}.md`);
        link.style.visibility = 'hidden';
        
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        // Show download feedback on button
        const span = btnExport.querySelector('span');
        const icon = btnExport.querySelector('i');
        const originalText = span.innerText;
        
        span.innerText = '蓝图导出成功！';
        btnExport.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
        btnExport.style.boxShadow = '0 4px 15px rgba(16, 185, 129, 0.4)';
        
        setTimeout(() => {
            span.innerText = originalText;
            btnExport.style.background = '';
            btnExport.style.boxShadow = '';
        }, 3000);
    });

    // ----------------------------------------------------------------------
    // 8. Mobile Menu Drawer Toggle
    // ----------------------------------------------------------------------
    const menuToggle = document.getElementById('menuToggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            document.body.classList.toggle('sidebar-open');
        });
    }

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (document.body.classList.contains('sidebar-open')) {
            const sidebar = document.querySelector('.nav-sidebar');
            if (sidebar && !sidebar.contains(e.target) && menuToggle && !menuToggle.contains(e.target)) {
                document.body.classList.remove('sidebar-open');
            }
        }
    });

    // Close menu when clicking a nav link
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            document.body.classList.remove('sidebar-open');
        });
    });
});
