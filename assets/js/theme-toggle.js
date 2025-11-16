// Dark mode toggle functionality
(function() {
  'use strict';

  // Check for saved theme preference or default to dark
  function getThemePreference() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      return savedTheme;
    }
    // Default to dark mode
    return 'dark';
  }

  // Apply theme to document
  function setTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    localStorage.setItem('theme', theme);
    updateToggleButton(theme);
  }

  // Update button icon
  function updateToggleButton(theme) {
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.innerHTML = theme === 'dark' ? '☀️' : '🌙';
      button.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  // Toggle between light and dark
  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme);
  }

  // Initialize on page load
  function init() {
    const theme = getThemePreference();
    setTheme(theme);

    // Add click handler to toggle button
    const toggleButton = document.getElementById('theme-toggle');
    if (toggleButton) {
      toggleButton.addEventListener('click', toggleTheme);
    }
  }

  // Apply theme immediately to prevent flash
  const theme = getThemePreference();
  if (theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  }

  // Run init when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Listen for system theme changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
      if (!localStorage.getItem('theme')) {
        setTheme(e.matches ? 'dark' : 'light');
      }
    });
  }
})();
