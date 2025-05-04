/**
 * Keyboard Shortcut Handler
 * Handles Ctrl+; (Windows/Linux) or Cmd+; (macOS) keyboard shortcuts
 */
class KeyboardShortcutHandler {
  constructor(options = {}) {
    // Default options
    this.options = {
      // The action to perform when the shortcut is triggered
      onShortcutTriggered: () => console.log('Shortcut triggered!'),
      // Whether to prevent the default browser behavior when the shortcut is triggered
      preventDefault: true,
      ...options
    };

    // Bind methods
    this.handleKeyDown = this.handleKeyDown.bind(this);
    
    // Initialize
    this.init();
  }

  /**
   * Initialize the keyboard shortcut handler
   */
  init() {
    document.addEventListener('keydown', this.handleKeyDown);
  }

  /**
   * Clean up event listeners
   */
  destroy() {
    document.removeEventListener('keydown', this.handleKeyDown);
  }

  /**
   * Handle keydown events
   * @param {KeyboardEvent} event - The keyboard event
   */
  handleKeyDown(event) {
    // Check if the key is semicolon (;)
    if (event.key === ';') {
      // Check if Ctrl key is pressed on Windows/Linux or Cmd key is pressed on macOS
      const isMac = /Mac|iPod|iPhone|iPad/.test(navigator.platform);
      const modifierKeyPressed = isMac ? event.metaKey : event.ctrlKey;

      if (modifierKeyPressed) {
        // Prevent default browser behavior if specified
        if (this.options.preventDefault) {
          event.preventDefault();
        }

        // Execute the callback function
        this.options.onShortcutTriggered(event);
      }
    }
  }
}

// Export the class
export default KeyboardShortcutHandler;
