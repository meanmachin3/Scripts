// ==UserScript==
// @name         Acronym Expander
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Double-click on acronyms to see their full forms
// @author       You
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Common acronyms database
    const acronyms = {
        // Technology
        'API': 'Application Programming Interface',ss
    };

    // Create tooltip element
    const tooltip = document.createElement('div');
    tooltip.style.cssText = `
        position: absolute;
        background: #333;
        color: white;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 14px;
        font-family: Arial, sans-serif;s
        z-index: 10000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.2s;
        max-width: 300px;
        word-wrap: break-word;
        border: 1px solid #555;
    `;
    document.body.appendChild(tooltip);

    // Function to show tooltip
    function showTooltip(text, x, y) {
        tooltip.textContent = text;
        tooltip.style.left = x + 'px';
        tooltip.style.top = (y - tooltip.offsetHeight - 10) + 'px';
        tooltip.style.opacity = '1';
        
        // Auto-hide after 3 seconds
        setTimeout(() => {
            tooltip.style.opacity = '0';
        }, 3000);
    }

    // Function to hide tooltip
    function hideTooltip() {
        tooltip.style.opacity = '0';
    }

    // Function to get selected text or word at cursor
    function getWordAtCursor(event) {
        const selection = window.getSelection();
        
        // If there's selected text, use that
        if (selection.rangeCount > 0 && !selection.isCollapsed) {
            return selection.toString().trim();
        }
        
        // Otherwise, try to get word at click position
        const range = document.caretRangeFromPoint(event.clientX, event.clientY);
        if (!range) return null;
        
        const textNode = range.startContainer;
        if (textNode.nodeType !== Node.TEXT_NODE) return null;
        
        const text = textNode.textContent;
        const offset = range.startOffset;
        
        // Find word boundaries
        let start = offset;
        let end = offset;
        
        // Move start backwards to find word beginning
        while (start > 0 && /[A-Za-z0-9]/.test(text[start - 1])) {
            start--;
        }
        
        // Move end forwards to find word end
        while (end < text.length && /[A-Za-z0-9]/.test(text[end])) {
            end++;
        }
        
        return text.substring(start, end);
    }

    // Function to check if text is likely an acronym
    function isLikelyAcronym(text) {
        if (!text || text.length < 2) return false;
        
        // Check if it's in our database
        if (acronyms[text.toUpperCase()]) return true;
        
        // Check if it looks like an acronym (all caps, 2-6 characters)
        if (/^[A-Z]{2,6}$/.test(text)) return true;
        
        // Check mixed case acronyms (like iPhone, HTML5, etc.)
        if (/^[A-Za-z0-9]{2,8}$/.test(text) && /[A-Z]/.test(text)) return true;
        
        return false;
    }

    // Main double-click handler
    document.addEventListener('dblclick', function(event) {
        const word = getWordAtCursor(event);
        
        if (!word || !isLikelyAcronym(word)) return;
        
        const upperWord = word.toUpperCase();
        const expansion = acronyms[upperWord];
        
        if (expansion) {
            showTooltip(`${word}: ${expansion}`, event.clientX, event.clientY);
        } else {
            // For unknown acronyms, show a generic message
            showTooltip(`${word}: Acronym (definition not available)`, event.clientX, event.clientY);
        }
        
        // Prevent text selection on double-click
        event.preventDefault();
    });

    // Hide tooltip on click elsewhere
    document.addEventListener('click', function(event) {
        if (event.detail !== 2) { // Not a double-click
            hideTooltip();
        }
    });

    // Hide tooltip on scroll
    document.addEventListener('scroll', hideTooltip);
    
    // Hide tooltip on key press
    document.addEventListener('keydown', hideTooltip);

    console.log('Acronym Expander loaded! Double-click on acronyms to see their full forms.');
})();