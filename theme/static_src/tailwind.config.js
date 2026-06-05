/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
    '../../**/*.py',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        cyber: {
          black:   '#0a0a0f',
          navy:    '#0d1117',
          dark:    '#0f172a',
          card:    '#111827',
          border:  '#1e293b',
          cyan:    '#00f5ff',
          'cyan-dim': '#00c4cc',
          green:   '#00ff88',
          purple:  '#7c3aed',
          red:     '#ff2d55',
          text:    '#e2e8f0',
          muted:   '#64748b',
        },
      },
      fontFamily: {
        sans:  ['Inter', 'system-ui', 'sans-serif'],
        mono:  ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      backgroundImage: {
        'cyber-grid': `
          linear-gradient(rgba(0,245,255,0.03) 1px, transparent 1px),
          linear-gradient(90deg, rgba(0,245,255,0.03) 1px, transparent 1px)
        `,
      },
      backgroundSize: {
        'grid-40': '40px 40px',
      },
      boxShadow: {
        'cyber':       '0 0 20px rgba(0,245,255,0.15)',
        'cyber-lg':    '0 0 40px rgba(0,245,255,0.2)',
        'cyber-inner': 'inset 0 0 20px rgba(0,245,255,0.05)',
      },
      animation: {
        'pulse-slow':   'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow':         'glow 2s ease-in-out infinite alternate',
        'slide-in':     'slideIn 0.3s ease-out',
        'fade-in':      'fadeIn 0.4s ease-out',
      },
      keyframes: {
        glow: {
          '0%':   { boxShadow: '0 0 5px rgba(0,245,255,0.2)' },
          '100%': { boxShadow: '0 0 20px rgba(0,245,255,0.6), 0 0 40px rgba(0,245,255,0.2)' },
        },
        slideIn: {
          '0%':   { transform: 'translateX(-10px)', opacity: '0' },
          '100%': { transform: 'translateX(0)',     opacity: '1' },
        },
        fadeIn: {
          '0%':   { opacity: '0', transform: 'translateY(8px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
};
