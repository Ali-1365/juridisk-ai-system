import KeyboardShortcutHandler from './keyboard-shortcuts.js';

// Initialize the keyboard shortcut handler
const shortcutHandler = new KeyboardShortcutHandler({
  onShortcutTriggered: (event) => {
    console.log('Ctrl+; or Cmd+; was pressed!');
    // Perform your desired action here
    // For example, toggle a modal, focus a search input, etc.
  }
});

// To clean up when no longer needed (e.g., in a single-page application)
// shortcutHandler.destroy();
